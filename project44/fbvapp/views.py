from django.shortcuts import render,redirect
from fbvapp.models import Employee
from fbvapp.forms import EmployeeForm
# Create your views here.
def retrive_data(request):
	emp=Employee.objects.all()
	my_dict={'emp':emp}
	return render(request=request,template_name='fbvapp/index.html',context=my_dict)

def create_data(request):
	form=EmployeeForm()
	my_dict={'form':form}
	if request.method=='POST':
		form=EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/index/')	

	return render(request=request, template_name='fbvapp/create.html',context=my_dict)

def delete_view(request,id):
	employee=Employee.objects.get(id=id)
	employee.delete()
	return redirect('/index/')

def update_view(request,id):
	employee=Employee.objects.get(id=id)
	my_dict={'employee':employee}
	if request.method=="POST":
		form=EmployeeForm(request.POST,instance=employee)
		if form.is_valid():
			form.save()
		return redirect('/index/')
	return render(request=request, template_name='fbvapp/update.html',context=my_dict)