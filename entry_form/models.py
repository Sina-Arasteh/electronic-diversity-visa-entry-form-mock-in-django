from django.db import models


class MailingAddress(models.Model):
    in_care_of = models.CharField("In Care Of", max_length=33, blank=True)
    address_line_one = models.CharField("Address Line 1", max_length=33)
    address_line_two = models.CharField("Address Line 2", max_length=33, blank=True)
    city = models.CharField("City/Town", max_length=33)
    province = models.CharField("District/County/Province/State", max_length=33)
    zip_code = models.CharField("Postal Code/Zip Code", max_length=33, blank=True)
    country = models.CharField(max_length=40)


class Entrants(models.Model):
    last_name = models.CharField("Last/Family Name", max_length=33)
    first_name = models.CharField("First Name", max_length=33, blank=True)
    middle_name = models.CharField("Middle Name", max_length=33, blank=True)
    gender = models.CharField(max_length=6)
    birth_date = models.DateField("Birth Date", blank=True)
    birth_city = models.CharField("Birth City", max_length=33,blank=True)
    birth_country = models.CharField("Birth Country", max_length=40)
    eligibility_country = models.CharField("Eligibility Country", max_length=40, blank=True)
    entrant_photograph = models.ImageField("Entrant Photograph", upload_to="photographs")
    mailing_address = models.OneToOneField(MailingAddress, on_delete=models.CASCADE)
    residence_country = models.CharField("Residence Country", max_length=40)
    phone_number = models.CharField("Phone Number", max_length=33)
    email_address = models.EmailField("Email Address")
    education_level = models.CharField("Education Level", max_length=33)
    marital_status = models.CharField("Marital Status", max_length=85)
    children_number = models.PositiveSmallIntegerField()
    confirmation_number = models.CharField("Confirmation Number", max_length=16, blank=True)
    digital_signature = models.CharField("Digital Signature", max_length=40, blank=True)

