from rest_framework import generics
from first_ap.api.models import First_ASerializer
from first_ap.models import First_A

class First_AListAPIView(generics.ListAPIView):
	lookup ='pk'
	serializer_class = First_ASerializer
	queryset = First_A.objects.all()

class First_ARetrieveAPIView(generics.RetrieveAPIView):
	queryset = First_A.objects.all()
	serializer_class = First_ASerializer
	lookup_field = "slug"



