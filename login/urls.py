from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'django.contrib.auth.views.login', {'template_name':'login/index.html'}, name='login'),
    url(r'^$', 'django.contrib.auth.views.logout_then_login', name='logout'),
]
