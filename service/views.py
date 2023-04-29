from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Baner, Feature_service, Service
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import SignUpForm


# Create your views here.
def Home(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        return redirect("search", search)
    if request.user.is_authenticated:

        u = False
    else:

        u = True
    b = Baner.objects.all()[0]
    f = 0
    if b.Baner_Display:
        f = 1
    feature = Feature_service.objects.all()
    if len(feature) > 0:
        len_feature = True
    else:
        len_feature = False
    service = Service.objects.all()

    return render(request, "Home.html",
                  {'flag': f, 'b': b, 'u': u, 'len_f': len_feature, "feat": feature, 'service': service})


def login(request):
    if request.user.is_authenticated:
        print(request.user)
        return redirect('Home')
    else:
        if request.method == 'POST':
            username = request.POST.get('exampleInputEmail1')
            password = request.POST.get('pass')
            # print(username)
            # print(password)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
                print('Username OR password is incorrect')
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('exampleInputEmail1')
        print(username)
        password = request.POST.get('pass')
        print("***", password)
        if User.objects.filter(email=username).exists():
            messages.error(request, ('Email already exist please use another Email'))
        # print(username)
        # print(password)
        else:
            user = User(username=username, email=username, password=password)

            user.is_active = True  # change this to False after testing
            # user.is_company = True  # Deactivate account till it is confirmed
            user.save()
            return redirect('Login')

    context = {}
    return render(request, 'register.html', context)


@login_required(login_url='/login')
def add_new_Service(request):
    if request.method == 'POST':
        category = request.POST.get('specificSizeSelect')
        name = request.POST.get('name')
        address = request.POST.get('address')
        desc = request.POST.get('desc')
        photo = request.FILES.get('pp')
        whatsapp = request.POST.get('whatsapp')
        phone = request.POST.get('phone')
        insta = request.POST.get('insta')
        wh = "https://wa.me/" + whatsapp
        ser = Service(provider=request.user, category=category, service_name=name, address=address, desc=desc,
                      profile_pic=photo, whatsapp=wh, instagram=insta, phone=phone)
        ser.save()
        return redirect("Home")
    return render(request, 'add-service.html')


def desc_service(request, pk):
    service = Service.objects.get(pk=pk)
    serv = Service.objects.all()
    return render(request, 'service.html', {'service': service, 'related': serv})


def search(request, string):
    service = Service.objects.filter(service_name__icontains=string)
    return render(request, 'search.html', {'service': service})


def category(request, string):
    service = Service.objects.filter(category=string)
    return render(request, 'search.html', {'service': service})


def user_service(request):
    u = request.user
    service = Service.objects.filter(provider=u)
    return render(request, 'search.html', {'service': service})

# class ActivateAccount(View):
#
#     def get(self, request, uidb64, token, *args, **kwargs):
#         try:
#             uid = force_text(urlsafe_base64_decode(uidb64))
#             user = User_custom.objects.get(pk=uid)
#         except (TypeError, ValueError, OverflowError, User_custom.DoesNotExist):
#             user = None
#
#         if user is not None and account_activation_token.check_token(user, token):
#             user.is_active = True
#
#             pr = patnerComp.objects.get(user=user)
#             pr.is_email_verified = True
#             pr.save()
#             user.save()
#             login(request, user)
#             messages.success(request, ('Your account have been confirmed.'))
#             return redirect('partner_company:partner_company_home')
#         else:
#             messages.warning(
#                 request, ('The confirmation link was invalid, possibly because it has already been used.'))
#             return redirect('user:Login')
#
