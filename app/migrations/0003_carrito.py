# Generated by Django 4.0.5 on 2022-06-28 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.marca')),
            ],
        ),
    ]
