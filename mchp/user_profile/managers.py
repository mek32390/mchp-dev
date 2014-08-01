from django.db import models

import user_profile.models

class StudentManager(models.Manager):
    # get or create the referral codes for a user
    def create_student(self, user, school):
        student = user_profile.models.Student(
            user=user, school=school
        )
        student.save()
        profile = user_profile.models.UserProfile(student=student)
        profile.save()
        # also make user roles here
        return student

    def referral_reward(self, user, referrer):
        user.student.add_earned_points(500)
        referrer.student.modify_balance(1)
