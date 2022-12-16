from django.shortcuts import render, redirect
from .forms import PersonaForm
from .models import persona
# from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def person(request):
    per = persona.objects.all()
    if request.method == 'GET':
        return render(request, 'Index.html',{
            'form' : PersonaForm,
            'personas' : per
        })
    else:
        form = PersonaForm(request.POST)
        new_per = form.save(commit=False)
        new_per.save()
        return render(request, 'Index.html', {
            'form' : PersonaForm,
            'personas' : per
        })

def modificar(request, per_id):
    if request.method == 'GET':
        per = persona.objects.get(pk=per_id)
        form = PersonaForm(instance=per)
        return render(request, 'update.html',{
            'persona' : per,
            'form' : form
        })
    else:
        per = persona.objects.get(pk=per_id)
        form = PersonaForm(request.POST, instance=per)
        form.save()
        return redirect('inicio')

def eliminar(request, per_id):
    per = persona.objects.get(pk = per_id)
    per.delete()
    return redirect('inicio')