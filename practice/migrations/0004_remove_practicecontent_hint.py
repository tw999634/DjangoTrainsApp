# Generated manually to remove the hint field from PracticeContent.

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0003_remove_goal_is_published_add_required_patterns'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practicecontent',
            name='hint',
        ),
    ]
