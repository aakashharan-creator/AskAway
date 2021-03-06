# Generated by Django 3.2.8 on 2021-10-23 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0002_question_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_code', models.CharField(max_length=8)),
                ('content', models.CharField(max_length=350)),
                ('answered', models.BooleanField(default=False)),
                ('topic', models.CharField(max_length=30)),
                ('answer', models.CharField(max_length=350)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
