# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BioOrtu',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nama_ayah', models.CharField(max_length=40)),
                ('pendidikan_ayah', models.CharField(max_length=200, choices=[('TDK', 'Tidak Sekolah'), ('SD', 'Sekolah Dasar'), ('SMP', 'Sekolah Menengah'), ('SMA', 'Sekolah Atas'), ('D3', 'Diploma'), ('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3')])),
                ('nama_ibu', models.CharField(max_length=40)),
                ('pendidikan_ibu', models.CharField(max_length=200, choices=[('TDK', 'Tidak Sekolah'), ('SD', 'Sekolah Dasar'), ('SMP', 'Sekolah Menengah'), ('SMA', 'Sekolah Atas'), ('D3', 'Diploma'), ('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3')])),
                ('pekerjaan_ayah', models.CharField(max_length=200, choices=[('TDK', 'Tidak Bekerja'), ('PN', 'Pegawai Negeri'), ('PS', 'Pegawai Swasta'), ('WS', 'Wira Swasta'), ('RT', 'Ibu Rumah Tangga')])),
                ('alamat', models.CharField(max_length=200)),
                ('no_telp', models.IntegerField(blank=True, null=True)),
                ('no_hp', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BioSiswa',
            fields=[
                ('NISL', models.IntegerField(primary_key=True, unique=True, serialize=False)),
                ('NISN', models.IntegerField(unique=True)),
                ('nama_depan', models.CharField(max_length=20)),
                ('nama_belakang', models.CharField(max_length=20)),
                ('tempat_lahir', models.CharField(max_length=20)),
                ('tanggal_lahir', models.DateField()),
                ('alamat', models.CharField(max_length=200)),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='bioortu',
            name='anak',
            field=models.ForeignKey(to='biodata.BioSiswa'),
        ),
    ]
