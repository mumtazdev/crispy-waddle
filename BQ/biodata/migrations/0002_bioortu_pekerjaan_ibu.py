# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bioortu',
            name='pekerjaan_ibu',
            field=models.CharField(default='Ibu Rumah Tangga', max_length=200, choices=[('TDK', 'Tidak Bekerja'), ('PN', 'Pegawai Negeri'), ('PS', 'Pegawai Swasta'), ('WS', 'Wira Swasta'), ('RT', 'Ibu Rumah Tangga')]),
            preserve_default=False,
        ),
    ]
