# Generated by Django 5.0.7 on 2024-11-11 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_reviews_owner'),
        ('users', '0004_profile_social_stackoverflow'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reviews',
            unique_together={('owner', 'project')},
        ),
    ]
