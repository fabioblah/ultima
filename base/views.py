from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PetReservationForm

def reserve_bath(request):
    if request.method == 'POST':
        form = PetReservationForm(request.POST)
        if form.is_valid():
            # Salvar a reserva do banho
            form.save()
            return HttpResponseRedirect('/reserve_success/')
    else:
        form = PetReservationForm()

    return render(request, 'reserve_bath.html', {'form': form})
