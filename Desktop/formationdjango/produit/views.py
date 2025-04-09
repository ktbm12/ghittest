from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from .models import produit  # ← ton modèle s'appelle "produit" avec p minuscule
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .form import CustomAuthenticationForm

def index(request, *args, **kwargs):
    liste = produit.objects.all()
    context = {
        'produits': liste  
    }
    return render(request, 'index.html', context)

class Create_Produit(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'produit/create.html')

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        produit.objects.create(name=name, price=price, description=description, image=image)
        messages.success(request, 'Produit créé avec succès.')
        return redirect('index')

def delete_produit(request, pk):
    objet = get_object_or_404(produit, pk=pk)
    objet.delete()
    messages.success(request, "Le produit a été supprimé avec succès.")
    return redirect('index')

def update_produit(request, pk):
    obj = get_object_or_404(produit, pk=pk)

    if request.method == 'POST':
        obj.name = request.POST.get('name')
        obj.price = request.POST.get('price')
        obj.description = request.POST.get('description')
        if request.FILES.get('image'):
            obj.image = request.FILES['image']
        obj.save()
        messages.success(request, "Produit mis à jour avec succès.")
        return redirect('index')

    return render(request, 'produit/update.html', {'produit': obj})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            # Authentification de l'utilisateur
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Assure-toi que 'home' est une URL valide
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})
