from django import forms as f
from django.utils.translation import gettext as _


class EmailTemplateForm(f.ModelForm):

    def clean(self):
        data = super(EmailTemplateForm, self).clean()
        print([data['subject'], data['html'], data['text']])
        if not any([data['subject'], data['html'], data['text']]):
            raise f.ValidationError(_("At least one of subject, html or text fields must be filled."))
