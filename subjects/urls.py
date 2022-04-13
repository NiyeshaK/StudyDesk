from django.urls import path
from . import views

urlpatterns = [
    path('OS',views.OS,name="OS"),
    path('DS',views.DS,name="DS"),
    path('dbms',views.dbms,name="dbms"),
    path('cn',views.cn,name="cn"),
    path('coa',views.coa,name="coa"),
    path('se',views.se,name="se"),
    path('python',views.python,name="python"),
    path('c',views.c,name="c"),
    path('php',views.php,name="php"),
    path('java',views.java,name="java"),
    path('df',views.df,name="df"),
    
    path('',views.subjects,name="subjects"),
]