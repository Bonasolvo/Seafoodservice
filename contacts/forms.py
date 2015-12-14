from django import forms
from captcha.fields import CaptchaField
from django.utils.translation import ugettext_lazy as _

from models import Message


class LeaveMessageForm(forms.ModelForm):
    captcha = CaptchaField(label=_("Letters from picture"),
                           output_format='%(text_field)s %(image)s %(hidden_field)s')

    class Meta:
        model = Message
    prefix = "leave_message"

