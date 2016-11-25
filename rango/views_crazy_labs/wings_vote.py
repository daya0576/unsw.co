# -*- coding: utf-8 -*-

import os
import json
import re
from django.shortcuts import render
from django.http import JsonResponse
from tango_with_django_project.settings import BASE_DIR


FILE = os.path.join(BASE_DIR, "static/z_test/wings_vote/vote_trend_all")


def get_files_in(FILE):
    files = [str(f) for f in os.listdir(FILE)]

    # sort by filename
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    files.sort(key=alphanum_key)

    return files


def get_voting_data():
    files = get_files_in(FILE)

    final_result = []
    for file in files:
        file_path = os.path.join(FILE, file)
        with open(file_path) as f:
            final_result.append(json.load(f))

    return final_result


def get_labels():
    return get_files_in(FILE)


def get_data(request):
    return render(request, 'z_lab/wings_vote.html', get_final_chart_data())


def get_final_chart_data():
    labels = get_labels()
    data = [[[] for x in range(5)] for y in range(11)]
    voting_items = []
    persons = []

    final_result = get_voting_data()

    ''' handle each file  '''
    for shot_result in final_result:
        # print shot_result
        keys = sorted(shot_result.keys(), key=lambda i: int(re.search(r'^(\d+)', i).group(1)))
        voting_items = keys

        ''' handle each voting item, e.g. 1、最佳男运动员奖 '''
        for i_item, k_item in enumerate(keys):
            # print k_item
            voting_item = k_item

            ''' handle each person(sort by name first) '''
            keys_name = sorted(shot_result[k_item].keys())
            persons.append(keys_name)

            for i_name, k_name in enumerate(keys_name):
                # handle voting data: e.g. 孙杨（游泳） 0.2450
                count = shot_result[k_item][k_name].strip(' ')
                data[i_item][i_name].append(float(count))

    # print labels
    # print data
    # print voting_items
    # print persons

    final_result = {}
    for i, item in enumerate(voting_items):
        final_result[item] = {}
        for j, person in enumerate(persons[i]):
            # print item, person
            final_result[item][person] = data[i][j]
    # print "final_result: ", final_result

    persons_dict = {}
    for i, item in enumerate(voting_items):
        persons_dict[item] = persons[i]
    # print persons_dict

    ''' generate colors'''
    colors = ['75,192,192', '192,75,192', '192,192,75', '75,75,192', '192,75,75']

    return {'labels': labels, 'final_result': final_result, 'voting_items': voting_items,
            'persons': persons, 'persons_dict': persons_dict, 'colors': colors}


if __name__ == "__main__":
    get_final_chart_data()


