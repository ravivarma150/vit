# your_app/context_processors.py

from .models import course_explore

def courses_context_processor(request):
    courses = course_explore.objects.all()
    return {'courses': courses}
