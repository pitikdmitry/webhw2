from django.conf.urls import url

import views

urlpatterns = [
    url(r'^hello$', views.index, name='index'),

    url(r'^getpost$', views.getpost),
    """url(r'^$', questions_list, name='questions_list'), # список новых вопросов
    url(r'^$', questions_list, name='questions_list'), # список лучших вопросв
    url(r'^$', questions_list, name='questions_list'), # список вопросов по тегу
    url(r'^$', questions_list, name='questions_list'),  # страница одного впороса со списком овтптов
    url(r'^$', questions_list, name='questions_list'),  # форма логина
    url(r'^$', questions_list, name='questions_list'),  # форма регитсрации
    url(r'^$', questions_list, name='questions_list'),  # форма создания вопроса"""

    url(r'^is_get_or_post$', views.is_get_or_post)
	#url(r'^get$', views.getpost, name='index2'),

]
