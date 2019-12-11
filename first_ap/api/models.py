from rest_framework import serializers
from first_ap.models import First_A

class First_ASerializer(serializers.ModelSerializer):
	class Meta():
		model = First_A
		fields = ['name', 'age']