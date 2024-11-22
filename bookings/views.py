from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Booking
from .forms import BookingForm

# Create your views here.
def bookings_home(request):
    all_bookings = Booking.objects.filter(booked=False)

    context = {
        'bookings': all_bookings,
    }

    return render(request, 'bookings/all_bookings.html', context)

def my_bookings(request):
    all_bookings = Booking.objects.filter(user=request.user)

    context = {
        'bookings': all_bookings,
    }

    return render(request, 'bookings/my_bookings.html', context)

def create_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            updated_booking = form.save(commit=False)
            updated_booking.user = request.user
            updated_booking.booked = True
            updated_booking.save()
            messages.success(request, "Booking created successfully.")
            return redirect('my_bookings')
        else:
            return redirect('bookings_home')
    else:
        form = BookingForm(instance=booking)
        context = {
            "form": form,
        }
        return render(request, 'bookings/create_booking.html', context)

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        booking.user = None
        booking.booked = False
        booking.doctor_type = None 
        booking.save()
        messages.success(request, "Booking cancelled successfully.")
        return redirect('my_bookings')
    else:
        form = BookingForm(instance=booking)
        context = {
            "form": form,
        }
        return render(request, 'bookings/cancel_booking.html', context)