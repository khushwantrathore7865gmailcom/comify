from django.urls import path, include
from .views import Home, login, signup, add_new_Service, desc_service, search, category, user_service
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', Home, name="Home"),
    path('login/', login, name="Login"),
    path("register/", signup, name="Register"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('addNewService/', add_new_Service, name='addNewService'),
    path('service/<int:pk>', desc_service, name='descService'),
    path('search/<str:string>', search, name='search'),
    path('category/<str:string>', category, name='category'),
    path('MyServices/', user_service, name='myservice')
]
