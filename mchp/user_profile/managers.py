from django.db import models
from django.conf import settings

from notification.api import add_notification
import user_profile.models
import dashboard.models

class StudentManager(models.Manager):
    # get or create the referral codes for a user
    def create_student(self, user, school):
        student = user_profile.models.Student(
            user=user, school=school,
        )
        student.save()
        profile = user_profile.models.UserProfile(student=student)
        profile.save()
        roles = user_profile.models.UserRole(user=user)
        roles.save()

        # set default rss settings
        dashboard.models.RSSSetting.objects.restore_default_settings(student)
        return student

    def referral_reward(self, user, referrer):
        reward_points = settings.MCHP_PRICING['referral_reward']
        user.student.add_earned_points(reward_points)
        referrer_roles = user_profile.models.UserRole.objects.get_roles(referrer)
        if referrer_roles.rep:
            referrer.student.modify_balance(1)
            add_notification(
                referrer,
                user.username + " used your code. You've got money in the bank",
            )
        else:
            referrer.student.add_earned_points(reward_points)
            add_notification(
                referrer,
                user.username + " used your code. You made a cool {} points".format(reward_points),
            )

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
    @staticmethod
    def get_event(name):
        if not name:
            return None

        return user_profile.models.OneTimeEvent.objects.get_or_create(
            name=name
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
    def get_flag(student, event_name):
        # usually this mean the user is not logged in, so don't show any of these
        if not student:
            return (True,)

        event = user_profile.models.OneTimeEvent.objects.filter(
            name=event_name
        )

        flag = user_profile.models.OneTimeFlag.objects.filter(
            student=student,
            event=event,
        )
        return flag.exists()
