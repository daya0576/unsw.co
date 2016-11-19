from django.conf.urls import patterns, url, include
from rango import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^index-more-courses/$', views.index_more_courses, name='index-more-courses'),
    url(r'^index-more-comments/$', views.index_more_comments, name='index-more-comments'),

    url(r'^about/$', views.about, name='about'),
    url(r'^subject/(?P<sub_name_slug>[\w\-]+)/$', views.subject, name='subject'),
    url(r'^category/(?P<cat_name_slug>[\w\-]+)/$', views.get_category, name='category'),
    url(r'^subject/(?P<sub_name_slug>[\w\-]+)/add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_cat_page/$', views.add_cat_page, name='add_cat_page'),
    url(r'^delete_cat_page/$', views.delete_cat_page, name='delete_cat_page'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^goto/$', views.track_url, name='goto'),
    # url(r'^profile/$', views.track_url, name='profile'),
    url(r'^like_category/$', views.like_category, name='like_category'),
    url(r'^dislike_category/$', views.dislike_category, name='dislike_category'),

    url(r'^suggest_category/$', views.suggest_category, name='suggest_category'),
    url(r'^sub_search/$', views.sub_search, name='sub_search'),

    # url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^delete_answer/$', views.delete_answer, name='delete_answer'),
    url(r'^category/(?P<cat_name_slug>[\w\-]+)/edit_answer/(?P<answer_id>[\d]+)$', views.edit_answer, name='edit_answer'),
    url(r'^category/(?P<cat_name_slug>[\w\-]+)/add_answer/$', views.get_category, name='add_answer'),

    url(r'^answer_up/$', views.answer_up, name='answer_up'),
    url(r'^answer_up_off/$', views.answer_up_off, name='answer_up_off'),
    url(r'^answer_down/$', views.answer_down, name='answer_down'),
    url(r'^answer_down_off/$', views.answer_down_off, name='answer_down_off'),

    url(r'^member/(?P<author>[\w]+)/$', views.member, name='member'),
    url(r'^member/delete/(?P<detail_id>[\w]+)$', views.member_detail_delete, name='member_delete'),
)


