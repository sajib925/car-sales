from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Car,  Order
from .forms import CommentForm



def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    comments = car.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CommentForm()
    return render(request, 'car_detail.html', {'car': car, 'comments': comments, 'form': form})

@login_required
def buy_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if car.quantity > 0:
        Order.objects.create(user=request.user, car=car)
        car.quantity -= 1
        car.save()
        return redirect('profile')
    return redirect('car_detail', pk=car.pk)

@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'profile.html', {'orders': orders})
