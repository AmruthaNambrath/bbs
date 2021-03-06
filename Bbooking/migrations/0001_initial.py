# Generated by Django 4.0.2 on 2022-02-09 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Andra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passname', models.CharField(default='', max_length=30)),
                ('froms', models.CharField(default='', max_length=30)),
                ('to', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.IntegerField()),
                ('b_id', models.IntegerField(default='')),
                ('pass1', models.CharField(default='', max_length=300)),
                ('pass2', models.CharField(default='', max_length=300)),
                ('pass3', models.CharField(default='', max_length=300)),
                ('pass4', models.CharField(default='', max_length=300)),
                ('pass5', models.CharField(default='', max_length=300)),
                ('date', models.DateTimeField()),
                ('rate', models.IntegerField()),
                ('date_now', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busname', models.CharField(max_length=30)),
                ('froms', models.CharField(max_length=30)),
                ('to', models.CharField(max_length=30)),
                ('fare', models.IntegerField()),
                ('state', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
                ('duration', models.IntegerField(max_length=24)),
                ('frequency', models.IntegerField()),
                ('b_id', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='karnataka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passname', models.CharField(default='', max_length=30)),
                ('froms', models.CharField(default='', max_length=30)),
                ('to', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Kerala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passname', models.CharField(default='', max_length=30)),
                ('froms', models.CharField(default='', max_length=30)),
                ('to', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Punjab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passname', models.CharField(default='', max_length=30)),
                ('froms', models.CharField(default='', max_length=30)),
                ('to', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TamilNadu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passname', models.CharField(default='', max_length=30)),
                ('froms', models.CharField(default='', max_length=30)),
                ('to', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
