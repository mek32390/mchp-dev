def referral_reward(user, referrer):
    user.student.add_earned_points(500)
    referrer.student.modify_balance(1)
