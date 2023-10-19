from rest_framework import serializers
from .models import*


class CompanySerializer(serializers.ModelSerializer):
 class Meta:
  model=Company
  fields="__all__"

class BankSerializer(serializers.ModelSerializer):
 class Meta:
  model=Bank
  fields="__all__"

class ProjectSerializer(serializers.ModelSerializer):
 class Meta:
  model=Project
  fields="__all__"

class ClientSerializer(serializers.ModelSerializer):
 class Meta:
  model=Client
  fields="__all__"

class ProjectMilestoneSerializer(serializers.ModelSerializer):
 class Meta:
  model=ProjectMilestone
  fields="__all__"

class ProjectInvoicesSerializer(serializers.ModelSerializer):
 class Meta:
  model=ProjectInvoices
  fields="__all__"

class ProjectPaymentsSerializer(serializers.ModelSerializer):
 class Meta:
  model=ProjectPayments
  fields="__all__"

class CurencySerializer(serializers.ModelSerializer):
 class Meta:
  model=Curency
  fields="__all__"

class ParametersSerializer(serializers.ModelSerializer):
 class Meta:
  model=Parameters
  fields="__all__"

class MssandNdaSerializer(serializers.ModelSerializer):
 class Meta:
  model=MssandNda
  fields="__all__"