from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from coursemanager.forms import RegistrationForm
from .models import Course
from .forms import CourseForm



@login_required
def course_list(request):
    query = request.GET.get("q", "")

    if query:
        courses = Course.objects.filter(
    Q(title__icontains=query) |
    Q(instructor__icontains=query)
).order_by("id")
    else:
        courses = Course.objects.all().order_by("id")
    paginator = Paginator(courses, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "courses/course_list.html",
        {
            "page_obj": page_obj,
            "query": query,
        }
    )

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    return render(
        request,
        "courses/course_detail.html",
        {"course": course},
    )
@login_required
def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("course_list")

    else:
        form = CourseForm()

    return render(request, "courses/course_form.html", {"form": form})
@login_required
def course_update(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect("course_detail", course_id=course.id)
    else:
        form = CourseForm(instance=course)

    return render(
        request,
        "courses/course_form.html",
        {"form": form},
    )
@login_required
def course_delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == "POST":
        course.delete()
        return redirect("course_list")

    return render(
        request,
        "courses/course_confirm_delete.html",
        {"course": course},
    )
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            login(request, user)
            return redirect("course_list")
    else:
        form = RegistrationForm()

    return render(
        request,
        "registration/register.html",
        {"form": form},
    )