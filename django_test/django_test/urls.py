from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns=patterns('',
    (r'^articles/',include('article.urls')),
    url(r'^admin/',include(admin.site.urls)),

    url(r'^accounts/login/$','django_test.views.login'),
    url(r'accounts/auth/$','django_test.views.auth_view'),
    url(r'^accounts/logout/$','django_test.views.logout'),
    url(r'^accounts/loggedin/$','django_test.views.loggedin'),
    url(r'^accounts/invalid/$','django_test.views.invalid_login'),
    url(r'^accounts/register/$','django_test.views.register_user'),
    url(r'^accounts/register_success/$','django_test.views.register_success'),
)




#OLD - TILL VIDEO - 3
"""
from django.conf.urls import patterns, include, url
from article.views import HelloTemplate
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^hello/$','article.views.hello'),
    url(r'^vijay/$','article.views.vijay'),
    url(r'^hello_template/$','article.views.hello_template'),
    url(r'^hello_template_simple/$','article.views.hello_template_simple'),
    url(r'^hello_class_view/$',HelloTemplate.as_view()),
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
"""