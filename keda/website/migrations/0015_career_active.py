# Generated by Django 4.1.6 on 2023-02-02 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_alter_career_slug_career'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='active',
            field=models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0),
        ),
    ]
