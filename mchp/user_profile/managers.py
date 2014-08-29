from django.db import models

import user_profile.models
from user_profile.utils import ONE_TIME_EVENTS_DICT
import dashboard.models
import schedule.models

class StudentManager(models.Manager):
    # get or create the referral codes for a user
    def create_student(self, user, school):
        student = user_profile.models.Student(
            user=user, school=school,
            major=schedule.models.Department.objects.get(name="Undecided")
        )
        student.save()
        profile = user_profile.models.UserProfile(student=student)
        profile.save()
        roles = user_profile.models.UserRole(user=user)
        roles.save()

        # set username for social users
        if user.first_name:
            user.username = user.first_name + user.last_name
            user.save()

        # set default rss settings
        dashboard.models.RSSSetting.objects.restore_default_settings(student)
        return student

    def referral_reward(self, user, referrer):
        user.student.add_earned_points(500)
        referrer_roles = user_profile.models.UserRole.objects.get_roles(referrer)
        if referrer_roles.rep:
            referrer.student.modify_balance(1)

class UserRoleManager(models.Manager):
    def get_roles(self, user):
        roles = user_profile.models.UserRole.objects.filter(user=user)
        if roles.exists():
            return roles[0]
        else:
            roles = user_profile.models.UserRole(user=user)
            roles.save()
            return roles

class OneTimeEventManager(models.Manager):
    def get_event(id):
        return user_profile.models.OneTimeEvent.objects.get_or_create(
            pk=id
        )[0]

class OneTimeFlagManager(models.Manager):
    @staticmethod
    def clear_flags(student):
        user_profile.models.OneTimeFlag.objects.filter(
            student=student
        ).delete()

    @staticmethod
    def set_flag(student, event):
        flag, created = user_profile.models.OneTimeFlag.objects.get_or_create(
            student=student,
            event=event,
        )
        return created

    @staticmethod
    def get_flags(student):
        return user_profile.models.OneTimeFlag.objects.filter(
            student=student
        )

    @staticmethod
    def get_flag(student, event):
        # usually this mean the user is not logged in, so don't show any of these
        if not student:
            return (True,)

        if event in ONE_TIME_EVENTS_DICT.keys():
            pk = ONE_TIME_EVENTS_DICT[event]
        else:
            return None
        event, created = user_profile.models.OneTimeEvent.objects.get_or_create(pk=pk, name=event)

        flag = user_profile.models.OneTimeFlag.objects.filter(
            student=student,
            event=event,
        )
        return (flag.exists(), event.pk)
