# coding: UTF-8
from django.test import TestCase
# from django.conf import settings
from rango.models import Category
from django.core.urlresolvers import reverse


class CaregoryMethodTests(TestCase):

    def test_ensure_views_are_postive(self):
        cat = Category(name='test', views=-1, likes=0)
        cat.save()
        self.assertEqual((cat.views >= 0), True)

    def test_slug_line_creation(self):
         cat = cat('Random Category String')
         cat.save()
         self.assertEqual(cat.slug, 'random-category-string')


class IndexViewTests(TestCase):

    def test_index_view_with_no_categories(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['categories'], [])





# settings.configure()

# from django.core.mail import send_mail
#
# send_mail(subject=u'测试 第一封',
#           message=u'哈哈哈哈',
#           from_email='daya0576@gmail.com',
#           recipient_list=['me@changchen.me'],
#           fail_silently=False,
#           # auth_user="daya0576@gmail.com",
#           # auth_password="a7198192"
#           )


