from django.db import models

import user_profile.models
import dashboard.models

class StudentManager(models.Manager):
    # get or create the referral codes for a user
    def create_student(self, user, school):
        student = user_profile.models.Student(
            user=user, school=school
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

class OneTimeFlagManager(models.Manager):
    def default(self, student):
        flags, created = user_profile.models.OneTimeFlag.objects.get_or_create(
            student=student
        )
        return flags
