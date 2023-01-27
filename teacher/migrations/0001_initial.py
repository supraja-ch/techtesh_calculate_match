# Generated by Django 3.1.7 on 2021-03-07 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=56)),
                ('last_name', models.CharField(max_length=56)),
                ('email_address', models.EmailField(max_length=254)),
                ('profile_picture', models.ImageField(default='default.jpg', upload_to='teacher')),
                ('mobile_number', models.IntegerField()),
                ('room_number', models.CharField(max_length=10)),
                ('subject_taught', models.CharField(max_length=256)),
                ('subject_count', models.PositiveIntegerField()),
                ('created', models.DateField()),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
