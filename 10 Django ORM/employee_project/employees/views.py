from django.shortcuts import render
from django.db.models import Avg, Count 
from django.db.models import Q 
from .models import Employee, Department 
from django.db import connection
 
# Create your views here.
def all_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees/all.html', {'employees':employees})

def js_department_employees(request):
    js_employees = Employee.objects.filter(department__name = "Javascript")
    return render(request, 'employees/js_employees.html', {'js_employees':js_employees})

def highest_salary_employees(request):
    highest_salary_employees = Employee.objects.filter(salary__gt = 50000)
    return render(request, 'employees/highest_salary_employees.html', {'highest_salary_employees':highest_salary_employees})


def py_dept_highest_salary_employees(request):
    py_dept_highest_salary_employees = Employee.objects.filter(department="Python", salary__gte = 50000)
    return render(request, 'employees/py_dept_highest_salary_employees.html', {'py_dept_highest_salary_employees':py_dept_highest_salary_employees})

def exclude_highest_salary_employees(request):
    exclude_highest_salary_employees = Employee.objects.exclude(salary__gte = 60000)
    return render(request, 'employees/exclude_highest_salary_employees.html', {'exclude_highest_salary_employees':exclude_highest_salary_employees})

def avg_salary(request):
    avg_salary = Employee.objects.aggregate(avg_salary= Avg('salary'))
    return render(request, 'employees/avg_salary.html', {'avg_salary':avg_salary})

def avg_salary_per_department(request):
    departments = Department.objects.aggregate(avg_salary= Avg('employee_salary'), )
    return render(request, 'employees/avg_salary_per_department.html', {'departments':departments})


def num_employees_per_department(request):
    departments = Department.objects.annotate(num_employees = Count('employee'))
    return render(request, 'employees/num_employees_per_department.html', {'departments':departments})

def dept_with_most_employees(request):
    department = Department.objects.annotate(num_employees = Count('employee')).order_by('- num_employees').first()
    return render(request, 'employees/dept_with_most_employees.html', {'department':department})

def py_and_js_employees(request):
    employees = Employee.objects.filter(Q(department_name="Python") & Q(department_name="Javascript"))
    return render(request, 'employees/py_and_js_employees.html', {'employees':employees})

def salary_or_name_contains(request):
    employees = Employee.objects.filter(Q(name__icontains="Python") | Q(salary__gte=60000))
    return render(request, 'employees/employees_list.html', {'employees':employees})

def high_paid_employees(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM employees_employee WHERE salary > 60000")
        employees = cursor.fetchall()

    employee_object = [Employee(*row) for row in employees]
    return render(request, 'employees/employees_list.html', {'employees':employee_object})



