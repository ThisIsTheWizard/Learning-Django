# Generated by Django 3.0.5 on 2020-04-08 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=99)),
                ('img', models.ImageField(upload_to='assets/img/uploads/')),
                ('desc', models.TextField()),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('new_price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
