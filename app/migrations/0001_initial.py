# Generated by Django 2.0.1 on 2018-02-07 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa')),
                ('description', models.CharField(max_length=10000, verbose_name='Opis')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_code', models.CharField(max_length=800000, verbose_name='Kod programu napisany w Python')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='Data dodania')),
                ('algorithm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Algorithm')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=30)),
                ('input_data', models.CharField(max_length=800000, verbose_name='Dane wejściowe')),
                ('output_data', models.CharField(max_length=800000, verbose_name='Dane wyjściowe')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='Data dodania')),
                ('algorithm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Algorithm')),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('result', models.CharField(max_length=10)),
                ('solution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Solution')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Test')),
            ],
        ),
    ]
