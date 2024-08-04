
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm  # Built-in form for user registration
from django.contrib import messages
from .models import course_explore
from django.shortcuts import render,get_object_or_404
from django.core.mail import send_mail
from .models import contact_form,enroll_form,course_names
from django.conf import settings

def home(request):
    courses=course_explore.objects.all()
    return render(request, 'home.html',{'courses':courses})

def about_us(request):
    courses=course_explore.objects.all()
    return render(request, 'about_us.html',{'courses':courses})

def course_drop_list(request):
    courses=course_explore.objects.all()
    return render(request, 'base.html',{'courses':courses})

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        contact = contact_form(name=name, email=email, message=message)
        contact.save()
        # send_mail(
        #     subject=f"Contact Form Submission from {name}",
        #     message=message,
        #     from_email=email,
        #     recipient_list=['your_email@example.com'],  # Replace with your email
        # )
        print(contact)
        messages.success(request,'Thank you for contacting ,i will get back you')
        return redirect ('contact')
    courses=course_explore.objects.all()
    return render(request, 'contact_page.html',{'courses':courses})

def mini_projects(request):
    courses=course_explore.objects.all()
    return render(request, 'mini_projects.html',{'courses':courses})

def enroll(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phonenumber=request.POST['phone']
        course=request.POST['course']
        course_instance=course_names.objects.get(course=course)
        enroll = enroll_form(name=name, email=email,phonenumber=phonenumber,course=course_instance)
        enroll.save()

        subject = 'welcome to Varma institute of Tech Solutions'
        message = f'Hi {enroll.name}, thank you for registering in varmainstitute tech solutions.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [enroll.email, ]
        send_mail( subject, message, email_from, recipient_list )
        print(contact)

        return render(request,'enroll_sucess.html')
    courses=course_explore.objects.all()
    return render(request,'enroll.html',{'courses':courses})

# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, username=email, password=password)
        
#         if user is not None:
#             login(request, user)
#             return redirect('/home/')  # Redirect to home after successful login
#         else:
#             messages.error(request, 'Invalid email or password.')  # Show an error message
#     return render(request, 'login.html')

# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)  # You can create a custom form if needed
#         if form.is_valid():
#             form.save()  # Save the new user
#             messages.success(request, 'Registration successful! You can log in now.')  # Show a success message
#             return redirect('/login/')  # Redirect to login after successful registration
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})


def python_developer(request):

    return render(request,'python_developer.html')

def Computer_vision_developer(request): 
    return render(request,'Computer_vision_developer.html')


def seleinum_testing_developer(request): 
    return render(request,'seleinum_testing_developer.html')

def machine_learning_developer(request): 
    return render(request,'machine_learning_developer.html')


def courses(request,pk):
    course= course_explore.objects.filter(pk=pk)
   
    return render (request,'course_page.html',{'course':course})

def course_search(request):
    query = request.GET.get('q')
    if query:
        try:
            course = course_explore.objects.get(course_name__course__icontains=query)
            return redirect('courses', pk=course.pk)
        except course_explore.DoesNotExist:
            return render(request, 'course_not_found.html', {'query': query})
    else:
        return redirect('course_drop')
    





    # create API viewsets

from rest_framework import viewsets
from .serializers import CourseNamesSerializer, ContactFormSerializer, EnrollFormSerializer

class CourseNamesViewSet(viewsets.ModelViewSet):
    queryset = course_names.objects.all()
    serializer_class = CourseNamesSerializer

class ContactFormViewSet(viewsets.ModelViewSet):
    queryset = contact_form.objects.all()
    serializer_class = ContactFormSerializer

class EnrollFormViewSet(viewsets.ModelViewSet):
    queryset = enroll_form.objects.all()
    serializer_class = EnrollFormSerializer
    


