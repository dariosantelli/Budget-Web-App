# Generated by Django 2.1.1 on 2019-11-29 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_auto_20191124_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
