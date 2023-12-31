# Generated by Django 5.0 on 2023-12-22 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_fueling'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('wash_type', models.CharField(choices=[('A', 'Automated'), ('S', 'Self-Service')], default=0, max_length=1)),
            ],
        ),
        migrations.AlterModelOptions(
            name='fueling',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='fueling',
            name='gas_type',
            field=models.CharField(choices=[('U', 'Unleaded'), ('P', 'Unleaded Plus'), ('R', 'Premium Unleaded')], default='U', max_length=1),
        ),
        migrations.AddField(
            model_name='car',
            name='car_wash',
            field=models.ManyToManyField(to='main_app.wash'),
        ),
    ]
