from django.shortcuts import render, get_object_or_404, redirect
from . models import Food, Item
from . forms import ItemForm, UserForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def index(request):
    foods = Food.objects.all()
    return render(request, 'Hotelapp/index.html', {'foods': foods})

def detail(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    return render(request, 'Hotelapp/detail.html', {'food': food})

def final(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    return render(request, 'Hotelapp/final_order.html', {'food': food})

def cancel_order(request, food_id, item_id):
    food = get_object_or_404(Food, pk=food_id)
    item = get_object_or_404(food.item_set, pk=item_id)
    item .delete()
    context = {'food': food,
               'message': 'Item Cancelled!'
               }
    return render(request, 'Hotelapp/detail.html', context)

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                albums = Food.objects.all(user=request.user)
                login(request, user)
                return render(request, 'Hotelapp:index.html', {'albums': albums})
    return render(request, 'Hotelapp/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                foods = Food.objects.all(user=request.user)
                return render(request, 'Hotelapp:login.html', {'foods': foods})
    return render(request, 'Hotelapp/index.html')


def logout_user(request):
    logout(request)
    return redirect('Hotelapp:login')

def add_item(request, food_id):
    form = ItemForm(request.POST or None)
    food = get_object_or_404(Food, pk=food_id)
    if form.is_valid():
            item = form.save(commit=False)
            item.food = food
            item.save()
            context = {'food': food,
                   }
            return render(request, 'Hotelapp/detail.html', context)
    form = ItemForm()
    return render(request, 'Hotelapp/add_item.html', {'form': form})


