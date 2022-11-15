from django.urls import path



from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('history',views.history,name='history'),
    path('logout',views.logout,name='logout'),
    path('catalogue',views.catalogue,name='catalogue'),
    path('pending',views.pending,name='pending'),
    path('about_us',views.about_us,name='about_us'),
    path('issue/<book_id>',views.issue,name='issue')
]