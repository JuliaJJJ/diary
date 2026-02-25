from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import User
from .models import Lesson, Attendance
from .forms import LessonForm


@login_required
def create_lesson(request):
    # Проверяем, что пользователь в группе Teacher
    if not request.user.groups.filter(name='Teacher').exists():
        return redirect('home')

    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.teacher = request.user
            lesson.save()
            return redirect('all_lessons')
    else:
        form = LessonForm()

    return render(request, 'lessons/create_lesson.html', {'form': form})


@login_required
def all_lessons(request):
    lessons = Lesson.objects.all()
    return render(request, 'lessons/all_lessons.html', {'lessons': lessons})


@login_required
def mark_attendance(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    students = User.objects.filter(groups__name='Student')

    if request.method == 'POST':
        for student in students:
            present = request.POST.get(str(student.id)) == 'on'

            Attendance.objects.update_or_create(
                lesson=lesson,
                student=student,
                defaults={'is_present': present}
            )

        return redirect('all_lessons')

    return render(request, 'lessons/attendance.html', {
        'lesson': lesson,
        'students': students
    })