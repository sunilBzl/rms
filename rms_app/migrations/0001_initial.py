# Generated by Django 3.2.9 on 2021-11-29 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=80)),
                ('rollnumber', models.IntegerField(unique=True)),
                ('student_class', models.IntegerField()),
                ('student_age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=100)),
                ('students', models.ManyToManyField(to='rms_app.Student')),
                ('teachers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='rms_app.teacher')),
            ],
        ),
    ]
