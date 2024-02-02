from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .forms import SignUpForm #register
from .forms import NameForm #get name
from django.contrib.auth.decorators import login_required #login auth 
from .forms import ImageUploadForm #image

# Create your views here.
def home(request):
    return render(request, template_name='pages/home.html')

def aboutPage(request):
    return render(request, template_name='pages/about.html')

def index(request):
    return render(request, template_name='pages/index.html')

def navbar(request):
    return render(request, template_name='pages/navbar.html')

def footer(request):
    return render(request, template_name='pages/footer.html')

def artists(request):
    return render(request, template_name='pages/artists.html')

def gallery(request):
    return render(request, template_name='pages/gallery.html')

def profile_1(request):
    return render(request, template_name='pages/profile_1.html')

def profile_2(request):
    return render(request, template_name='pages/profile_2.html')

def profile_3(request):
    return render(request, template_name='pages/profile_3.html')

def profile_4(request):
    return render(request, template_name='pages/profile_4.html')

def profile_5(request):
    return render(request, template_name='pages/profile_5.html')

def profile_6(request):
    return render(request, template_name='pages/profile_6.html')

def profile_7(request):
    return render(request, template_name='pages/profile_7.html')

def profile_8(request):
    return render(request, template_name='pages/profile_8.html')

def profile_9(request):
    return render(request, template_name='pages/profile_9.html')

def success(request):
    return render(request, template_name='pages/success.html')

def make(request):
    return render(request, template_name='pages/make.html')

def test(request):
    return render(request, template_name='pages/test.html')

# users/views.py
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = SignUpForm()
    return render(request, 'pages/register.html', {'form': form})

#login view
def custom_login(request):
    return render(request, template_name='pages/login.html')
#get name
def name_template(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            template = f"Hello {first_name} {last_name}! Welcome to our platform."
            return render(request, 'pages/test.html', {'template': template})
    else:
        form = NameForm()

    return render(request, 'pages/make-2.html', {'form': form})
#upload image
def image_upload_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/success/')  # Redirect to success page after successful upload
    else:
        form = ImageUploadForm()

    return render(request, 'pages/upload.html', {'form': form})
@login_required
def conditional_template(request):
    # If the user is logged in, use a different template
    if request.user.is_authenticated:
        template_name = 'http://127.0.0.1:8000/success/'
    else:
        template_name = 'http://127.0.0.1:8000/register/'

    return render(request, template_name)