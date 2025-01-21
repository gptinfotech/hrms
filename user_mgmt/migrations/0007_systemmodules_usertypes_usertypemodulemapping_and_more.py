# Generated by Django 5.1.4 on 2025-01-21 09:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_mgmt', '0006_rename_id_users_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemModules',
            fields=[
                ('system_module_id', models.AutoField(primary_key=True, serialize=False)),
                ('system_module_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('module_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserTypes',
            fields=[
                ('user_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_type', models.CharField(max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserTypeModuleMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_mgmt.systemmodules')),
                ('user_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_mgmt.usertypes')),
            ],
        ),
        migrations.AlterField(
            model_name='users',
            name='user_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_mgmt.usertypes'),
        ),
    ]
