from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.db.models import Count
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView,View, UpdateView

from calendar_mchp.models import ClassCalendar, CalendarEvent, Subscription
from calendar_mchp.exceptions import TimeOrderError, CalendarExpiredError, BringingUpThePastError
from lib.decorators import school_required
from referral.models import ReferralCode
from schedule.models import Course, Section
from schedule.utils import WEEK_DAYS

import stored_messages

from datetime import datetime,timedelta
from decimal import Decimal, ROUND_HALF_DOWN
import json
import logging
logger = logging.getLogger(__name__)

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ" 

class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.

    I stole this right from the django website.
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def ajax_messages(self):
        django_messages = []

        for message in messages.get_messages(self.request):
            django_messages.append({
                "level": message.level,
                "message": message.message,
                "extra_tags": message.tags,
            })
        return django_messages

    def send_ajax_error_message(self, message, **kwargs):
        messages.error(
            self.request,
            message,
        )
        data = {
            'messages': self.ajax_messages(),
        }
        status = kwargs.get('status', 500)
        return self.render_to_json_response(data, status=status)

'''
url: /calendar/create/
name: calendar_create
'''
class CalendarCreateView(View, AjaxableResponseMixin):
    template_name = 'calendar_mchp/calendar_create.html'

    def get_success_url(self):
        return reverse('calendar')

    def get(self, request, *args, **kwargs):
        courses = self.student.courses.exclude(
            id__in = self.student.calendars.all().values('course__pk')
        )
        calendars = ClassCalendar.objects.filter(
            owner = self.student,
        )
        data = {
            'calendars': calendars,
            'courses': courses,
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return redirect(reverse('calendar'))
        # were just going to forgo any fancy django form saving for this one
        calendar = self._make_calendar(request)
        try:
            calendar.save()
        except (IntegrityError, TimeOrderError) as err:
            # they made a calendar for this class
            if err.__class__ == IntegrityError:
                return self.send_ajax_error_message('You have already made a calendar for that course', status=403)
            else:
                # the start date was too early
                return self.send_ajax_error_message(str(err), status=403)
        # now add the times as sections
        return self._make_sections(request.POST.get('times', {}), calendar)

    def _make_calendar(self, request):
        course = Course.objects.filter(
            pk=request.POST.get('course', ''),
            student=self.student,
        )
        if not course.exists():
            # you can only create a calendar for a course you're enrolled in
            return self.send_ajax_error_message('You are not enrolled in that class', status=403)
        else:
            # course found
            course = course[0]

        end_date = timezone.make_aware(datetime.strptime(
            request.POST.get('enddate', ''), "%m/%d/%Y"),
            timezone.utc)
        calendar_data = {
            'course': course,
            'owner': self.student,
            'description': request.POST.get('description', ''),
            'end_date': end_date,
            'private': request.POST.get('private', True),
            'color': request.POST.get('color', '#FFFFFF'),
            'price': request.POST.get('price', 100),
        }
        return ClassCalendar(**calendar_data)
    
    def _make_sections(self, times, calendar):
        times = json.loads(times)
        for day in times:
            start_time = timezone.make_aware(datetime.strptime(
                times[day]['start'], DATE_FORMAT),
                timezone.get_current_timezone())
            start_time = timezone.localtime(start_time, timezone=timezone.utc)
            end_time = timezone.make_aware(datetime.strptime(
                times[day]['end'], DATE_FORMAT),
                timezone.get_current_timezone())
            end_time = timezone.localtime(end_time, timezone=timezone.utc)
            section_data = {
                'course': calendar.course,
                'student': self.student,

                'day': WEEK_DAYS.index(day),
                'start_time': start_time,
                'end_time': end_time,
            }
            section = Section(**section_data)
            # TODO error handling
            section.save()
        data = {
            'calendar': calendar.pk,
        }
        return self.render_to_json_response(data, status=200)

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(CalendarCreateView, self).dispatch(*args, **kwargs)

calendar_create = CalendarCreateView.as_view()

'''
url: /calendar/delete/
name: calendar_delete
'''
class CalendarDeleteView(DeleteView, AjaxableResponseMixin):
    model = ClassCalendar

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            cal = ClassCalendar.objects.filter(
                owner=self.student,
                pk = request.POST.get('id', None)
            )
            if cal.exists(): 
                cal = cal[0]
                cal.delete()
                # also delete the section that got made w/ this calendar
                Section.objects.filter(
                    student=self.student,
                    course=cal.course,
                ).delete()
                # clear out any subscriptions and let people know
                subs = Subscription.objects.filter(
                    calendar=cal
                )
                subscribers = list(map(lambda sub: sub.student.user, subs))
                stored_messages.api.add_message_for(
                    subscribers,
                    stored_messages.STORED_INFO,
                    '{} has deleted a calendar for {}'.format(request.user.username, cal.course)
                )
                subs.delete()

                messages.success(
                    self.request,
                    "Calendar deleted"
                )
                status = 200
            else:
                messages.error(
                    self.request,
                    "Is that really your calendar?"
                )
                status = 403
            data = {
                'messages': self.ajax_messages(),
            }
            return self.render_to_json_response(data, status=status)
        else:
            return redirect(reverse('calendar'))

    def get(self, request, *args, **kwargs):
        return redirect(reverse('calendar'))

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(CalendarDeleteView, self).dispatch(*args, **kwargs)

calendar_delete = CalendarDeleteView.as_view()

'''
url: /calendar/unsubscribe/
name: calendar_unsubscribe
'''
class CalendarUnsubscribeView(View, AjaxableResponseMixin):
    model = Subscription

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            sub = Subscription.objects.filter(
                student=self.student,
                calendar = request.POST.get('pk', None)
            )
            if sub.exists(): 
                sub = sub[0]
                sub.delete()
                messages.success(
                    self.request,
                    "Like sands of the hourglass, so is your subscription to that calendar."
                )
                status = 200
            else:
                messages.error(
                    self.request,
                    "You don't have a subscription to that calendar; neither does it have a subscription to you"
                )
                status = 403
            data = {
                'messages': self.ajax_messages(),
            }
            return self.render_to_json_response(data, status=status)
        else:
            return redirect(reverse('calendar'))

    def get(self, request, *args, **kwargs):
        return redirect(reverse('calendar'))

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(CalendarUnsubscribeView, self).dispatch(*args, **kwargs)

calendar_unsubscribe = CalendarUnsubscribeView.as_view()

'''
url: /calendar/events/add/
name: event_add
'''
class EventAddView(View, AjaxableResponseMixin):
    template_name = 'calendar_mchp/event_add.html'
    model = CalendarEvent

    def post(self, request, *args, **kwargs):
        calendar = ClassCalendar.objects.filter(
            pk=request.POST.get('calendar', ''),
            owner=self.student
        )
        if not calendar.exists():
            return
        else:
            calendar = calendar[0]

        events = request.POST.get('events', '[]')
        events = json.loads(events)
        error = False
        for index in events:
            event = events[index]
            all_day = False
            date = event['date']

            # most things don't let you submit a time yet
            if event['hasTime']:
                start = datetime.strptime(date, DATE_FORMAT)
                start = timezone.make_aware(start, timezone.utc)
                end = start + timedelta(hours=1)
            else:
                date = datetime.strptime(date, DATE_FORMAT)
                start, end = self._get_class_time(calendar, date)

            # add the event
            event_data = {
                'calendar': calendar,
                'title': event['title'],
                'description': event['description'],
                'start': start,
                'end': end,
                'all_day': all_day,
                'last_edit': timezone.now(),
            }
            cal_event = CalendarEvent(**event_data)
            try:
                cal_event.save()
            except ( CalendarExpiredError, BringingUpThePastError ) as e:
                messages.error(
                    self.request,
                    str(e)
                )
                error = True
        if not error:
            messages.success(
                self.request,
                "Your events have been updated"
            )
            # send a notification to everyone that an event has been added
            subscribers = list(map(lambda sub: sub.student.user, Subscription.objects.filter(
                calendar=calendar
            )))
            stored_messages.api.add_message_for(
                subscribers,
                stored_messages.STORED_INFO,
                '{} has add an event to {}'.format(request.user.username, calendar.course)
            )

        if self.request.is_ajax():
            data = {
                'messages': self.ajax_messages(),
            }
            return self.render_to_json_response(data, status=200)
        else:
            return redirect(reverse('calendar'))

    def _get_class_time(self, calendar, date):
        section = Section.objects.filter(
            course=calendar.course,
            day = date.weekday()
        )
        if section.exists():
            section = section[0]
            start = datetime.combine(date, section.start_time)
            start = timezone.make_aware(
                start,
                timezone.utc
            )
            end = datetime.combine(start, section.end_time)
            end = timezone.make_aware(
                end,
                timezone.utc
            )
        else:
            start_time = timezone.make_aware(date, timezone.get_current_timezone())
            start = timezone.localtime(start_time, timezone=timezone.utc)
            print(start)
            end = start + timedelta(hours=1)
        return (start, end)

    def get(self, request, *args, **kwargs):
        calendars = ClassCalendar.objects.filter(
            owner = self.student
        )
        for calendar in calendars:
            sections = Section.objects.filter(
                course=calendar.course,
                student=self.student,
            )
            calendar.end_date = timezone.make_naive(calendar.end_date, timezone.utc)
            for section in sections:
                day_name = WEEK_DAYS[section.day]
                start_date = datetime.combine(datetime.today(), section.start_time)
                end_date = datetime.combine(datetime.today(), section.end_time)

                start_time = timezone.make_aware(start_date, timezone.utc)
                end_time = timezone.make_aware(end_date, timezone.utc)
                start_time = timezone.localtime(start_time, timezone=timezone.get_current_timezone())
                end_time = timezone.localtime(end_time, timezone=timezone.get_current_timezone())
                section.day_name = day_name
                section.start = start_time
                section.end = end_time

            setattr(calendar, 'sections', sections)
        selected_calendar = request.GET.get('calendar', '')
        data = {
            'calendars': calendars,
            'selected_calendar': selected_calendar,
        }
        return render(request, self.template_name, data)

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(EventAddView, self).dispatch(*args, **kwargs)

event_add = EventAddView.as_view()

'''
url: /calendar/events/update/
name: event_update
'''
class EventUpdateView(UpdateView, AjaxableResponseMixin):
    model = CalendarEvent

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            print(request.POST)
            event = CalendarEvent.objects.filter(
                calendar__owner=self.student,
                id = request.POST.get('pk', None)
            )
            if event.exists():
                event = event[0]

                date = request.POST.get('date', None)
                if date:
                    start = timezone.make_aware(datetime.strptime(
                        json.loads(date), DATE_FORMAT),
                        timezone.get_current_timezone())
                    start = timezone.localtime(start, timezone=timezone.utc)
                    print(start)
                    end = start + timedelta(hours=1)
                    setattr(event, 'start', start)
                    setattr(event, 'end', end)

                update = request.POST.get('name', '')
                if update == 'title':
                    description = request.POST.get('value', '')
                    setattr(event, 'title', description)

                if update == 'description':
                    description = request.POST.get('value', '')
                    setattr(event, 'description', description)
                if update == 'class':
                    print(request.POST.get('value', 'fuck'))
                    calendar = ClassCalendar.objects.filter(
                        owner = self.student,
                        course__pk = request.POST.get('value', -1)
                    )
                    if calendar.exists():
                        calendar = calendar[0]
                        event.calendar = calendar
                    else:
                        response = "We couldn't find a calendar for that class"
                        status=403
                        data = {
                            'response': response,
                        }
                        return self.render_to_json_response(data, status=status)
                try:
                    event.save()
                    response = "Event updated"
                    status=200
                    # send a notification to everyone that this calendar event has been updated
                    subscribers = list(map(lambda sub: sub.student.user, Subscription.objects.filter(
                        calendar=event.calendar
                    )))
                    stored_messages.api.add_message_for(
                        subscribers,
                        stored_messages.STORED_INFO,
                        '{} has updated event: {} in {}'.format(request.user.username, event.title, event.calendar.course)
                    )
                except (CalendarExpiredError, BringingUpThePastError) as e:
                    status=403
                    data = {
                        'response': str(e),
                    }
                    return self.render_to_json_response(data, status=status)
            else:
                response = "Event not found"
                status=403
            data = {
                'response': response,
            }
            return self.render_to_json_response(data, status=status)
        else:
            return redirect(reverse('calendar'))

    def get(self, request, *args, **kwargs):
        return redirect(reverse('calendar'))

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(EventUpdateView, self).dispatch(*args, **kwargs)

event_update = EventUpdateView.as_view()

'''
url: /calendar/events/delete/
name: event_delete
'''
class EventDeleteView(DeleteView, AjaxableResponseMixin):
    model = CalendarEvent

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            event = CalendarEvent.objects.filter(
                calendar__owner=self.student,
                id = request.POST.get('pk', None)
            )
            if event.exists():
                event = event[0]
                event.delete()

                messages.success(
                    self.request,
                    "Event deleted"
                )
            else:
                messages.error(
                    self.request,
                    "Event not found"
                )
            data = {
                'messages': self.ajax_messages(),
            }
            return self.render_to_json_response(data, status=200)
        else:
            return redirect(reverse('calendar'))

    def get(self, request, *args, **kwargs):
        return redirect(reverse('calendar'))

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(EventDeleteView, self).dispatch(*args, **kwargs)

event_delete = EventDeleteView.as_view()

'''
url: /calendar/preview/<pk>
name: calendar_preview
'''
class CalendarPreview(DetailView):
    template_name = 'calendar_mchp/calendar_preview.html'
    model = ClassCalendar

    def post(self,request, *args, **kwargs):
        if not self.student:
            return redirect(reverse('landing_page'))
        calendar = get_object_or_404(self.model, pk=self.kwargs['pk'], private=False)

        if calendar.owner == self.student:
            messages.error(
                request,
                "Woah there Narcissus, you can't subscribe to your own calendar"
            )
            return self.get(request, *args, **kwargs)

        subscription, created = Subscription.objects.get_or_create(
            student=self.student,
            calendar=calendar,
        )
        if not created:
            if subscription.enabled:
                messages.warning(
                    request,
                    "Slow down there Eager McBeaver, you're already subscribed to that calendar"
                )
            else:
                if not self.student.reduce_points(calendar.price):
                    messages.error(
                        request,
                        "Well that didn't do much good, try buying some points first"
                    )
                    return self.get(request, *args, **kwargs)
                else:
                    # renew subscription
                    points = calendar.price * (settings.MCHP_PRICING['commission_rate'] / 100)
                    points = points / 100
                    points = Decimal(points).quantize(Decimal('1.0000'), rounding=ROUND_HALF_DOWN)
                    calendar.owner.modify_balance(points)
                    calendar.owner.save()

                    subscription.enabled=True
                    subscription.save()
                    messages.success(
                        request,
                        "Your subscription has gone through Carrousel and been renewed"
                    )
        else:
            if not self.student.reduce_points(calendar.price):
                messages.error(
                    request,
                    "Pump your break kid, you don't have enough points to buy that."
                )
                subscription.delete()
                return self.get(request, *args, **kwargs)
            subscription.price = calendar.price
            subscription.save()
            points = calendar.price * (settings.MCHP_PRICING['commission_rate'] / 100)
            points = points / 100
            points = Decimal(points).quantize(Decimal('1.0000'), rounding=ROUND_HALF_DOWN)
            calendar.owner.modify_balance(points)
            calendar.owner.save()
            messages.success(
                request,
                "Your subscription has been noted"
            )
            stored_messages.api.add_message_for(
                [calendar.owner.user], 
                stored_messages.STORED_INFO,
                '{} has subscribed to your {} calendar'.format(request.user.username, calendar.course)
            )
        return redirect(reverse('calendar'))

    def get(self, request, *args, **kwargs):
        referral_link = ''
        if not request.user.is_anonymous() and request.user.student_exists():
            referral_link = ReferralCode.objects.get_referral_code(request.user).referral_link

        calendar = get_object_or_404(self.model, pk=self.kwargs['pk'], private=False)
        # this is going to recalculate its accuracy 
        calendar.save()

        events = CalendarEvent.objects.filter(
            calendar=calendar,
            start__lt=timezone.now(),
        ).order_by('start')[:3]
        count = CalendarEvent.objects.filter(
            calendar=calendar,
            start__lte=timezone.now()
        ).count()
        next_event = CalendarEvent.objects.filter(
            calendar=calendar,
            start__gte=timezone.now()
        ).order_by('start')[:1]
        if next_event.exists():
            next_event = next_event[0]
        else:
            next_event = None
        total_count = CalendarEvent.objects.filter(
            calendar=calendar
        ).count()

        # class meeting times
        sections = Section.objects.filter(
            course=calendar.course,
            student=self.student,
        )
        for section in sections:
            day_name = WEEK_DAYS[section.day]
            start_date = datetime.combine(datetime.today(), section.start_time)
            end_date = datetime.combine(datetime.today(), section.end_time)

            start_time = timezone.make_aware(start_date, timezone.utc)
            end_time = timezone.make_aware(end_date, timezone.utc)
            start_time = timezone.localtime(start_time, timezone=timezone.get_current_timezone())
            end_time = timezone.localtime(end_time, timezone=timezone.get_current_timezone())
            section.day_name = day_name
            section.start = start_time
            section.end = end_time
        setattr(calendar, 'sections', sections)

        data = {
            'calendar': calendar,
            'owner': calendar.owner,
            'owner_level': round((timezone.now() - calendar.owner.user.date_joined) / timedelta(days=7)),
            'events': events,
            'past_count': count,
            'next_event': next_event,
            'total_count': total_count,
            'referral_link': referral_link,
            'current_path': request.get_full_path(),
        }
        return render(request, self.template_name, data)
    
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_anonymous() and self.request.user.student_exists():
            self.student = self.request.user.student
        else:
            self.student = None
        return super(CalendarPreview, self).dispatch(*args, **kwargs)

calendar_preview = CalendarPreview.as_view()

'''
url: /calendar/
name: calendar
'''
class CalendarView(View):
    template_name = 'calendar_mchp/calendar.html'

    def get(self, request, *args, **kwargs):
        owned_calendars = ClassCalendar.objects.filter(
            owner=self.student
        ).order_by(
            'private', 'title'
        ).annotate(
            subscriptions=Count('subscribers')
        )
        cal_courses = ClassCalendar.objects.filter(
            owner = self.student,
        ).values('course__pk', 'course__dept', 'course__course_number')
        courses = self.student.courses.all()
        subscriptions = ClassCalendar.objects.filter(
            subscription__student=self.student,
            subscription__enabled=True,
            subscription__accuracy__gte=-1,
        ).order_by('title')
        subscription_info = Subscription.objects.filter(
            student=self.student,
            enabled=True,
        ).values('pk', 'accuracy', 'payment_date', 'subscribe_date', 'price', 'enabled', 'calendar')
        for subscription in subscriptions:
            for info in subscription_info:
                print(info)
                if info['calendar'] == subscription.pk:
                    payment_date = timezone.localtime(info['payment_date'], timezone=timezone.get_current_timezone())
                    subscribe_date = timezone.localtime(info['subscribe_date'], timezone=timezone.get_current_timezone())
                    print(payment_date)
                    setattr(subscription, 'rating', info['accuracy'])
                    setattr(subscription, 'payment_date', payment_date)
                    setattr(subscription, 'subscribe_date', subscribe_date)
                    setattr(subscription, 'price', info['price'])
                    setattr(subscription, 'enabled', info['enabled'])

        delinquent_subscriptions = ClassCalendar.objects.filter(
            subscription__student=self.student,
            subscription__enabled=False,
        ).order_by('title')
        for calendar in delinquent_subscriptions:
            missed_events = CalendarEvent.objects.filter(
                calendar=calendar,
                start__gte=timezone.now(),
            ).count()
            setattr(calendar, 'missed_events', missed_events)
        data = {
            'flags': self.student.one_time_flag.default(self.student),
            'calendar_courses': cal_courses,
            'courses': courses,
            'owned_calendars': owned_calendars,
            'subscriptions': subscriptions,
            'delinquent_subscriptions': delinquent_subscriptions,
        }
        return render(request, self.template_name, data)

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(CalendarView, self).dispatch(*args, **kwargs)

calendar = CalendarView.as_view()

'''
url: /calendar/update/
name: calendar_update
'''
class CalendarUpdateView(View, AjaxableResponseMixin):
    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            calendar = ClassCalendar.objects.filter(
                owner=self.student,
                id = request.POST.get('pk', None)
            )
            if calendar.exists():
                calendar = calendar[0]

                date = request.POST.get('date', None)
                if date:
                    end_date = timezone.make_aware(datetime.strptime(
                        json.loads(date), DATE_FORMAT),
                        timezone.get_current_timezone())
                    end_date = timezone.localtime(end_date, timezone=timezone.utc)
                    setattr(calendar, 'end_date', end_date)

                update = request.POST.get('name', '')
                if update == 'description':
                    description = request.POST.get('value', '')
                    setattr(calendar, 'description', description)

                changed_privacy = False
                if update == 'private':
                    private = int(request.POST.get('value', 1))
                    if private  == 1:
                        setattr(calendar, 'private', False)
                    elif private == 2:
                        setattr(calendar, 'private', True)
                    changed_privacy = True

                if update == 'price':
                    price = request.POST.get('value', 0)
                    try:
                        price = int(price)
                        setattr(calendar, 'price', price)
                    except:
                        response = "That's not a price that you can sell something for"
                        status=400
                        data = {
                            'response': response,
                        }
                        return self.render_to_json_response(data, status=status)

                calendar.save()
                response = "Calendar updated"
                status=200
            else:
                response = "We couldn't find that calendar"
                status=403
            data = {
                'response': response,
                'privacy': changed_privacy,
            }
            return self.render_to_json_response(data, status=status)
        else:
            return redirect(reverse('calendar'))

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(CalendarUpdateView, self).dispatch(*args, **kwargs)

calendar_update = CalendarUpdateView.as_view()

'''
url: /calendar/subscription/update
name: subscription_update
'''
class SubscriptionUpdateView(View, AjaxableResponseMixin):
    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            subscription = Subscription.objects.filter(
                student=self.student,
                calendar = request.POST.get('calendar', None)
            )
            if subscription.exists():
                subscription = subscription[0]
                rating = int(request.POST.get('rating', None))
                print(rating)
                if rating != None:
                    subscription.accuracy = rating
                    subscription.save()
                    # update aggragate calendar accuracy
                    subscription.calendar.save()
                response = "Accuracy updated"
                status=200
            else:
                response = "You are not subscribed to that calendar"
                status=403
            data = {
                'response': response,
            }
            return self.render_to_json_response(data, status=status)
        else:
            return redirect(reverse('calendar'))

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(SubscriptionUpdateView, self).dispatch(*args, **kwargs)

subscription_update = SubscriptionUpdateView.as_view()

'''
url: /calendar/feed/
name: calendar_feed
'''
class CalendarFeed(View, AjaxableResponseMixin):

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['GET'])

    def get(self, request, *args, **kwargs):
        if self.request.is_ajax():
            # get the ranges that full calendar sends in the request
            start = request.GET.get('start', '')
            start = timezone.make_aware(datetime.strptime(
                start, "%Y-%m-%d"),
                timezone.utc
            )
            end = request.GET.get('end', '')
            end = timezone.make_aware(datetime.strptime(
                end, "%Y-%m-%d"),
                timezone.utc
            )
            # event data
            events = CalendarEvent.objects.filter(
                calendar__owner=self.student,
                calendar__end_date__gte=timezone.now(),
                is_recurring=False,
                start__range=(start,end)
            ).values('id', 'title', 'description', 'start', 'end', 'all_day', 'url',
                     'calendar__course__name', 'calendar__color', 'calendar__course__pk',
                     'calendar__pk', 'calendar__private', 'last_edit'
            )

            subscribed_events = Subscription.objects.filter(
                student=self.student,
                enabled=True,
                calendar__private=False,
                calendar__calendarevent__start__range=(start,end)
            ).values(
                'calendar__calendarevent__title',
                'calendar__calendarevent__description',
                'calendar__calendarevent__start',
                'calendar__calendarevent__end',
                'calendar__calendarevent__id',
                'calendar__calendarevent__last_edit',
                'calendar__color',
                'calendar__pk',
                'calendar__private',
                'calendar__course__pk',
                'calendar__course__name',
            )
            for event in subscribed_events:
                start_time = timezone.localtime(event['calendar__calendarevent__start'], timezone=timezone.get_current_timezone())
                end_time = timezone.localtime(event['calendar__calendarevent__end'], timezone=timezone.get_current_timezone())
                last_edit = timezone.localtime(event['calendar__calendarevent__last_edit'], timezone=timezone.utc)

                event['start'] = start_time.strftime(DATE_FORMAT)
                event['end'] = end_time.strftime(DATE_FORMAT)
                event['last_edit'] = last_edit.strftime(DATE_FORMAT)

                event['course'] = event['calendar__course__name']
                event['id'] = event['calendar__calendarevent__id']
                event['title'] = event['calendar__calendarevent__title']
                event['description'] = event['calendar__calendarevent__description']
                event['owned'] = False

                del event['calendar__calendarevent__start']
                del event['calendar__calendarevent__end']
                del event['calendar__calendarevent__title']
                del event['calendar__calendarevent__description']
                del event['calendar__calendarevent__id']
                del event['calendar__calendarevent__last_edit']

            # convert the returned events to a format we can use on the page
            for event in events:
                start_time = timezone.localtime(event['start'], timezone=timezone.get_current_timezone())
                end_time = timezone.localtime(event['end'], timezone=timezone.get_current_timezone())
                last_edit = timezone.localtime(event['last_edit'], timezone=timezone.utc)

                event['last_edit'] = last_edit.strftime(DATE_FORMAT)
                event['start'] = start_time.strftime(DATE_FORMAT)
                event['end'] = end_time.strftime(DATE_FORMAT)
                event['allDay'] = event['all_day']
                event['course'] = event['calendar__course__name']
                event['owned'] = True

                del event['calendar__course__name']
                del event['all_day']

            both = sorted(list(events) + list(subscribed_events), key=lambda x: x['start'])
            data = {
                'events': both,
            }
            return self.render_to_json_response(data, status=200)
        else:
            return redirect(reverse('calendar'))

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(CalendarFeed, self).dispatch(*args, **kwargs)

calendar_feed = CalendarFeed.as_view()

'''
url: /calendar/list/
name: calendar_list
'''
class CalendarListView(View, AjaxableResponseMixin):

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['GET'])

    def get(self, request, *args, **kwargs):
        if self.request.is_ajax():
            course = request.GET.get('course', -1)
            calendars = ClassCalendar.objects.filter(
                course=course,
                private=False,
                end_date__gte=timezone.now(),
            ).annotate(
                events=Count('calendarevent__pk'),
            ).order_by(
                'create_date', 'title'
            ).values('title', 'price', 'owner', 'events', 'owner__user__username','pk',
                     'description', 'create_date', 'course__professor')
            for calendar in calendars:
                date = timezone.localtime(calendar['create_date'], timezone=timezone.utc)
                calendar['date'] = date.strftime(DATE_FORMAT)
                calendar_instance = ClassCalendar.objects.get(pk=calendar['pk'])
                # reset accuracy
                calendar_instance.save()
                calendar['subscriptions'] = calendar_instance.subscribers.count()
                calendar['accuracy'] = calendar_instance.accuracy
                sections = Section.objects.filter(
                    course=calendar_instance.course,
                    student__pk=calendar['owner'],
                )
                time_string = ''
                for section in sections:
                    day_name = WEEK_DAYS[section.day]
                    start_date = datetime.combine(datetime.today(), section.start_time)
                    end_date = datetime.combine(datetime.today(), section.end_time)

                    start_time = timezone.make_aware(start_date, timezone.utc)
                    end_time = timezone.make_aware(end_date, timezone.utc)
                    start_time = timezone.localtime(start_time, timezone=timezone.get_current_timezone())
                    end_time = timezone.localtime(end_time, timezone=timezone.get_current_timezone())
                    time_string += day_name[:3] + ' '
                    time_string += start_time.strftime('%I%p').lstrip('0') + '-'
                    time_string += end_time.strftime('%I%p').lstrip('0') + '&nbsp;&nbsp;&nbsp;&nbsp;'
                calendar['time'] = time_string
                del calendar['create_date']

            print(calendars)
            data = {
                'calendars': list(calendars),
            }
            return self.render_to_json_response(data, status=200)
        else:
            return redirect(reverse('calendar'))

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(CalendarListView, self).dispatch(*args, **kwargs)

calendar_list = CalendarListView.as_view()
