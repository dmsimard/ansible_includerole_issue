# ansible_includerole_issue

```
$ ansible-playbook playbook.yml 
 [WARNING]: Host file not found: /etc/ansible/hosts

 [WARNING]: provided hosts list is empty, only localhost is available


PLAY [Run reproducer without static] **********************************************************************************************************************************************************

TASK [reproducer : debug] *********************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": "noop"
}
########################################
{'msg': u'noop', '_ansible_verbose_always': True, '_ansible_no_log': False}
########################################
{u'msg': u'noop'}
########################################

PLAY [Run reproducer with static] *************************************************************************************************************************************************************

TASK [include_role] ***************************************************************************************************************************************************************************
########################################
{'include_variables': {u'name': u'reproducer'}, 'include_role': TASK: include_role, 'changed': False}
 [WARNING]: Failure using method (v2_runner_on_ok) in callback plugin
(<ansible.plugins.callback./home/dmsimard/dev/ansible_includerole_issue/library/plugins/callback/reproducer.CallbackModule object at 0x7f84ec98e190>): TASK: include_role is not JSON
serializable


TASK [reproducer : debug] *********************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": "noop"
}
########################################
{'msg': u'noop', '_ansible_verbose_always': True, '_ansible_no_log': False}
########################################
{u'msg': u'noop'}
########################################

PLAY RECAP ************************************************************************************************************************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```