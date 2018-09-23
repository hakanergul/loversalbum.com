# Generated by Django 2.1.1 on 2018-09-22 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ilan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=40)),
                ('metin', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=20)),
                ('soyad', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('ilan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='askilan.Ilan')),
            ],
        ),
    ]