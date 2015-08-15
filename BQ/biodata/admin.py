from django.contrib import admin

from .models import BioSiswa, BioOrtu

class BioOrtuInline(admin.StackedInline):
	model = BioOrtu
	extra = 0



class BioSiswaAdmin(admin.ModelAdmin):
	inlines = [BioOrtuInline]
	list_display = ('NISL','nama_depan','nama_belakang')


admin.site.register(BioSiswa, BioSiswaAdmin)