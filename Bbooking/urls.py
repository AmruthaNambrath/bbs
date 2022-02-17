from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('reg', views.reg, name="reg"),
    path('userlog', views.userlog, name="userlog"),
    path('login', views.login, name="login"),
    path('userv', views.userv, name="userv"),
    path('add', views.add, name="add"),
    path('root', views.root, name="root"),
    path('search', views.search, name="search"),
    path('view', views.view, name="view"),
    path('book/<id>', views.book, name="book"),
    path('total/<id>', views.total, name="total"),
    path('history', views.history, name="history"),
    path('user_home', views.user_home, name='user_home'),
    path('states', views.states, name="states"),
    path('logout',views.logout,name="logout"),
    path('admins',views.admins,name="admins"),
    path('admilog',views.admilog,name="admilog"),
    path('payment',views.payment,name="payment"),
    path('success',views.success,name="success"),
    path('userh',views.userh,name="userh"),
    path('mail_check',views.mail_check,name="mail_check"),
    path('reset',views.reset,name="reset"),
    path('change',views.change,name="change"),
    path('alogout',views.alogout,name="alogout"),
    path('edit',views.edit,name="edit"),
    path('editbus',views.editbus,name="editbus"),
    path('back1',views.back1,name="back1"),
    path('back2',views.back2,name="back2"),
    path('back3',views.back3,name="back3"),
]
