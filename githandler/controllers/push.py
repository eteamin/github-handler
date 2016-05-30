# -*- coding: utf-8 -*-

import hmac
import subprocess
from hashlib import sha1
from tg import expose
from tg import RestController
from tg import request, response
from webob.exc import HTTPForbidden
from pymlconf import ConfigManager


class PushController(RestController):

    @expose('githandler.templates.push')
    def index(self):
        return dict(page='push')

    @expose('json')
    def post(self, payload):
        signature = hmac.new(key='', msg=str(payload), digestmod=sha1).hexdigest()
        if hmac.compare_digest(signature, request.headers.environ['X_HUB_SIGNATURE']):
            self.exec()
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

    def exec(self):
        __builtin_config = '''
        before_install:
          - mkdir test_dir
          - cd test_dir

        install:
          - touch test.txt
          - ls
        script:
          - rm test.txt

        after_success:
          - ls
          - cd ..
          - rm -rf test_dir
        '''

        config = ConfigManager(__builtin_config)
        commands = [config.before_install, config.install, config.script, config.after_success]
        for command in commands:
            for item in command:
                yield self.popen(item)
