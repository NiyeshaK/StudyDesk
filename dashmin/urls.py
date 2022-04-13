from django.urls import path
from . import views

urlpatterns = [
    path('profile',views.profile,name="profile"),
    path('edit',views.edit,name="edit"),
    path('form',views.form,name="form"),
    path('submit',views.submit,name="submit"),
    path('table',views.table,name="table"),
    path('table/note/<int:pk>',views.view1,name="view1"),
    path('table/video/<int:pk>',views.view2,name="view2"),
    path('vid',views.vid,name="vid"),
    path('table/delete_note/<int:pk>',views.delete_n,name="delete-n"),
    path('table/delete_v/<int:pk>',views.delete_v,name="delete-v"),
    
]

