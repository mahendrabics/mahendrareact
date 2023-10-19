
from django.contrib import admin
from django.urls import path, include
from.views import*

urlpatterns =[

    path('CompanyList/',CompanyList.as_view()),
   
    path('Companydel/<int:pk>/',Companydel.as_view()),

    


    path('BankList/',BankList.as_view()),
   
    path('Bankdel/<int:pk>/',Bankdel.as_view()),





    path('ProjectList/',ProjectList.as_view()),
   
    path('Projectdel/<int:pk>/',Projectdel.as_view()),




    path('ClientList/',ClientList.as_view()),
   
    path('Clientdel/<int:pk>/',Clientdel.as_view()),





    path('Project/',ProjectMilestoneList.as_view()),
   
    path('Milestonedel/<int:pk>/',ProjectMilestonedel.as_view()),





    path('InvoicesList/',ProjectInvoicesList.as_view()),
   
    path('Invoicesdel/<int:pk>/',ProjectInvoicesdel.as_view()),





    path('PaymentsList/',ProjectPaymentsList.as_view()),
   
    path('Paymentsdel/<int:pk>/',ProjectPaymentsdel.as_view()),



    path('CurencyList/',CurencyList.as_view()),
   
    path('Curencydel/<int:pk>/',Curencydel.as_view()),


    path('ParametersList/',ParametersList.as_view()),
   
    path('Parametersdel/<int:pk>/',Parametersdel.as_view()),  


    path('MssandNdaList/',MssandNdaList.as_view()),
   
    path('MssandNdadel/<int:pk>/',MssandNdadel.as_view()),


]




    

