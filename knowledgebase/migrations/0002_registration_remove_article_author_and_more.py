# knowledgebase/migrations/0002_add_name_field.py
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('knowledgebase', '0001_initial'),  # Adjust this to the previous migration
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='name',
            field=models.CharField(max_length=100, default=''),
            preserve_default=False,
        ),
    ]
