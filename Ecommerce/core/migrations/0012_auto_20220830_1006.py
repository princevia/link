# Generated by Django 2.2.4 on 2022-08-30 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20220818_2234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ('-timestamp',)},
        ),
        migrations.AddField(
            model_name='payment',
            name='paystack_ref_id',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
