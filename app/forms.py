from django import forms

def validate_for_a(data):
    if data.lower().startswith('a'):
        raise forms.ValidationError('started with a')

def validate_forl_len(data):
    if len(data)<5:
        raise forms.ValidationError('len is < 5')

class SchoolForm(forms.Form):
    Sname=forms.CharField()
    Sprincipal=forms.CharField()
    Slocation=forms.CharField()
    email=forms.EmailField()
    renteremail=forms.EmailField()

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['renteremail']
        if e!=re:
            raise forms.ValidationError('emails not matched')    