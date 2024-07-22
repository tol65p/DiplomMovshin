from django import forms
from django.core.exceptions import ValidationError
from . models import Users, Runners, Protokols, Events
from datetime import date as dt
class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['nickname', 'password', 'email']
    pass_control = forms.CharField(max_length=20, help_text='Пароль повторно')

    def clean(self):
        form_data = self.cleaned_data
        if form_data['password'] != form_data['pass_control']:
            self._errors['password'] = ['Пароли не совпадают!']
        return form_data

    def clean_email(self):
        mail = self.cleaned_data['email']
        if Users.objects.filter(email=mail).exists():
            raise ValidationError("такой мэйл вже є !")
        return mail

    def clean_nickname(self):
        username = self.cleaned_data['nickname']
        if Users.objects.filter(nickname=username).exists():
            raise ValidationError("такой Ник вже є !")
        return username

class EntryForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['nickname', 'password']

    def clean(self):
        form_data = self.cleaned_data
        rec = Users.objects.filter(nickname=form_data['nickname'])
        if rec.exists():
            if rec[0].password != form_data['password']:
                raise ValidationError("пароль не соответствует НИК'у !")
        else:
            raise ValidationError("Такого НИК не зарегистрировано !")
        return form_data

class RunnerForm(forms.ModelForm):
    class Meta:
        model = Runners
        fields = ['fam', 'name', 'gender', 'birthday', 'city', 'tel', 'sportTeam', 'identKod']

class ProtokolForm(forms.ModelForm):
    #spisEvent = Events.objects.filter(date__gt=dt.today())
    #event = forms.ChoiceField(choices=spisEvent)
    class Meta:
        model = Protokols
        fields = ['event', 'discount', 'oplata']

