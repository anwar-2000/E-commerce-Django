# Generated by Django 4.1.6 on 2023-02-20 22:04

import Utilisateurs.manager
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Utilisateurs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='utilisateur',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='utilisateur',
            managers=[
                ('objects', Utilisateurs.manager.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='mot_de_passe',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='username',
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='email_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='forgot_password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='mobile',
            field=models.CharField(default='', max_length=14),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='password',
            field=models.CharField(default='', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
