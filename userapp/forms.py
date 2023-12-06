from django import forms
from userapp.models import Employee


class UserForm(forms.Form):
    uid = forms.IntegerField()
    uname = forms.CharField()
    uloc = forms.CharField()
    uemail = forms.CharField()


class EmployeeForm(forms.ModelForm):
    class Meta:

        model = Employee
        #fields = "__all__"
        fields = ['eid', 'ename', 'esal']
        