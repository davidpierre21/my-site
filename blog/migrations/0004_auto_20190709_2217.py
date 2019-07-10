# Generated by Django 2.2.3 on 2019-07-10 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.PositiveIntegerField(choices=[(0, 'Draft'), (1, 'Published'), (2, 'Archived')], default=0),
        ),
    ]