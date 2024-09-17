# Generated by Django 5.1.1 on 2024-09-17 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsers', '0004_news_shares'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")),
            ],
            options={
                'verbose_name': 'E-mail',
                'verbose_name_plural': 'E-maillar',
            },
        ),
    ]
