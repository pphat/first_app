from django_project import views, settings
from django.contrib import admin
from django.urls import path, include, re_path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.IndexTemplateView.as_view(), name='index'),
	
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name = 'user_login'),
	path('logout/', auth_views.LogoutView.as_view(), name = 'user_logout'),
	
	path('change-password/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('user_logout')), name='password_change'),
	path('change-password-done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
	
	path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z](1, 13)-[0-9A-Za-z](1, 20))/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
	path('first_ap/',include('first_ap.urls', namespace = 'first_ap')),
	path('api/first_ap/',include('first_ap.api.urls',namespace='api_first_ap')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#updated DO NOT REMOVE THIS LINE