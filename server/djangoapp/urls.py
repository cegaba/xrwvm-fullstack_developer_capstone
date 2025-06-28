# Uncomment the imports before you add the code
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'djangoapp'
urlpatterns = [
    # POST /djangoapp/register/ → registration endpoint
    path('register/', views.registration, name='registration'),

    # POST /djangoapp/login/    → login endpoint
    path('login/',    views.login_user,    name='login'),

    # GET  /djangoapp/logout/   → logout endpoint
    path('logout/',   views.logout_user,   name='logout'),
    path(route='get_cars', view=views.get_cars, name ='getcars'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
