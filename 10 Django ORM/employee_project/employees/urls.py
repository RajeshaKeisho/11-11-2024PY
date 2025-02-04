from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all_employees),
    path('jsdept/', views.js_department_employees),
    path('highsal/', views.highest_salary_employees),
    path('rhdept/', views.py_dept_highest_salary_employees),
    path('exclude/', views.exclude_highest_salary_employees),
    path('avgsal/', views.avg_salary),
    path('avgsalpd/', views.avg_salary_per_department),
    path('numemp/', views.num_employees_per_department),
    path('most/', views.dept_with_most_employees),
    path('hrit/', views.py_and_js_employees),
    path('salaryorname/', views.salary_or_name_contains),
    path('highpaid/', views.high_paid_employees),

]
