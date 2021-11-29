from .models import Student
from .forms import StudentForm
from django.shortcuts import render,redirect, get_object_or_404
 
def CreateStudent(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentForm()
    else:
        form = StudentForm()

    students = Student.objects.all().order_by("-id")
    context = {'form':form, 'students':students}
    return render(request, 'home.html', context)

def GetStudent(request, **kwargs):
    reg = kwargs.get('reg')
    student = get_object_or_404(Student, reg_no=reg)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm(instance=student)

    context = {'student':student, 'form': form}
    return render(request, 'std_detail.html', context )

def DeleteStudent(request, **kwargs):
    reg = kwargs.get('reg')
    student = Student.objects.get(reg_no=reg)
    student.delete()
    return redirect('home')