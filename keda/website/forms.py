from django.forms import ModelForm
from django import forms
from website.models import *
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class SubscriptionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
    class Meta:
        model = Subscription
        fields = "__all__"

        widgets = {
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'example@email.com'}),
        }

class ConsultForm(ModelForm):
    class Meta:
        model = Consult
        fields = "__all__"
        labels = {
            'name': ('Nama'),
            'business_sector': ('Sektor Usaha Anda'),
            'phone_number': ('Nomor HP'),
            'question': ('Pertanyaan Anda'),
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','id':'name', 'placeholder':'John Doe'}),
            'business_sector' : forms.TextInput(attrs={'class':'form-control','id':'business_sector','placeholder':'Digital Marketing'}),
            'phone_number': PhoneNumberPrefixWidget(initial="ID",attrs={'class':'form-control','id':'phone_number', 'placeholder':'82388400299'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'example@email.com'}),
            'question' : forms.Textarea(attrs={'class':'form-control'})
        }

class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = "__all__"
        labels = {
            'candidate_name': ('Nama'),
            'career_tag_id' : ('Posisi yang dilamar'),
            'whatsapp_number': ('Whatsapp Number'),
            'email': ('Email'),
            'cv': ('CV')
        }
        widgets = {
            'candidate_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'John Doe'}),
            'career_tag_id' : forms.Select(attrs={"class":'form-control'}),
            'whatsapp_number' : PhoneNumberPrefixWidget(initial="ID",attrs={'class':'form-control','id':'phone_number', 'placeholder':'82388400299'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'example@email.com'}),
            'cv' : forms.FileInput(attrs={'class':'form-control','accept':'application/pdf'})
        }

