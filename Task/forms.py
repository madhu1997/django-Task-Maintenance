from django import forms
from Task.models import Trainee,sessionDetails,evaluation
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class TraineeForm(forms.ModelForm):  
    class Meta:  
        model = Trainee 
        fields = ('Full_Name','Age','Qualification','profile_pic') 

class TaskForm(forms.ModelForm):
    #tid = forms.CharField(widget = forms.HiddenInput(),initial= User)
    Date = forms.DateField()
    class Meta:
        model = sessionDetails
        fields = ('Date','session1','session2','session3','session4','description')
class evaluateForm(forms.ModelForm):  
    class Meta:  
        model = evaluation  
        fields = "__all__"
