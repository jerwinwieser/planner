
from django.contrib import admin
from django.urls import path, include
from users import views as user_views

# add auth views for our login / logout pages
from django.contrib.auth import views as auth_views

# add for settings in debug mode
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('profile/', user_views.profile, name='profile'),
	path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('registrations.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)