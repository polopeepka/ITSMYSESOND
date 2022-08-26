# Generated by Django 4.1 on 2022-08-25 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_bottle_address_remove_bottle_expired_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BottlesCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bottle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bottle_count', to='core.bottle')),
            ],
        ),
    ]