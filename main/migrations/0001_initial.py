# Generated by Django 5.1.6 on 2025-02-25 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kutubxonachi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('ish_vaqti', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('jins', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], max_length=10)),
                ('tugilgan_sana', models.DateField()),
                ('kitob_soni', models.IntegerField(default=0)),
                ('tirik', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Talaba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('guruh', models.CharField(max_length=50)),
                ('kurs', models.IntegerField()),
                ('kitob_soni', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('janr', models.CharField(max_length=100)),
                ('sahifa', models.IntegerField()),
                ('muallif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.muallif')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('olingan_sana', models.DateField()),
                ('qaytarish_sana', models.DateField()),
                ('kitob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.kitob')),
                ('kutubxonachi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.kutubxonachi')),
                ('talaba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.talaba')),
            ],
        ),
    ]
