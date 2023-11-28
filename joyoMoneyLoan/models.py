from django.db import models

# Create your models here.
class NormalData(models.Model):
    home_loan = models.CharField(max_length=255)
    personal_loan = models.CharField(max_length=255)
    credit_cat = models.CharField(max_length=255)
    car_loan = models.CharField(max_length=255)
    testimonial1 = models.CharField(max_length=255)
    testimonial2 = models.CharField(max_length=255)
    testimonial3 = models.CharField(max_length=255)
    testimonial_name1 = models.CharField(max_length=255)
    testimonial_name2 = models.CharField(max_length=255)
    testimonial_name3 = models.CharField(max_length=255)
    image1 = models.CharField(max_length=255)
    image2 = models.CharField(max_length=255)
    image3 = models.CharField(max_length=255)
    image4 = models.CharField(max_length=255)
    image5 = models.CharField(max_length=255)
    image6 = models.CharField(max_length=255)

# models.py

class LoanApplication(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    application_no = models.CharField(max_length=255, unique=True, blank=True, null=True)
    salary = models.CharField(max_length=255)
    loan_type = models.CharField(max_length=255)
    employment_type_choices = [
        ('salaried', 'Salaried'),
        ('self_employed', 'Self Employed'),
    ]
    employment_type = models.CharField(max_length=15, choices=employment_type_choices)
    address = models.TextField()
    business_address = models.TextField()
    bank_name = models.CharField(max_length=255)
    account_type = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    ifsc_code = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)
    pan_no = models.CharField(max_length=10)
    adhar_no = models.CharField(max_length=12)
    dob = models.DateField()
    voter_id = models.CharField(max_length=255)
    three_month_salary = models.FileField(upload_to='loan_files/')
    itr = models.FileField(upload_to='loan_files/')
    income_proof = models.FileField(upload_to='loan_files/')
    registration_proof = models.FileField(upload_to='loan_files/')
    reference_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.application_no}"

class Email(models.Model):
    address = models.EmailField(unique=True)

    def __str__(self):
        return self.address

class Image(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Register(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    type_choices = [
        ('agent', 'Agent'),
        ('user', 'User'),
    ]
    type = models.CharField(max_length=10, choices=type_choices)

    def __str__(self):
        return self.email