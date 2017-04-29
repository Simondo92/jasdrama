# -*- coding: utf-8 -*-
"""
.. module:: .urls
   :synopsis: 

.. moduleauthor:: Simon Anderson-Dry <simon.andersondry@therealbuzzgroup.com>
"""
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from home_page import views
from home_page.views import HomePage

urlpatterns = [
    url(r'^$', views.index, name='hello_world'),
    url(r'^index/$', HomePage.as_view(), name='hello_world2'),

]
