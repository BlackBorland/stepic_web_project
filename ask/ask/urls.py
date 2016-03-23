from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.get_questions, name="first_page", kwargs={"question_type": "new"}),
    url(r'^login/$', views.login, name="login"),
    url(r'^question/(?P<question_id>\d+)/$', views.get_current_question, name="question"),
)
