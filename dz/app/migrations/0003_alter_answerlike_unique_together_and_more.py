# Generated by Django 4.2.7 on 2023-11-15 20:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_alter_answer_creation_date_alter_answer_rating_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='answerlike',
            unique_together={('answer', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='questionlike',
            unique_together={('question', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='userlike',
            unique_together={('from_user', 'to_user')},
        ),
    ]