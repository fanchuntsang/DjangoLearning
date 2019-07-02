# Generated by Django 2.1.7 on 2019-03-02 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collect', '0002_comment_comment_in_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collect',
            fields=[
                ('collect_id', models.AutoField(primary_key=True, serialize=False)),
                ('collect_type', models.IntegerField()),
                ('collect_in_id', models.IntegerField(default='1')),
                ('collect_flag', models.BooleanField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]