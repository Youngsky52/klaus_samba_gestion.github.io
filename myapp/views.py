from django.shortcuts import render, redirect

from myapp.form import EtudiantForm
from myapp.models import Etudiant


# Create your views here.
def form_l(request):
    return render(request, 'acceuil.html')


def index(request):
    form = EtudiantForm
    return render(request, "index.html", {'form':form })

def ajouter(request):
    form = EtudiantForm(request.POST)
    form.save()
    return redirect('afficher')



def afficher(request):
    etudiant = Etudiant.objects.all()
    if request.method=='GET':
        nom =request.GET.get('rech')
        if nom is not None:
          etudiant = Etudiant.objects.filter(nom__icontains=nom)
    else:
        etudiant = Etudiant.objects.all()

    return render(request, 'afficher.html', {'etudiant': etudiant })


def modifier(request, id):
    etudiant = Etudiant.objects.get(id=id)

    return render(request, 'modifier.html', context={'etudiant': etudiant })


def mise_a_j(request, id):
    etudiant = Etudiant.objects.get(id=id)
    form = EtudiantForm(request.POST, instance=etudiant)
    form.save()
    return redirect('afficher')

def supprimer(request, id):
    etud = Etudiant.objects.get(id=id)
    etud.delete()
    return redirect('afficher')


def base(request):
    return render(request, 'base.html')