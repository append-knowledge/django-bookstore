from django.urls import path
from owner import views
urlpatterns=[
    path('',views.owner_dashboard,name="dashboard"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('books/add',views.books_add,name="addbook"),
    path('books/edit/<int:id>',views.books_edit,name="editbook"),
    path('books/remove<int:id>',views.books_delete,name="removebook"),
    path('books/list',views.book_list,name='booklist'),
    path("books/home",views.home,name="bookhome"),
    path('books/details/<int:id>',views.book_detail,name="bookdetails"),
    path('dash/edit/<int:id>',views.owner_edit,name='dashedit')
]