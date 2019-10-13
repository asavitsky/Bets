# Generated by Django 2.2.3 on 2019-09-30 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('pl1', models.CharField(max_length=200)),
                ('pl2', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MainMarket_for_graphs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('bwin', models.FloatField()),
                ('onexstavka', models.FloatField()),
                ('fonbet', models.FloatField()),
                ('tennesi', models.FloatField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='odds.Event')),
            ],
        ),
        migrations.CreateModel(
            name='MainMarket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cf1', models.FloatField()),
                ('cfX', models.CharField(max_length=200)),
                ('cf2', models.FloatField()),
                ('ref', models.URLField()),
                ('bmk', models.CharField(max_length=200)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='odds.Event')),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='odds.Sport')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='League',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='odds.League'),
        ),
    ]
