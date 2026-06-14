# Generated manually to remove unused submission timestamp.

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0005_simplify_timestamps_and_explanation_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practicesubmission',
            name='created_at',
        ),
    ]
