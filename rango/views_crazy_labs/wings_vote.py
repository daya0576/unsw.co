# -*- coding: utf-8 -*-

import os
import json
from django.shortcuts import render
from django.http import JsonResponse
from tango_with_django_project.settings import BASE_DIR


FILE = os.path.join(BASE_DIR, "static/z_test/wings_vote/vote_trend.json")


def get_voting_data():
    with open(FILE) as f:
        final_result = json.load(f)

    return final_result


def get_x(data):
    return [shot['time'] for shot in data]


def get_y(data):
    vote_result = [shot['vote_result'] for shot in data]
    y1 = [vote[u'WINGS战队（电竞） '] for vote in vote_result]
    y2 = [vote[u'邹市明（拳击） '] for vote in vote_result]
    y3 = [vote[u'柯洁（围棋） '] for vote in vote_result]

    return y1, y2, y3


def get_data(request):
    voting_data = get_voting_data()

    x = get_x(voting_data)
    y1, y2, y3 = get_y(voting_data)

    return JsonResponse({'label': x, 'y1': y1, 'y2': y2, 'y3': y3})


from django.views.generic import TemplateView
line_chart = TemplateView.as_view(template_name='z_lab/wings_vote.html')


if __name__ == "__main__":
    data = get_voting_data()
    print(data)
    x = [shot['time'] for shot in data]
    print(x)

    vote_result = [shot['vote_result'] for shot in data]
    y1 = [vote[u'WINGS战队（电竞） '] for vote in vote_result]
    y2 = [vote[u'邹市明（拳击） '] for vote in vote_result]
    y3 = [vote[u'柯洁（围棋） '] for vote in vote_result]

    y = [y1, y2, y3]
