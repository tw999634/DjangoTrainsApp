# Generated manually for the practice app structure updated by the user.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_alter_practicecontent_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practicecontent',
            name='goal',
        ),
        migrations.RemoveField(
            model_name='practicecontent',
            name='is_published',
        ),
        migrations.AlterField(
            model_name='practicecontent',
            name='concept',
            field=models.CharField(max_length=80, verbose_name='学習キーワード'),
        ),
        migrations.AlterField(
            model_name='practicecontent',
            name='order',
            field=models.IntegerField(default=1, verbose_name='表示順'),
        ),
        migrations.AddField(
            model_name='practicecontent',
            name='required_patterns',
            field=models.TextField(blank=True, help_text='1行につき1つの正規表現を書きます。すべて一致した場合に正解になります。', verbose_name='正解判定用パターン'),
        ),
    ]
