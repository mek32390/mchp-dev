from django.db import models

import payment.models

class StripeCustomerManager(models.Manager):
    def set_default_card(self, user, default_card):
        all_cards = payment.models.StripeCustomer.objects.filter(
            user = user,
        )
        if not all_cards:
            return None
        ret_card = None
        for card in all_cards:
            card.default = False
            if card == default_card:
                ret_card = card
                card.default = True
            card.save()
        return ret_card
