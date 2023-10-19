
from django.shortcuts import render
# from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import *
from.models import*
from.serializers import*
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework import request
from datetime import datetime
# from datetime import datetime



# Create your views here.
class CompanyList(GenericAPIView,ListModelMixin,CreateModelMixin):
   queryset=Company.objects.all()
   serializer_class=CompanySerializer
   permission_classes=permissions.AllowAny,
   def get(self,request):
      return self.list(request)
   def post(self,request):
      return self.create(request)
class Companydel(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
   queryset=Company.objects.all()
   serializer_class=CompanySerializer
   permission_classes=(permissions.AllowAny,)
   def put(self,request,*args,**kwargs):
      return self.update(request,*args,**kwargs)
   def delete(self,request,*args,**kwargs):
      return self.destroy(request,*args,**kwargs)
   def get(self,request,*args,**kwargs):
      return self.retrieve(request,*args,**kwargs)



class BankList(GenericAPIView,ListModelMixin,CreateModelMixin):
   queryset=Bank.objects.all()
   serializer_class=BankSerializer
   permission_classes=permissions.AllowAny,
   def get(self,request):
      return self.list(request)
   def post(self,request):
      return self.create(request)
class Bankdel(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
   queryset=Bank.objects.all()
   serializer_class=BankSerializer
   permission_classes=(permissions.AllowAny,)
   def put(self,request,*args,**kwargs):
      return self.update(request,*args,**kwargs)
   def delete(self,request,*args,**kwargs):
      return self.destroy(request,*args,**kwargs)
   def get(self,request,*args,**kwargs):
      return self.retrieve(request,*args,**kwargs)


class ProjectList(GenericAPIView,ListModelMixin,CreateModelMixin):
   queryset=Project.objects.all()
   serializer_class=ProjectSerializer
   permission_classes=permissions.AllowAny,
   def get(self,request):
      return self.list(request)
   def post(self,request):
      obj=Project.objects.all().values().last()
      old_num=str(obj['Projectid']).split('/')[-1]
      # a='3/2/1'.split('/')[2]
      b=1
      k=int(old_num)+1
      print(k)

      solu=request.data['Solution']
      ser=request.data['Service']
      prop=request.data['Projectid']
      okji=(str(solu)+'/'+str(ser)+'/'+str(prop))
      request.data['Projectid']=okji
      print(okji)
      return self.create(request)

   
class Projectdel(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
   queryset=Project.objects.all()
   serializer_class=ProjectSerializer
   permission_classes=(permissions.AllowAny,)
   def put(self,request,*args,**kwargs):
      return self.update(request,*args,**kwargs)
   def delete(self,request,*args,**kwargs):
      return self.destroy(request,*args,**kwargs)
   def get(self,request,*args,**kwargs):
      return self.retrieve(request,*args,**kwargs)


class ClientList(GenericAPIView,ListModelMixin,CreateModelMixin):
   queryset=Client.objects.all()
   serializer_class=ClientSerializer
   permission_classes=permissions.AllowAny,
   def get(self,request):
      return self.list(request)
   def post(self,request):
      return self.create(request)
class Clientdel(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
   queryset=Client.objects.all()
   serializer_class=ClientSerializer
   permission_classes=(permissions.AllowAny,)
   def put(self,request,*args,**kwargs):
      return self.update(request,*args,**kwargs)
   def delete(self,request,*args,**kwargs):
      return self.destroy(request,*args,**kwargs)
   def get(self,request,*args,**kwargs):
      return self.retrieve(request,*args,**kwargs)

class ProjectMilestoneList(GenericAPIView,ListModelMixin,CreateModelMixin):
   queryset=ProjectMilestone.objects.all()
   serializer_class=ProjectMilestoneSerializer
   permission_classes=permissions.AllowAny,
   def get(self,request):
      return self.list(request)
   def post(self,request):
      return self.create(request)
class ProjectMilestonedel(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
   queryset=ProjectMilestone.objects.all()
   serializer_class=ProjectMilestoneSerializer
   permission_classes=(permissions.AllowAny,)
   def put(self,request,*args,**kwargs):
      return self.update(request,*args,**kwargs)
   def delete(self,request,*args,**kwargs):
      return self.destroy(request,*args,**kwargs)
   def get(self,request,*args,**kwargs):
      return self.retrieve(request,*args,**kwargs)


import datetime

class ProjectInvoicesList(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = ProjectInvoices.objects.all()
    serializer_class = ProjectInvoicesSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        obj = ProjectInvoices.objects.all().values().last()
        old, okj = str(obj['Invoiceno']).split('/')
        print(old, okj)
        a = datetime.datetime.strptime(old, '%Y-%m-%d')
        print(type(a))
        print(a.strftime('%d-%m-%Y'))

        a = a.strftime('%d-%m-%Y')
        print(a)

        b = datetime.date.today()
        print(b.strftime('%d-%m-%Y'))
        print(b)

        if a != b:
            l = a
            print(l)
            c = int(okj) + 1
            print(c)
            z = str(l) + '/' + str(c)
            print(z)
            request.data['Invoiceno'] = z
        else:
            d = str(b) + '/' + '001'
            print(d)
            request.data['Invoiceno'] = d

        return self.create(request)





class ProjectInvoicesdel(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
   queryset=ProjectInvoices.objects.all()
   serializer_class=ProjectInvoicesSerializer
   permission_classes=(permissions.AllowAny,)
   def put(self,request,*args,**kwargs):
      return self.update(request,*args,**kwargs)
   def delete(self,request,*args,**kwargs):
      return self.destroy(request,*args,**kwargs)
   def get(self,request,*args,**kwargs):
      return self.retrieve(request,*args,**kwargs)

class ProjectPaymentsList(GenericAPIView,ListModelMixin,CreateModelMixin):
   queryset=ProjectPayments.objects.all()
   serializer_class=ProjectPaymentsSerializer
   permission_classes=permissions.AllowAny,
   def get(self,request):
      return self.list(request)
   def post(self,request):
      return self.create(request)
class ProjectPaymentsdel(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
   queryset=ProjectPayments.objects.all()
   serializer_class=ProjectPaymentsSerializer
   permission_classes=(permissions.AllowAny,)
   def put(self,request,*args,**kwargs):
      return self.update(request,*args,**kwargs)
   def delete(self,request,*args,**kwargs):
      return self.destroy(request,*args,**kwargs)
   def get(self,request,*args,**kwargs):
      return self.retrieve(request,*args,**kwargs)


class CurencyList(GenericAPIView,ListModelMixin,CreateModelMixin):
   queryset=Curency.objects.all()
   serializer_class=CurencySerializer
   permission_classes=permissions.AllowAny,
   def get(self,request):
      return self.list(request)
   def post(self,request):
      return self.create(request)
class Curencydel(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
   queryset=Curency.objects.all()
   serializer_class=CurencySerializer
   permission_classes=(permissions.AllowAny,)
   def put(self,request,*args,**kwargs):
      return self.update(request,*args,**kwargs)
   def delete(self,request,*args,**kwargs):
      return self.destroy(request,*args,**kwargs)
   def get(self,request,*args,**kwargs):
      return self.retrieve(request,*args,**kwargs)


class ParametersList(GenericAPIView,ListModelMixin,CreateModelMixin):
   queryset=Parameters.objects.all()
   serializer_class=ParametersSerializer
   permission_classes=permissions.AllowAny,
   def get(self,request):
      return self.list(request)
   def post(self,request):
      return self.create(request)
   
   
class Parametersdel(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
   queryset=Parameters.objects.all()
   serializer_class=ParametersSerializer
   permission_classes=(permissions.AllowAny,)
   def put(self,request,*args,**kwargs):
      return self.update(request,*args,**kwargs)
   def delete(self,request,*args,**kwargs):
      return self.destroy(request,*args,**kwargs)
   def get(self,request,*args,**kwargs):
      return self.retrieve(request,*args,**kwargs)

class MssandNdaList(GenericAPIView,ListModelMixin,CreateModelMixin):
   queryset=MssandNda.objects.all()
   serializer_class=MssandNdaSerializer
   permission_classes=permissions.AllowAny,
   def get(self,request):
      return self.list(request)
   def post(self,request):
      return self.create(request)
class MssandNdadel(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
   queryset=MssandNda.objects.all()
   serializer_class=MssandNdaSerializer
   permission_classes=(permissions.AllowAny,)
   def put(self,request,*args,**kwargs):
      return self.update(request,*args,**kwargs)
   def delete(self,request,*args,**kwargs):
      return self.destroy(request,*args,**kwargs)
   def get(self,request,*args,**kwargs):


      return self.retrieve(request,*args,**kwargs)

