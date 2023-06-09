# Generated by Django 4.1.7 on 2023-05-04 15:56

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, validators=[users.validators.not_rambler_email]),
        ),
    ]
