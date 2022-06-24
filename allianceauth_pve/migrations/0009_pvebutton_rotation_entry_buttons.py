# Generated by Django 4.0.5 on 2022-06-24 11:23

import django.core.validators
from django.db import migrations, models


def default_buttons(apps, schema_editor):
    PveButton = apps.get_model('allianceauth_pve.PveButton')
    Rotation = apps.get_model('allianceauth_pve.Rotation')

    PveButton.objects.bulk_create([
        PveButton(text='Drifter', amount=300000000),
        PveButton(text='Garrison', amount=253400000),
        PveButton(text='Stronghold', amount=234900000),
        PveButton(text='Citadel', amount=310100000),
        PveButton(text='Bastion', amount=445600000),
        PveButton(text='The Mirror', amount=363200000),
    ])

    for rotation in Rotation.objects.all():
        rotation.entry_buttons.set(PveButton.objects.all())


class Migration(migrations.Migration):

    dependencies = [
        ('allianceauth_pve', '0008_auto_20220424_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='PveButton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=64, unique=True)),
                ('amount', models.FloatField(validators=[django.core.validators.MinValueValidator(-1000000000000), django.core.validators.MaxValueValidator(1000000000000)])),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.AddField(
            model_name='rotation',
            name='entry_buttons',
            field=models.ManyToManyField(help_text='Button to be shown in the Entry form.', related_name='+', to='allianceauth_pve.pvebutton'),
        ),
        migrations.RunPython(default_buttons, migrations.RunPython.noop),
    ]
