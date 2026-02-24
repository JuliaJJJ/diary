from django.http import HttpResponse

def all_lessons(request):

    if request.user.groups.filter(name='Teachers').exists():
        return HttpResponse("Це вчитель")

    return HttpResponse("Ви не вчитель")