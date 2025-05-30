# Generated by Django 5.2 on 2025-05-02 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('summary', models.TextField()),
                ('type', models.TextField(choices=[('income', 'Income'), ('expense', 'Expense'), ('lend', 'Lend'), ('borrow', 'Borrow')])),
                ('amount', models.PositiveIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='categories.category')),
                ('person', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.person')),
            ],
        ),
    ]
