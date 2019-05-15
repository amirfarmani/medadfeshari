# Generated by Django 2.1.5 on 2019-05-15 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190402_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_donate', models.CharField(max_length=200)),
                ('email_donate', models.CharField(max_length=200)),
                ('amount_donate', models.CharField(max_length=200)),
                ('transaction_code_donate', models.CharField(max_length=200)),
                ('transaction_status_donate', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Donate',
            },
        ),
        migrations.AlterField(
            model_name='myidea',
            name='idea_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 15, 16, 33, 51, 839854), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='myidea',
            name='idea_publisher',
            field=models.CharField(default='هم مدادفشاری', help_text='میتوانید نوشته خود را با یک نام خاص انتشار دهید', max_length=200, verbose_name='نگارنده'),
        ),
    ]