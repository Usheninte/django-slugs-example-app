# Generated by Django 2.1.7 on 2019-02-15 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_articlepkandslug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleUniqueSlug',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.Article')),
                ('slug', models.SlugField(default='', editable=False, max_length=100)),
            ],
            bases=('blog.article',),
        ),
    ]
