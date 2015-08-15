from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic

from .models import BioSiswa, BioOrtu


class IndexView(generic.ListView):
    template_name = 'biodata/index.html'
    context_object_name = 'nama_siswa'

    def get_queryset(self):
        """Return the last five published questions."""
        return BioSiswa.objects.order_by('NISL')[:5]
