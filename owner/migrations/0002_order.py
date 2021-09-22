# Generated by Django 3.2.6 on 2021-09-02 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=120)),
                ('status', models.CharField(choices=[('delivered', 'delivered'), ('cancel', 'cancel'), ('intransit', 'intransit'), ('ordered', 'ordered')], default='ordered', max_length=20)),
                ('phone_number', models.CharField(max_length=10)),
                ('delivery_date', models.DateField(null=True)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.book')),
            ],
        ),
    ]
