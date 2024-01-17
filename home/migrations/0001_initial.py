# Generated by Django 4.2.3 on 2024-01-17 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='state_master_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_id', models.IntegerField(default=0)),
                ('stat_name', models.TextField()),
                ('Description', models.CharField(blank=True, max_length=50, null=True)),
                ('created_by_user_id', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_by_user_id', models.IntegerField(blank=True, default=0, null=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'state_master_table',
            },
        ),
    ]
