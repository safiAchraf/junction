# Generated by Django 4.2.6 on 2023-10-07 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('junction', '0012_interests_user_interests_remove_chapitres_course_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='child_learner',
            name='child_score',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='child_learner',
            name='child_streak',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
