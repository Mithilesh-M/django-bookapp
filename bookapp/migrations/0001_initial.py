# Generated by Django 3.2 on 2021-04-22 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name', max_length=200)),
                ('bio', models.TextField(help_text='Enter bio', max_length=500)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter genre name', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter genre name', max_length=200)),
                ('address', models.CharField(help_text='Enter address', max_length=500)),
                ('description', models.TextField(help_text='Enter description', max_length=500)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter book title', max_length=200)),
                ('isbn', models.UUIDField(unique=True)),
                ('no_of_page', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='Enter no.of page')),
                ('cover_image', models.ImageField(upload_to='')),
                ('description', models.TextField(help_text='Enter description', max_length=500)),
                ('published_date', models.DateField()),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookapp.author')),
                ('genre', models.ManyToManyField(to='bookapp.Genre')),
                ('publisher', models.ManyToManyField(to='bookapp.Publisher')),
            ],
        ),
    ]
