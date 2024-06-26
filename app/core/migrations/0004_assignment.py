# Generated by Django 3.2.25 on 2024-06-04 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20240602_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('classid', models.CharField(max_length=200)),
                ('duedate', models.DateTimeField()),
                ('filelocation', models.CharField(max_length=255)),
                ('instructions', models.CharField(max_length=200)),
                ('subjectID', models.CharField(max_length=100)),
                ('teacherID', models.CharField(max_length=100)),
                ('teacherName', models.CharField(max_length=100)),
            ],
        ),
    ]
