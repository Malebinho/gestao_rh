# Generated by Django 2.2 on 2019-04-10 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0002_auto_20190410_1702'),
        ('registro_hora_extra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoraextra',
            name='funcionario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.Funcionario'),
            preserve_default=False,
        ),
    ]
