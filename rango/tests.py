# coding: UTF-8
from django.test import TestCase
from django.conf import settings

settings.configure()

from django.core.mail import send_mail

send_mail(subject=u'测试 第一封',
          message=u'哈哈哈哈',
          from_email='daya0576@gmail.com',
          recipient_list=['me@changchen.me'],
          fail_silently=False,
          # auth_user="daya0576@gmail.com",
          # auth_password="a7198192"
          )
