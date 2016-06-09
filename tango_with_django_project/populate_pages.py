import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import urllib, urllib2
import django
from django.db.models import Q
django.setup()

from rango.models import Category, Subject
from bs4 import BeautifulSoup

from rango.models import Category, CatPage, User


def add_page(title, cat, url, views, user):
    page = CatPage.objects.get_or_create(category=cat, title=title, user=user)[0]

    page.url = url
    page.views = views

    page.save()


def generate_pages():
    # cat = Category.objects.get(no="COMP9021")
    cats = Category.objects.all()
    user = User.objects.get(id=100)

    for cat in cats:
        if "handbook" in cat.url:
            print cat.name + ": " + cat.url
            add_page("Link of Handbook", cat, cat.url, 0, user)
        else:
            print cat.name + " illegal url: " + cat.url

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    # delete_under()
    generate_pages()