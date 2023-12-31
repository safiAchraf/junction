# Generated by Django 4.2.6 on 2023-10-05 23:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_instructor', models.BooleanField(default=False)),
                ('is_learner', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='chapitres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapitre_name', models.CharField(max_length=20)),
                ('chapitre_description', models.CharField(max_length=100)),
                ('chapitre_duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.CharField(max_length=100)),
                ('video_title', models.CharField(max_length=20)),
                ('chapitre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='junction.chapitres')),
            ],
        ),
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_title', models.CharField(max_length=20)),
                ('quiz_description', models.CharField(max_length=100)),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=20)),
                ('chapitre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='junction.chapitres')),
            ],
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=20)),
                ('course_description', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('course_duration', models.IntegerField()),
                ('course_price', models.IntegerField()),
                ('instructor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='child_learner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_name', models.CharField(max_length=20)),
                ('child_age', models.IntegerField()),
                ('child_level', models.IntegerField()),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='child_enrolled',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_progress', models.IntegerField()),
                ('child_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='junction.child_learner')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='junction.course')),
            ],
        ),
        migrations.AddField(
            model_name='chapitres',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='junction.course'),
        ),
        migrations.CreateModel(
            name='adult_enrolled',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_progress', models.IntegerField()),
                ('adult_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='junction.course')),
            ],
        ),
    ]
