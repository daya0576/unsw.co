import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
import urllib, urllib2
import django
django.setup()

from rango.models import Category, Subject
from bs4 import BeautifulSoup

def populate():
    # python_cat = add_cat('0', 'Python', views=128, likes=64, level='0')
    # add_page(cat=python_cat,
    #     title="Official Python Tutorial",
    #     url="http://docs.python.org/2/tutorial/")
    # add_page(cat=python_cat,
    #     title="How to Think like a Computer Scientist",
    #     url="http://www.greenteapress.com/thinkpython/")
    # add_page(cat=python_cat,
    #     title="Learn Python in 10 Minutes",
    #     url="http://www.korokithakis.net/tutorials/python/")

    # django_cat = add_cat('', "Django", views=64, likes=32)
    # add_page(cat=django_cat,
    #     title="Official Django Tutorial",
    #     url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")
    # add_page(cat=django_cat,
    #     title="Django Rocks",
    #     url="http://www.djangorocks.com/")
    # add_page(cat=django_cat,
    #     title="How to Tango with Django",
    #     url="http://www.tangowithdjango.com/")
    #
    # frame_cat = add_cat("Other Frameworks", views=32, likes=16)
    # add_page(cat=frame_cat,
    #     title="Bottle",
    #     url="http://bottlepy.org/docs/dev/")
    # add_page(cat=frame_cat,
    #     title="Flask",
    #     url="http://flask.pocoo.org")

    add_cat('BINF9010', 'Bioinformatics Methods and Applications', views=0, likes=0, level='0', url='http://www.handbook.unsw.edu.au/postgraduate/courses/2016/BINF9010.html')
    add_cat('COMP4161', 'Advanced Topics in Software Verification *', views=0, likes=0, level='0', url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP4161.html')
    add_cat('COMP9020', 'Foundations of Computer Science', views=0, likes=0, level='0', url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9020.html')
    add_cat('COMP9021', 'Principles of Programming', views=0, likes=0, level='0', url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9021.html')
    add_cat('COMP9032', 'Microprocessors and Interfacing', views=0, likes=0, level='0', url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9032.html')
    add_cat('COMP9116', 'System Development Using Event-B', views=0, likes=0, level='0', url='http://www.handbook.unsw.edu.au/postgraduate/courses/2013/COMP9116.html')
    add_cat('COMP9311', 'Database Systems', views=0, likes=0, level='0', url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9311.html')
    add_cat('COMP9414', 'Artificial Intelligence', views=0, likes=0, level='0', url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9414.html')
    add_cat('COMP9441', 'Security Engineering *', views=0, likes=0, level='0', url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9441.html')
    add_cat('COMP9511', 'Human Computer Interaction', views=0, likes=0, level='0', url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9511.html')
    add_cat('GSOE9210', 'Engineering Decision Structures', views=0, likes=0, level='0', url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/GSOE9210.html')
    add_cat('GSOE9820', 'Engineering Project Management', views=0, likes=0, level='0', url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/GSOE9820.html')

    add_cat('COMP4418', 'Knowledge Representation and Reasoning *', views=0, likes=0, level='1', url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP4418.html')
    add_cat('COMP6721', '(In-)Formal Methods: The Lost Art', views=0, likes=0, level='1', url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP6721.html')
    add_cat('COMP9024', 'Data Structures and Algorithms', views=0, likes=0, level='1', url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9024.html')
    add_cat('COMP9041', 'Software Construction: Techniques and Tools', views=0, likes=0, level='1', url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9041.html')
    add_cat('COMP9222', 'Digital Circuits and Systems', views=0, likes=0, level='1', url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9222.html')
    add_cat('COMP9331', 'Computer Networks and Applications', views=0, likes=0, level='1', url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9331.html')
    add_cat('COMP9334', 'System Capacity Planning *', views=0, likes=0, level='1', url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9334.html')
    add_cat('COMP9415 ', 'Computer Graphics', views=0, likes=0, level='1', url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9415.html')


    add_cat('BINF9020', 'Computational Bioinformatics', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/BINF9020.html')
    add_cat('COMP4001', 'Object-Oriented Software Development', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP4001.html')
    add_cat('COMP4141', 'Theory of Computation', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP4141.html')
    add_cat('COMP4411', 'Experimental Robotics *', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP4411.html')
    add_cat('COMP4431', 'Game Design Workshop', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP4431.html')
    add_cat('COMP4511', 'User Interface Design and Construction', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP4511.html')
    add_cat('COMP6714', 'Information Retrieval and Web Search *', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP6714.html')
    add_cat('COMP6752', 'Modelling Concurrent Systems', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP6752.html')
    add_cat('COMP6731', 'Geometric and Graph Theoretic Data Processing', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP6731.html')
    add_cat('COMP6771', 'Advanced C++ Programming *', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP6771.html')
    add_cat('COMP9101', 'Design & Analysis of Algorithms', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9101.html')
    add_cat('COMP9102 ', 'Programming Languages and Compilers', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9102.html')
    add_cat('COMP9018', 'Advanced Graphics', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9018.html')
    add_cat('COMP9151', 'Foundations of Concurrency', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9151.html')
    add_cat('COMP9161', 'Concepts of Programming Languages', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9161.html')
    add_cat('COMP9171', 'Object-Oriented Programming *', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9171.html')
    add_cat('COMP9181', 'Language-based Software Safety *', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9181.html')
    add_cat('COMP9152', 'Comparative Concurrency Semantics', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9152.html')
    add_cat('COMP9153', 'Algorithmic Verification *', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9153.html')
    add_cat('COMP9201', 'Operating Systems', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9201.html')
    add_cat('COMP9283 ', 'Extended Operating Systems', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9283.html')
    add_cat('COMP9211 ', 'Computer Architecture', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9211.html')
    add_cat('COMP9313', 'Big Data Management', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9313.html')
    add_cat('COMP9315', 'Database Systems Implementation', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9315.html')
    add_cat('COMP9318', 'Data Warehousing and Data Mining *', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9318.html')
    add_cat('COMP9319', 'Web Data Compresssion and Search *', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9319.html')
    add_cat('COMP9321', 'Web Applications Engineering', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9321.html')
    add_cat('COMP9332', 'Network Routing and Switching', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9332.html')
    add_cat('COMP9333', 'Advanced Computer Networks', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9333.html')
    add_cat('COMP9335', 'Wireless Mesh and Sensor Networks *', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9335.html')
    add_cat('COMP9336', 'Mobile Data Networking *', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9336.html')
    add_cat('COMP9417', 'Machine Learning and Data Mining *', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9417.html')
    add_cat('COMP9431', 'Robotic Software Architecture *', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9431.html')
    add_cat('COMP9444', 'Neural Networks *', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9444.html')
    add_cat('COMP9447', 'Security Engineering Workshop', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9447.html')
    add_cat('COMP9517', 'Computer Vision *', views=0, likes=0, level=2, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9517.html')


    add_cat('COMP4121', 'Advanced and Parallel Algorithms *', views=0, likes=0, level=3, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP4121.html')
    add_cat('COMP4432', 'Game Design Studio', views=0, likes=0, level=3, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP4432.html')
    add_cat('COMP6741', 'Parameterized and Exact Computation', views=0, likes=0, level=3, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP6741.html')
    add_cat('COMP9242', 'Advanced Operating Systems *', views=0, likes=0, level=3, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9242.html')
    add_cat('COMP9243', 'Distributed Systems *', views=0, likes=0, level=3, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9243.html')
    add_cat('COMP9322', 'Service-Oriented Architectures', views=0, likes=0, level=3, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9322.html')
    add_cat('COMP9323', 'e-Enterprise Project *', views=0, likes=0, level=3, url='http://www.handbook.unsw.edu.au/postgraduate/courses/current/COMP9323.html')
    # add_cat('', '', views=0, likes=0, level=3, url='')



    # Print out what we have added to the user.
    # for c in Category.objects.all():
    #     for p in Page.objects.filter(category=c):
    #         print "- {0} - {1}".format(str(c), str(p))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views

    p.save()
    return p


def add_cat(no, name, level, views, likes, description='', url=''):
    c = Category.objects.filter(no=no)
    if c.count() > 0:
        c = Category.objects.get(no=no)
        c.subject = Subject.objects.get(slug="both")
    else:
        c = Category(name=name)

        c.no = no
        c.level = level
        c.views = views
        c.likes = likes
        c.description = description
        c.url = url
        c.subject = Subject.objects.get(slug="cse-undergraduate")

    c.save()

    return c


def undergraduate():
    score_content = urllib.urlopen('http://www.handbook.unsw.edu.au/vbook2016/brCoursesBySubjectArea.jsp?studyArea=COMP&StudyLevel=Undergraduate').read()
    soup = BeautifulSoup(score_content)
    data = []

    table_all = soup.find('table', class_="tabluatedInfo")
    # table_body = table_all.find('tbody')

    rows = table_all.find_all('tr')
    for row in rows:
        cols = row.find_all('td')

        if len(cols) == 3:
            href = cols[1].find_all('a')
            href = href[0].get('href')
            cols = [ele.text.strip() for ele in cols]

            row_result = [ele for ele in cols if ele]
            row_result.append(href)

            data.append(row_result) # Get rid of empty values

    # print data
    # [u'COMP1000', u'Introduction to World Wide Web, Spreadsheets and Databases', u'6', u'http://www.handbook.unsw.edu.au/undergraduate/courses/2016/COMP1000.html']

    for row in data:
        print row
        add_cat(row[0], row[1], views=0, likes=0, level='0', url=row[3])


def delete_under():
    subject = Subject.objects.get(slug="cse-undergraduate")
    Category.objects.filter(subject=subject).delete()
    subject = Subject.objects.get(slug="both")
    Category.objects.filter(subject=subject).delete()


# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    delete_under()
    undergraduate()

