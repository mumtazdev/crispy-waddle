from django.db import models

# di edit agus

class BioSiswa(models.Model):
	NISL = models.IntegerField(primary_key=True, unique=True)
	NISN = models.IntegerField(unique=True)
	nama_depan = models.CharField(max_length=20)
	nama_belakang = models.CharField(max_length=20)
	tempat_lahir = models.CharField(max_length=20)
	tanggal_lahir = models.DateField()
	alamat = models.CharField(max_length=200)
	foto = models.ImageField()
	def __str__(self):
		return self.nama_depan

class BioOrtu(models.Model):
	PENDIDIKAN = (
		('TDK','Tidak Sekolah'),
		('SD','Sekolah Dasar'),
		('SMP', 'Sekolah Menengah'),
		('SMA', 'Sekolah Atas'),
		('D3', 'Diploma'),
		('S1', 'S1'),
		('S2', 'S2'),
		('S3', 'S3'),
	)
	PEKERJAAN = (
		('TDK','Tidak Bekerja'),
		('PN','Pegawai Negeri'),
		('PS', 'Pegawai Swasta'),
		('WS', 'Wira Swasta'),
		('RT', 'Ibu Rumah Tangga'),
	)
	anak = models.ForeignKey(BioSiswa)
	nama_ayah = models.CharField(max_length=40)
	pendidikan_ayah = models.CharField(max_length=200, choices=PENDIDIKAN)
	pekerjaan_ayah = models.CharField(max_length=200, choices=PEKERJAAN)
	nama_ibu = models.CharField(max_length=40)
	pendidikan_ibu = models.CharField(max_length=200, choices=PENDIDIKAN)
	pekerjaan_ibu = models.CharField(max_length=200, choices=PEKERJAAN)
	alamat = models.CharField(max_length=200)
	no_telp = models.IntegerField(blank=True, null=True)
	no_hp = models.IntegerField(blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	def __str__(self):
			return self.nama_ayah

