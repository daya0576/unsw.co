# -*- coding: utf-8 -*-

from random import randint
import os
import json

from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

from tango_with_django_project.settings import BASE_DIR


FILE = os.path.join(BASE_DIR, "static/z_test/wings_vote/vote_trend.json")


def get_voting_data():
    with open(FILE) as f:
        final_result = json.load(f)

    return final_result


def get_x():
    data = get_voting_data()
    x = [shot['time'] for shot in data]
    return x


def get_y():
    data = get_voting_data()
    vote_result = [shot['vote_result'] for shot in data]
    y1 = [vote[u'WINGS战队（电竞） '] for vote in vote_result]
    y2 = [vote[u'邹市明（拳击） '] for vote in vote_result]
    y3 = [vote[u'柯洁（围棋） '] for vote in vote_result]

    y = [y1, y2, y3]
    return y


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels."""
        # return ["January", "February", "March", "April", "May", "June", "July"]
        return get_x()

    def get_data(self):
        """Return 3 datasets to plot."""
        # return [[75, 44, 92, 11, 44, 95, 35],
        #         [41, 92, 18, 3, 73, 87, 92],
        #         [87, 21, 94, 3, 90, 13, 65]]
        return get_y()


line_chart = TemplateView.as_view(template_name='z_lab/wings_vote.html')
line_chart_json = LineChartJSONView.as_view()


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
