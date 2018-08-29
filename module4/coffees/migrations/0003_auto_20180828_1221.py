# Generated by Django 2.0.8 on 2018-08-28 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffees', '0002_auto_20180828_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coffee',
            name='flavour',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coffee',
            name='name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coffee',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coffee',
            name='processing',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coffee',
            name='rosat',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]