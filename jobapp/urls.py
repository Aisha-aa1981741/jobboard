from django.urls import path
from .views import *

urlpatterns = [
    # Other URL patterns
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', jobs, name='jobs'),
    path('postjob/', postjob, name='postjob'),
    path('updatejob/', updatejob, name='updatejob'),
    path('jobdetail/<int:id>/', jobdetail, name='jobdetail'),
]
