from django import forms
from django.forms import fields, widgets
from . import models

class ReivewInput(forms.ModelForm):
    
    number=forms.IntegerField(min_value=1, max_value=5,label="rating", 
                              widget=forms.NumberInput(attrs={'style': 'border: 1px solid;'}))
    
    
    class Meta:
        model=models.Review
        fields=("text",)
        widgets={
            'text':forms.TextInput( attrs={
                'placeholder':'Leave a review',
                'style': 'border: 1px solid; ',
                }),
        }
        
    def clean_number(self):
        return self.cleaned_data.get("number")
    
    
        
    def save(self):
        review= super().save(commit=False)
        review.rating=self.cleaned_data.get("number")
        
        return review
        