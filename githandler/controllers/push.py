# -*- coding: utf-8 -*-

from tg import expose
from tg import RestController
from tg import request, response
from webob.exc import HTTPForbidden

import subprocess


class PushController(RestController):
    @expose('githandler.templates.push')
    def index(self):
        return dict(page='push')

    @expose('json')
    def post(self):
        if request.environ['HTTP_ORIGIN'] is 'hello':
            print()
        else:
            return HTTPForbidden().explanation

    @staticmethod
    def popen(executable, timeout=None):
        sb = subprocess.Popen(
            '%s' % executable,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
        stdout, stderr = sb.communicate(timeout=timeout)
        return stdout, stderr, sb.returncode

