from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Ilan
# Create your views here.

class AnasayfaView(TemplateView):
    template_name = 'anasayfa.html'

class IlanlarView(ListView):
    model = Ilan
    template_name = 'ilanlar.html'

def ilan_detay(request, ilan_id):
    ilanimiz = get_object_or_404(Ilan, pk=ilan_id)
    return render(request, 'ilan.html', {'ilan_context': ilanimiz})