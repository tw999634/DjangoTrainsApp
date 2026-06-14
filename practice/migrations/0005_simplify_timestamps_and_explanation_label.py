# Generated manually to simplify timestamp fields and align the explanation label.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0004_remove_practicecontent_hint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practicecontent',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='practicecontent',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='practiceprogress',
            name='completed_at',
        ),
        migrations.RemoveField(
            model_name='practiceprogress',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='practicecontent',
            name='explanation',
            field=models.TextField(verbose_name='詳細'),
        ),
    ]
