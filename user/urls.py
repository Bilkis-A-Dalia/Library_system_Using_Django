
from django.urls import path
from .import views

urlpatterns = [
    path('signup/',views.RegistrationView.as_view(),name='signup'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
    path('pass_change/',views.pass_change,name='pass_change'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('profile/',views.profile,name='profile'),
    path('order/<int:id>',views.order,name='order'),
]