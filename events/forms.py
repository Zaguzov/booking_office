from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from events.models import ShoppingCart


class BuyingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.ticket = kwargs.pop('ticket', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = ShoppingCart
        fields = ('number_of_purchased_tickets',)
        labels = {'number_of_purchased_tickets': _('Кол-во билетов')}

    def clean(self):
        data = self.cleaned_data
        if data['number_of_purchased_tickets'] > self.ticket.number_of_available_tickets:
            raise ValidationError(
                _('Кол-во покупаемых билетов не может '
                  'быть больше кол-ва доступных'),
                code='invalid',
            )
        return data


