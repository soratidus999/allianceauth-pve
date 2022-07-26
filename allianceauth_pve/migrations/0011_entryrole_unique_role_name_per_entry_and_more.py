# Generated by Django 4.0.5 on 2022-06-26 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allianceauth_pve', '0010_rolesetup_generalrole_rotation_roles_setups'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='entryrole',
            constraint=models.UniqueConstraint(fields=('entry', 'name'), name='unique_role_name_per_entry'),
        ),
        migrations.AddConstraint(
            model_name='generalrole',
            constraint=models.UniqueConstraint(fields=('setup', 'name'), name='unique_role_name_per_setup'),
        ),
    ]
