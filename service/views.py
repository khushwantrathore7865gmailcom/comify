from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Baner, Feature_service, Service, Profile, service_picture
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import RegisterForm


# Create your views here.
def Home(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        return redirect("search", search)
    if request.user.is_authenticated:

        u = False
        try:
            p = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return redirect('Profile')
    else:

        u = True


    b = Baner.objects.all()
    f=0
    if len(b)>0:
        if b[0].Baner_Display:
            print(b[0].Title)
            f = 1


    feature = Feature_service.objects.all()
    if len(feature) > 0:
        len_feature = True
    else:
        len_feature = False
    service = Service.objects.all()

    return render(request, "Home.html",
                  {'flag': f, 'b': b, 'u': u, 'len_f': len_feature, "feat": feature, 'service': service})


def Login(request):
    if request.user.is_authenticated:
        print(request.user)
        return redirect('Home')
    else:
        if request.user.is_authenticated:

            u = False
        else:

            u = True
        if request.method == 'POST':
            username = request.POST.get('exampleInputEmail1')
            password = request.POST.get('pass')

            print(username)
            print(password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
                print('Username OR password is incorrect')
                messages.info(request, 'Username OR password is incorrect')

        context = {'u':u}
        return render(request, 'login.html', context)


@login_required(login_url='/login')
def profile_form(request):

    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        photo = request.FILES.get('pp')
        p = Profile(name=name, user=request.user, gender=gender, age=age, address=address, profile_pic=photo)
        p.save()
        return redirect('Home')

    context = {}
    if request.user.is_authenticated:

        u = False
    else:

        u = True

    return render(request, 'profile_form.html', {'u': u})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('exampleInputEmail1')
        print(username)
        password = request.POST.get('pass')
        print("***", password)
        if User.objects.filter(email=username).exists():
            messages.error(request, ('Email already exist please use another Email'))

        else:
            # user = User(username=username, email=username, password=password)

            # user.is_active = True  # change this to False after testing
            # user.is_company = True  # Deactivate account till it is confirmed
            # user.save()
            user = User.objects.create_user(username=username, email=username, password=password, is_active=True)
            login(request, user)
            return redirect('Profile')

    context = {}
    return render(request, 'register.html', context)


@login_required(login_url='/login')
def add_new_Service(request):
    if request.method == 'POST':
        category = request.POST.get('cat')
        subcategory = request.POST.get('specificSizeSelect')
        name = request.POST.get('name')
        address = request.POST.get('address')
        desc = request.POST.get('desc')
        photo = request.FILES.getlist('pp')
        whatsapp = request.POST.get('whatsapp')
        phone = request.POST.get('phone')
        insta = request.POST.get('insta')
        wh = "https://wa.me/" + whatsapp
        print(photo)

        ser = Service(provider=request.user, category=category, service_name=name, address=address, desc=desc,
                      whatsapp=wh, instagram=insta, phone=phone,profile_pic=photo[0])
        ser.save()
        for p in photo:
            ph = service_picture(service=ser, profile_pic=p)
            ph.save()
        return redirect("Home")
    if request.user.is_authenticated:

        u = False
    else:

        u = True
    return render(request, 'add-service.html')


def desc_service(request, pk):
    if request.user.is_authenticated:

        u = False
    else:

        u = True
    service = Service.objects.get(pk=pk)
    photo = service_picture.objects.filter(service=service)
    ph=photo[0]
    serv = Service.objects.all()
    if request.user.is_authenticated:

        u = False
    else:

        u = True
    return render(request, 'service2.html', {'u':u,'service': service, 'related': serv,'photo':photo,'p':ph})


def search(request, string):
    service = Service.objects.filter(service_name__icontains=string)
    if request.user.is_authenticated:

        u = False
    else:

        u = True
    return render(request, 'search.html', {'service': service})


def category(request, string):
    service = Service.objects.filter(category=string)
    if request.user.is_authenticated:

        u = False
    else:

        u = True
    return render(request, 'search.html', {'u':u,'service': service})

@login_required(login_url='/login')
def user_Profile(request):
    u = request.user

    service = Service.objects.filter(provider=u)
    if len(service) > 0:
        s = True
    else:
        s = False

    pr = Profile.objects.get(user=u)
    if request.user.is_authenticated:

        ue = False
    else:

        ue = True
    return render(request, 'profile.html', {'service': service, 'pr': pr, 'u': u, 'se': s, 'ue': ue})


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            print("============", form.data["password1"])
            form.save()

        return redirect("/login")
    else:
        form = RegisterForm()

    return render(response, "s2.html", {"form": form})
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
