from django.contrib import admin


from .models import Student 


class StudentAdmin(admin.ModelAdmin):  
    list_display = ('projectname','username', 'workdescription','startdate','enddate','workhours','completed')  


# Register your models here.
admin.site.register(Student, StudentAdmin)  
