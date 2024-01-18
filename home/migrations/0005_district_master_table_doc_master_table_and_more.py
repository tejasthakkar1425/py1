# Generated by Django 4.2.3 on 2024-01-18 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_gstcharges'),
    ]

    operations = [
        migrations.CreateModel(
            name='district_master_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_id', models.IntegerField(default=0)),
                ('district_name', models.TextField()),
                ('state_id', models.IntegerField(default=0)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('created_by_user_id', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_by_user_id', models.IntegerField(blank=True, default=0, null=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'district_master',
            },
        ),
        migrations.CreateModel(
            name='doc_master_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_id', models.IntegerField(default=0)),
                ('doc_number', models.IntegerField(default=0)),
                ('doc_date', models.DateTimeField(auto_now_add=True)),
                ('LR_number', models.IntegerField(default=0)),
                ('gst_charges_id', models.IntegerField(blank=True, default=0, null=True)),
                ('net_amount', models.FloatField(default=0, null=True)),
                ('is_cancel', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'doc_master',
            },
        ),
        migrations.CreateModel(
            name='review_feedback_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_id', models.IntegerField(default=0)),
                ('user_id', models.IntegerField(default=0)),
                ('review_image', models.TextField()),
                ('review_decription', models.TextField()),
                ('review_star', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'review&feedback_master',
            },
        ),
        migrations.CreateModel(
            name='user_master_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_master_id', models.IntegerField(default=0)),
                ('user_email_id', models.TextField()),
                ('user_name', models.TextField()),
                ('user_password', models.TextField()),
            ],
            options={
                'db_table': 'user_master_master',
            },
        ),
        migrations.CreateModel(
            name='vehicle_master_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_id', models.IntegerField(default=0)),
                ('vehicle_name', models.TextField()),
                ('RC_book_number', models.TextField()),
                ('Reg_number', models.IntegerField(default=0)),
                ('capacity', models.FloatField(default=0, null=True)),
                ('insurance_from', models.DateTimeField(auto_now_add=True)),
                ('insurance_to', models.DateTimeField(auto_now_add=True)),
                ('insurance_company_name', models.TextField()),
                ('owner_name', models.TextField()),
            ],
            options={
                'db_table': 'vehicle_master',
            },
        ),
        migrations.CreateModel(
            name='vehicle_route_master_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_rout_id', models.IntegerField(default=0)),
                ('from_state_id', models.IntegerField(default=0)),
                ('to_state_id', models.IntegerField(default=0)),
                ('veh_rout_det', models.TextField()),
                ('veh_rout_drt_id', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'vehicle_rout_master',
            },
        ),
    ]
