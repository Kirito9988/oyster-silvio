from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'main/home.html')


def how_it_works(request):
    return render(request, 'main/how_it_works.html')


def products(request):
    return render(request, 'main/products.html')


def cost(request):
    return render(request, 'main/cost.html')


def about(request):
    return render(request, 'main/about.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # or wherever you want to redirect after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form})


def start(request):
    # ... your code for the view ...
    return render(request, 'start.html')