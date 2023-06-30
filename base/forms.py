from django import forms
from .models import PetReservation

class PetReservationForm(forms.ModelForm):
    class Meta:
        model = PetReservation
        fields = ['pet_name', 'phone', 'reservation_day', 'observations']
        widgets = {
            'observations': forms.Textarea(attrs={'rows': 4}),
        }
