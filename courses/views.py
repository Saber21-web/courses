from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Payment
from .forms import CourseForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
    else:
        form = CourseForm(instance=course)
    
    return render(request, 'courses/course_detail.html', {'form': form, 'course': course})

def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses_list.html', {'courses': courses})

@login_required(login_url='login')
def course_buy(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'courses/course_buy.html', {'course': course})

def payment_page(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    payment = Payment(amount=100, status="Pending")
    payment.save()  # Сохраняем платеж в базе данных

    payment = Payment({
        "intent": "sale",
        "payer": {"payment_method": "paypal"},
        "redirect_urls": {
                    "return_url": request.build_absolute_uri(reverse('courses:paypal_success', kwargs={'course_id': course.id})),
                    "cancel_url": request.build_absolute_uri(reverse('courses:paypal_cancel', kwargs={'course_id': course.id})),
        },
        "transactions": [{
            "amount": {
                "total": str(course.price),
                "currency": "USD"
            },
            "description": course.name
        }]
    })

    if payment.create():

        return redirect(payment.links[1].href)

def payment_success(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.purchased = True
    course.save()
    return render(request, 'courses/payment_success.html', {'course': course})

def payment_cancel(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/payment_cancel.html', {'course': course})