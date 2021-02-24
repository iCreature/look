from django import forms
from .models import submitted

class BookForm(forms.ModelForm):
    class Meta:
        model= submitted
        fields =('paper','student_no')
