# Generated by Django 4.0.2 on 2022-02-01 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Water',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drunk', models.IntegerField(choices=[(0, 'None'), (1, 'Little'), (2, 'Some'), (3, 'Lots'), (4, 'Perfect')], default=0)),
            ],
        ),
    ]