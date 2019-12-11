from django.urls import path, re_path
from first_ap.api import views

app_name = 'api_first_ap'

urlpatterns = [
	path('list/', views.First_AListAPIView.as_view(),name = 'api_first_a_list'),
	# path('detail/<int:pk>', views.First_ARetrieveAPIView.as_view(), name='api_first_a_detail'),
	re_path(r'^detail/(?P<slug>[-\w]+)/', views.First_ARetrieveAPIView.as_view()),
]