# Generated by Django 5.0.7 on 2024-07-11 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diplom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Protokols',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.PositiveSmallIntegerField(default=0, help_text='скидка, %:')),
                ('oplata', models.DecimalField(decimal_places=2, default=0, help_text='Оплата, грн:', max_digits=7)),
                ('finresult', models.TimeField(blank=True, default=None, help_text='Финишный результат:')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Diplom.agecategory')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diplom.events')),
                ('runner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diplom.runners')),
            ],
        ),
    ]