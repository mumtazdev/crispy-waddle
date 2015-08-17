from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from .models import BioOrtu, BioSiswa


def index(request):
    list_siswa = BioSiswa.objects.order_by('-NISL')[:5]
    output = ', '.join([p.nama_depan for p in list_siswa])
    return HttpResponse(output)

def detail(request, anak_id):
	return HttpResponse("You're looking at biodata %s." % anak_id)