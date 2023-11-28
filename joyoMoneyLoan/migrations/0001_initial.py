# Generated by Django 4.2.4 on 2023-11-28 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LoanApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=255)),
                ('application_no', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('salary', models.CharField(max_length=255)),
                ('loan_type', models.CharField(max_length=255)),
                ('employment_type', models.CharField(choices=[('salaried', 'Salaried'), ('self_employed', 'Self Employed')], max_length=15)),
                ('address', models.TextField()),
                ('business_address', models.TextField()),
                ('bank_name', models.CharField(max_length=255)),
                ('account_type', models.CharField(max_length=255)),
                ('account_number', models.CharField(max_length=255)),
                ('ifsc_code', models.CharField(max_length=255)),
                ('branch_name', models.CharField(max_length=255)),
                ('remark', models.CharField(max_length=255)),
                ('pan_no', models.CharField(max_length=10)),
                ('adhar_no', models.CharField(max_length=12)),
                ('dob', models.DateField()),
                ('voter_id', models.CharField(max_length=255)),
                ('three_month_salary', models.FileField(upload_to='loan_files/')),
                ('itr', models.FileField(upload_to='loan_files/')),
                ('income_proof', models.FileField(upload_to='loan_files/')),
                ('registration_proof', models.FileField(upload_to='loan_files/')),
                ('reference_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NormalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_loan', models.CharField(max_length=255)),
                ('personal_loan', models.CharField(max_length=255)),
                ('credit_cat', models.CharField(max_length=255)),
                ('car_loan', models.CharField(max_length=255)),
                ('testimonial1', models.CharField(max_length=255)),
                ('testimonial2', models.CharField(max_length=255)),
                ('testimonial3', models.CharField(max_length=255)),
                ('testimonial_name1', models.CharField(max_length=255)),
                ('testimonial_name2', models.CharField(max_length=255)),
                ('testimonial_name3', models.CharField(max_length=255)),
                ('image1', models.CharField(max_length=255)),
                ('image2', models.CharField(max_length=255)),
                ('image3', models.CharField(max_length=255)),
                ('image4', models.CharField(max_length=255)),
                ('image5', models.CharField(max_length=255)),
                ('image6', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('agent', 'Agent'), ('user', 'User')], max_length=10)),
            ],
        ),
    ]