# -*- coding:utf-8 -*-
# edit by fuzongfei

from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

from ProjectManager.pt.views import IncepPerformView, IncepRollbackView, IncepStopView, IncepOfRecordsView, \
    IncepOfRecordsListView, IncepOfDetailsView, IncepOfDetailsListView, IncepOfResultsView

urlpatterns = [
    path(r'incep_perform/', login_required(IncepPerformView.as_view()), name='p_incep_perform'),
    re_path(r'incep_rollback/', login_required(IncepRollbackView.as_view()), name='p_incep_rollback'),
    re_path(r'incep_stop/', login_required(IncepStopView.as_view()), name='p_incep_stop'),
    path(r'incep_perform_records/', login_required(IncepOfRecordsView.as_view()), name='p_incep_perform_records'),
    path(r'incep_perform_records_l/', login_required(IncepOfRecordsListView.as_view()),
         name='p_incep_perform_records_l'),
    re_path(r'incep_perform_details/(?P<taskid>.*)/', login_required(IncepOfDetailsView.as_view())),
    path(r'incep_perform_details_l/', login_required(IncepOfDetailsListView.as_view()),
         name='p_incep_perform_details_l'),
    re_path(r'incep_perform_records/', login_required(IncepOfResultsView.as_view()), name='p_incep_perform_records'),
]