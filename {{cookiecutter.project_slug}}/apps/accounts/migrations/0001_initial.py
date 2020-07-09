# Generated by Django 2.2.12 on 2020-07-09 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='e-mail')),
                ('is_active', models.BooleanField(blank=True, default=True, verbose_name='is active')),
                ('is_delete', models.BooleanField(blank=True, default=False, verbose_name='is delete')),
                ('is_staff', models.BooleanField(blank=True, default=False, verbose_name='is staff')),
                ('first_name', models.CharField(max_length=128, verbose_name='first name')),
                ('last_name', models.CharField(max_length=128, verbose_name='last name')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]
