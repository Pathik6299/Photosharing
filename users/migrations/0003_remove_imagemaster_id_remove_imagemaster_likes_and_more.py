# Generated by Django 4.1.4 on 2022-12-11 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_imagemaster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemaster',
            name='id',
        ),
        migrations.RemoveField(
            model_name='imagemaster',
            name='likes',
        ),
        migrations.AddField(
            model_name='imagemaster',
            name='ImageID',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='LikeMaster',
            fields=[
                ('LikeID', models.AutoField(primary_key=True, serialize=False)),
                ('ImageID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.imagemaster')),
                ('UserID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
