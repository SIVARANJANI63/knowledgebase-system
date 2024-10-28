from django.shortcuts import render, redirect
from .forms import R_f  # Replace with your actual form
from .models import Registration  # Replace with your actual model

def index(request):
    return render(request, 'index.html') 
 # Render the index.html template

def register(request):
    if request.method == 'POST':
        form = R_f(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table_view')
    else:
        form = R_f()
    return render(request, 'register.html', {'form': form})

def table_view(request):
    registrations = Registration.objects.all()  # Query all records from the Registration table
    return render(request, 'table_view.html', {'registrations': registrations})
