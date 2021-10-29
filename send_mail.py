import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'helloSite.settings'


if __name__ == '__main__':
    send_mail('测试邮箱内容发送！',
              'Python、Java：能实现简单的功能需求，写小项目',
              'sjp19941119@163.com',
              ['1048707084@qq.com'],)