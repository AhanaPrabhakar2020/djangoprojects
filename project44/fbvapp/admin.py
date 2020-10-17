from django.contrib import admin
from fbvapp.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    '''
        Admin View for Employee
    '''
    list_display = ['eno','ename','esalary','eaddress']
    
	
    

admin.site.register(Employee, EmployeeAdmin)


