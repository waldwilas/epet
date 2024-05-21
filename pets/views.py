from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Pet
from .forms import PetForm


@login_required
def index(request):
    context = {
        'pets': Pet.objects.filter(owner=request.user)
    }

    return render(request, 'pets/index.html', context)


@login_required
def show_pet(request, id: int):
    pet = get_object_or_404(Pet, id=id)

    if request.user != pet.owner and not request.user.is_superuser:
        return redirect('pets:index')

    return render(request, 'pets/show.html', {'pet': pet})


@login_required
def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
           pet = form.save(commit=False)
           pet.owner = request.user
           pet.save()
        return redirect('pets:show', id=pet.id)
    else:
        form = PetForm()

    context = {'form': form}

    return render(request, 'pets/add.html', context)


@login_required
def edit_pet(request, id):
    return redirect('pets:show', id=id)


@login_required
def delete_pet(request, id):
    pet = get_object_or_404(Pet, id=id)

    if request.user != pet.owner and not request.user.is_superuser:
        return redirect('pets:index')

    if request.method == 'POST':
        pet.delete()
        return redirect('pets:index')

    context = {'pet': pet}

    return render(request, 'pets/delete.html', context)
