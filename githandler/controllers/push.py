# -*- coding: utf-8 -*-

from tg import expose
from tg import RestController
from tg import request
import subprocess


class PushController(RestController):
    @expose('githandler.templates.push')
    def index(self):
        return dict(page='push')

    @expose('json')
    def post(self, **kwargs):
        if request.environ['HTTP_ORIGIN'] is config.giturl:
            subprocess.call('bash-script')