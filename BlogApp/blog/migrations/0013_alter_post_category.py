
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_merge_0011_alter_post_category_0011_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default='coding', on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
        ),
    ]
