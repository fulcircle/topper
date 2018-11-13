# Generated by Django 2.1.3 on 2018-11-13 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('endpoint', models.URLField()),
                ('last_run', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('G', '✓ good'), ('E', '× error'), ('R', '~ running')], default='G', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('url', models.URLField(blank=True, max_length=2000, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('comments', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True, db_index=True)),
                ('status', models.CharField(choices=[('N', 'New'), ('O', 'Ok'), ('E', 'Error')], default='N', max_length=1)),
                ('top_ten', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='api.Service')),
            ],
            options={
                'verbose_name': 'story',
                'verbose_name_plural': 'stories',
                'ordering': ('-score', 'date'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='story',
            unique_together={('service', 'code', 'date')},
        ),
    ]