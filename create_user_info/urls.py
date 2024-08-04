
from django.urls import path,include
from create_user_info import views
from rest_framework.routers import DefaultRouter
from .views import CourseNamesViewSet, ContactFormViewSet, EnrollFormViewSet


router = DefaultRouter()
router.register(r'course-names', CourseNamesViewSet)
router.register(r'contact-forms', ContactFormViewSet)
router.register(r'enroll-forms', EnrollFormViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('courses_drop/',views.course_drop_list,name='course_drop'),
    path('courses/<int:pk>/', views.courses, name='courses'),
    path('search/', views.course_search, name='course_search'),
    path('contact/', views.contact, name='contact'),
    path('mini_projects/',views.mini_projects,name='mini_projects'),
    path('enroll/',views.enroll,name='enroll'),
    path('python/',views.python_developer,name='python'),
    path('Computer_vision/',views.Computer_vision_developer,name='computer_vision'),
    path('selenium_testing/',views.seleinum_testing_developer,name='selenium_testing'),
    path('machine_larning/',views.machine_learning_developer,name='machine_larning'),
    path('api/', include(router.urls)),
   

    ]
