# Generated by Django 2.0.9 on 2018-12-24 20:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('pic_link', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Oder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quontity', models.IntegerField()),
                ('note', models.TextField()),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('deliverd_time', models.DateTimeField(blank=True, null=True)),
                ('is_delivered', models.BooleanField(default=False)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='rio.Item')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_email', models.CharField(max_length=50)),
                ('user_phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='oder',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='username', to='rio.User'),
        ),
    ]
