from django.db import models


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


# Create your models here.
class Company(models.Model):
 name=models.CharField(max_length=50)
 companyLogo=models.ImageField()
 eamailID= models.EmailField()
 contactNumber=models.IntegerField()
 GSTNumber=models.IntegerField()
 PANNumber=models.IntegerField()
 LUTNumber=models.IntegerField()
 adress=models.TextField()
 country=models.BinaryField()
 ID=models.AutoField(primary_key=True)
 image=models.ImageField(upload_to="my_picture",blank=True)
 

class Bank(models.Model):
 BankName=models.CharField(max_length=50)
 BankId=models.CharField(max_length=50)
 BankAddress=models.TextField()
 AccountNumber=models.IntegerField()
 Branchname=models.CharField(max_length=50)
 IFSCCode=models.IntegerField()
 SwiftCode=models.IntegerField()
 PaypalID=models.IntegerField()
 ID=models.AutoField(primary_key=True)
class Project(models.Model):

 ID=models.AutoField(primary_key=True)
 ClientID=models.IntegerField()
 PointofContact=models.IntegerField()
 Solution=models.IntegerField()
 Service=models.IntegerField()
 ProjectName=models.TextField()
 PORef=models.CharField(max_length=50)
 StartDate=models.DateTimeField()
 EndDate=models.DateTimeField()
 Currency=models.IntegerField()
 ProjectValue=models.IntegerField()
 Projectid=models.CharField(max_length=50)
 projectStatus=models.CharField(max_length=50)
 projectuploadpdf=models.CharField(max_length=500)

ser='SA'
solu='DI'
lastproid='SU/AI/003'
output='SA/DI/004'


 
class Client(models.Model):
 clientCompanyName=models.CharField(max_length=50)
 pointofcontact=models.IntegerField()
 emailid=models.EmailField()
 GstNumber=models.IntegerField()
 Address=models.CharField(max_length=50)
 countrycode=models.IntegerField()
 ClientId=models.AutoField(primary_key=True)

class ProjectMilestone(models.Model):
 projectid=models.IntegerField()
 MilestoneDate=models.DateField()
 Milestonevalue=models.IntegerField()
 Milestoneupdate=models.DateField()
 


class ProjectInvoices(models.Model):
 milestoneid=models.IntegerField()
 milestoneNoteRemark=models.IntegerField()
 milestonehours=models.TimeField()
 milestoneValue=models.IntegerField()
 convertionrate=models.IntegerField()
 status=models.IntegerField()
 Invoiceno=models.CharField(max_length=50)
 Invoicedate=models.DateField()

class ProjectPayments(models.Model):
 milestoneid=models.AutoField(primary_key=True)
 paymentDate=models.DateField()
 paymentValue=models.IntegerField()
 PaymentNote=models.CharField(max_length=50)


class Curency(models.Model):
 Rate=models.IntegerField()
 RateonDate=models.IntegerField()


class Parameters(models.Model):
 parameterid=models.IntegerField()
 Description=models.CharField(max_length=50)
 CurrencyRate=models.IntegerField()


class MssandNda(models.Model):
 id=models.AutoField(primary_key=True)
 Clientname=models.CharField(max_length=50)
 startdate=models.DateField()
 Enddate=models.DateField()
 Documentid=models.IntegerField()
 status=models.CharField(max_length=50)
 docupload=models.CharField(max_length=500)





  
 def save(self, request):
        self.Project_number = self.Project_number + 1
        super().save(request)  