from django.forms import ModelForm
from django import forms
from .models import UserInfo


class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name', 'phone_number', 'desired_sub','notes']

    def clean(self):
        super(UserInfoForm, self).clean()

        name = self.cleaned_data.get('name')
        number = self.cleaned_data.get('phone_number')
        desired_sub = self.cleaned_data.get('desired_sub')
        notes = self.cleaned_data.get('notes')

        # if len(name) < 3:
        #     self.errors['name'] = self.error_class([
        #         'Minimum 3 character required for name.'
        #     ])
        # if len(str(number)) < 10 or len(str(number)) > 13:
        #     self.errors['phone_number'] = self.error_class([
        #         'Number should contain between 10 and 13 numbers'
        #     ])

        return self.cleaned_data
