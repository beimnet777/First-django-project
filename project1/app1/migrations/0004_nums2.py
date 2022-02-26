# Generated by Django 4.0.2 on 2022-02-23 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_nums_is_offer'),
    ]

    operations = [
        migrations.CreateModel(
            name='nums2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(null=True)),
                ('is_offer', models.BooleanField(default=False)),
                ('fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.nums')),
            ],
        ),
    ]