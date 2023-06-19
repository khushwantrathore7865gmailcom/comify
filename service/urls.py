from django.urls import path, include, reverse_lazy
from .views import Home, Login, signup, add_new_Service, desc_service, search, category, user_Profile, register, \
    profile_form, delete, edit_Service, deletePic, aboutus
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', Home, name="Home"),
    path('login/', Login, name="Login"),
    path("register/", signup, name="Register"),
    path("r/", register, name="R"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('addNewService/', add_new_Service, name='addNewService'),
    path('service/<int:pk>', desc_service, name='descService'),
    path('search/<str:string>', search, name='search'),
    path('delete/<int:pk>', delete, name='delete'),
    path('deletePic/<int:pk>', deletePic, name='deletePic'),
    path('edit/<int:pk>', edit_Service, name='edit'),
    path('category/<str:string>', category, name='category'),
    path('MyProfile/', user_Profile, name='myProfile'),
    path('aboutUs/', aboutus, name='aboutUs'),
    path('Profile/', profile_form, name='Profile'),
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='account/password_reset.html', email_template_name='account/password_reset_emailre.html',
        success_url=reverse_lazy('password_reset_done')),
         name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="account/password_reset_confirm.html",
        success_url=reverse_lazy('password_reset_complete')), name='password_reset_confirm'),
    path('account/reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='account/password_reset_complete.html'), name='password_reset_complete'),

]
