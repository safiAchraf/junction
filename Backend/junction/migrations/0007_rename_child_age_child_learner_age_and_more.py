# Generated by Django 4.2.6 on 2023-10-06 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('junction', '0006_alter_child_learner_child_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='child_learner',
            old_name='child_age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='child_learner',
            old_name='child_level',
            new_name='level',
        ),
        migrations.RenameField(
            model_name='child_learner',
            old_name='child_name',
            new_name='name',
        ),
    ]
