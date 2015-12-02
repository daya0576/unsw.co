from django.conf.urls import patterns, url, include
from rango import views
from DjangoUeditor import urls as DjangoUeditor_urls

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^subject/(?P<sub_name_slug>[\w\-]+)/$', views.subject, name='subject'),
    url(r'^category/(?P<cat_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^subject/(?P<sub_name_slug>[\w\-]+)/add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_cat_page/$', views.add_cat_page, name='add_cat_page'),
    url(r'^delete_cat_page/$', views.delete_cat_page, name='delete_cat_page'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^goto/$', views.track_url, name='goto'),
    # url(r'^profile/$', views.track_url, name='profile'),
    url(r'^like_category/$', views.like_category, name='like_category'),
    url(r'^dislike_category/$', views.dislike_category, name='dislike_category'),
    url(r'^suggest_category/$', views.suggest_category, name='suggest_category'),
    url(r'^ueditor/', include(DjangoUeditor_urls)),
    url(r'^edit_description_view/', views.edit_description_view, name='editor'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_answer/$', views.add_answer, name='add_answer'),

)


