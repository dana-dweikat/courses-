from django import forms
from .models import Courses


class CoursesForms(forms.ModelForm):
    class Meta:
        model=Courses
        fields=['name','description']


    def __init__(self, *args, **kwargs):
        super(CoursesForms, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'


