# Generated by Django 3.2.5 on 2021-07-12 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('receitas', '0003_rename_passos_receita_ingredientes'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
