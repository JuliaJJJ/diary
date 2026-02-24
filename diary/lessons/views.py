from django.http import HttpResponse
from .models import Lesson

def all_lessons(request):
    lessons = Lesson.objects.all()
    text = ""

    for lesson in lessons:
        text += lesson.name + "<br>"

    return HttpResponse(text)