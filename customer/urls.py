from django.urls import path
from customer import views
urlpatterns=[
    path('accounts/signup',views.sign_up,name='signup'),
    path('accounts/signin',views.sign_in,name='signin'),
    path('accounts/signout',views.sign_out,name='signout'),
    path('accounts/home',views.base_home,name='home'),
    path('orders/add/<int:p_id>',views.order_create,name='orderbook'),
    path('my_orders',views.my_orders,name='my_orders'),
    path('my_order/remove<int:id>',views.order_remove,name='order_remove'),
    path('accounts/book/filter',views.book_find,name='findbook')
]