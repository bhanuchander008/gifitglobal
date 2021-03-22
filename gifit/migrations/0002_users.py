# Generated by Django 3.0.5 on 2021-03-22 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=250)),
                ('LastName', models.CharField(max_length=250)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('dob', models.CharField(max_length=250)),
                ('nationality', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('locked', models.CharField(max_length=250)),
                ('failed_attempts', models.IntegerField()),
                ('point_balance', models.FloatField()),
                ('lastlogin_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]