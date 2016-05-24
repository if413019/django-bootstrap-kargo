from django.conf.urls import url
from customers import views as customer_views

urlpatterns = [
    url(r'^$', customer_views.index, name="index"),
    url(r'^customers/$', customer_views.customers, name="customers"),

    url(r'^create_customer/$', customer_views.create_customer, name="create_customer"),
    url(r'^edit_customer/(?P<uuid>[0-9a-z-]+)/$', customer_views.edit_customer, name="edit_customer"),
    url(r'^delete_customer/(?P<uuid>[0-9a-z-]+)/$', customer_views.delete_customer, name="delete_customer"),
]
