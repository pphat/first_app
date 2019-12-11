from django import forms
from first_ap.models import First_A
class First_AForm(forms.ModelForm):
	class Meta():
		model = First_A
		exclude = ['slug']