# Generated by Django 3.0.3 on 2022-11-15 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyHomePage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myserviceprojectlist',
            name='img',
            field=models.ImageField(blank=True, default='MyServiceProject/default.png', help_text='若没有选择封面，则使用默认封面', null=True, upload_to='MyServiceProject/', verbose_name='服务封面'),
        ),
    ]
