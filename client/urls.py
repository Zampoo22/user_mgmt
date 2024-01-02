from django.urls import path
from . import views

urlpatterns = [ 
    path("user", views.client_list),
    path("user/<int:id>", views.get_client_detail, name="get employee detail")
    ,path('user_update/<int:pk>', views.update_client_detail)
    ,path('user/delete/<int:pk>', views.delete_client)
]


