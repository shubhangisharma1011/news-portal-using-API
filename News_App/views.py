from django.contrib.auth.decorators import login_required
from django.contrib.sites import requests
from django.shortcuts import render
import requests
import json
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from .models import User_Model_Email_Verification
from .forms import CreateUserForm
from django.core.mail import send_mail
from django.conf import settings
import uuid
# Create your views here.
@method_decorator(login_required, name='dispatch')
class Home_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Home.html', {'api': api})


@method_decorator(login_required, name='dispatch')
class Apple_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/everything?q=apple&from=2021-07-07&to=2021-07-07&sortBy=popularity&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Apple.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Tesla_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2021-06-08&sortBy=publishedAt&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Tesla.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Tech_Crunch_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Tech_Crunch.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class World_News_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'World.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Latest_News_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Latest_News.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class India_News_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'India_News.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class India_Business_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'India_Business.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class India_Health_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'India_Health.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class India_Science_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'India_Science.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class India_Sports_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'India_Sports.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class India_Sports_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'India_Sports.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class India_Technology_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'India_Technology.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class India_Entertainment_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'India_Entertainment.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Argentina_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=ar&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Argentina.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Australia_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=au&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Australia.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Austria_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=at&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Austria.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Belgium_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=be&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Belgium.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Brazil_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=br&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Brazil.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Bulgaria_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=bg&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Bulgaria.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Canada_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=ca&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Canada.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class China_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=cn&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'China.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Colombia_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=co&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Colombia.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Cuba_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=cu&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Cuba.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Czech_Republic_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=cz&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Czech_Republic.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Egypt_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=eg&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Egypt.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class France_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=fr&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'France.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Germany_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=de&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Germany.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Greece_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=gr&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Greece.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Hong_Kong_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=hk&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Hong_Kong.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Hungary_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=hu&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Hungary.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Indonesia_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=id&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Indonesia.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Ireland_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=ie&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Ireland.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Israel_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=il&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Israel.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Italy_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=it&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Italy.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Japan_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=jp&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Japan.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Latvia_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=lv&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Latvia.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Malaysia_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=my&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Malaysia.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Mexico_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=mx&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Mexico.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Morocco_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=ma&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Morocco.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class Netherland_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=nl&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'Netherland.html', {'api':api})


@method_decorator(login_required, name='dispatch')
class New_Zealand_View(View):
    def get(self, request):
        business_news = requests.get("https://newsapi.org/v2/top-headlines?country=nz&apiKey=4b7b547583e146e1b0a0a953ef4e59c5")
        api = json.loads(business_news.content)
        return render(request, 'New_Zealand.html', {'api':api})


def send_email_after_registration(email,token):
    subject = "Verify Email"
    message = f"Hi click on the link to verify your account http://127.0.0.1:8000/account-verify/{token}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)


class Registration_View(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request,'Registration_2.html',{'form':form})
    def post(self, request):
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            new_user = form.save()
            uid = uuid.uuid4()
            em_obj = User_Model_Email_Verification(user=new_user, token=uid)
            em_obj.save()
            send_email_after_registration(new_user.email, uid)
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            messages.success(request, 'verification link send to your email' + first_name+ last_name)
        else:
            print(form.errors)  # for display the error via form
            context = {'form': form}
            return render(request, 'Registration_2.html', context)
        return redirect('/')


def account_verify(request, token):
    account_activate = User_Model_Email_Verification(token=token)
    account_activate.verify = True
    account_activate.save()
    return redirect('Login_View')


class Login_View(View):
    def get(self,request):
        form = CreateUserForm()
        context = {'form':form}
        return render(request, 'Login.html',context)
    def post(self, request):
        form = CreateUserForm(request.POST)
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
        else:
            messages.error(request, 'Please fill the correct details')
            return redirect('Home_View')
        messages.success(request,"Welcome! "+email)
        return redirect('Home_View')


class Logout_View(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Successfully logout")
        return redirect('/')

"""
from .models import Blog,CustomUser

def index(request):
    blog=Blog.objects.all()
    context={'blogs':blog}

    return render(request,'index.html',context)

def blog_post(request):
    if request.method=='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        blog = Blog(title=title,content=content,user_id=request.user)
        blog.save()
        messages.success(request,"Post has been submitted successfully!!")
        return redirect('index')
    blog = Blog.objects.all()
    context = {'blogs': blog}

    return render(request,'blog_post.html',context)

def blog_detail(request,id):
    blog = Blog.objects.get(id=id)
    return render(request,'blog_detail.html',{'blog':blog})


def delete_post(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    messages.success(request,"Post has been deleted successfully!!")"""
#    return redirect('index')

