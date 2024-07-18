from django.urls import path
from .views import employeeregister
from .views import getallemployee
from .views import deleteemployee,updateemployee


urlpatterns = [
    path('dashboard/',getallemployee,name='getallemployee'),
    path('employeeregister/',employeeregister,name='employeeregister'),
    path('deleteemployee/<int:id>',deleteemployee,name='deleteemployee'),
    # path('editemployee/<int:id>',editemployee,name='editemployee'),
    path('updateemployee/<int:id>',updateemployee,name='updateemployee')
]

