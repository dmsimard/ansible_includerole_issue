from __future__ import (absolute_import, division, print_function)
from ansible.plugins.callback import CallbackBase

import json

class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'notification'
    CALLBACK_NAME = 'reproducer'

    def __init__(self):
        super(CallbackModule, self).__init__()

    def v2_runner_on_ok(self, result):
        print("#" * 40)
        print(result._result)
        parsed = json.loads(self._dump_results(result._result))
        print("#" * 40)
        print(parsed)
        print("#" * 40)
