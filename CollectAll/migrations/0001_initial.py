# Generated by Django 4.2 on 2023-04-07 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_id', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('collection_favorite', models.CharField(max_length=10)),
                ('collection_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('collection_notes', models.TextField(max_length=1000)),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CollectionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_type', models.CharField(help_text='Enter a collection type (e.g. sport, music, etc.)', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_comment_id', models.IntegerField()),
                ('user_comment', models.TextField(max_length=1000)),
                ('collection_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='CollectAll.collection')),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CollectionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('item_notes', models.TextField(help_text='Enter a brief description of the item', max_length=1000)),
                ('item_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('collected_date', models.DateField()),
                ('item_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('collection_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_items', to='CollectAll.collection')),
                ('collection_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_type_items', to='CollectAll.collection')),
                ('parent_collection_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_items', to='CollectAll.collection')),
            ],
        ),
    ]
