from django.urls import path, re_path
from first_ap import views


app_name='first_ap'

urlpatterns=[
	path('',views.IndexTemplateView.as_view(), name = 'index'),
	path('my_page/',views.First_AMyPageView.as_view(), name = 'first_a_my_page'),
	path('list/',views.First_AListView.as_view(), name = 'first_a_list'),
	path('create/',views.First_ACreateView.as_view(), name = 'first_a_create'),
	re_path(r'^detail/(?P<slug>[-\w]+)/',views.First_ADetailView.as_view(), name = 'first_a_detail'),
	re_path(r'^update/(?P<slug>[-\w]+)/',views.First_AUpdateView.as_view(), name = 'first_a_update'),
	re_path(r'^delete/(?P<slug>[-\w]+)/',views.First_ADeleteView.as_view(), name = 'first_a_delete'),
]