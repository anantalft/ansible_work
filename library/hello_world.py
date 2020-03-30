#!/usr/bin/python
#https://medium.com/@auscunningham/write-a-ansible-module-with-python-527f0b292b4d
from ansible.module_utils.basic import *

def main():
    fields  = {
     "args": {"default": True, "type": "str"},
    }
    module = AnsibleModule(argument_spec=fields)
    theReturnValue = {
    "hello": "world",
    "input": module.params["args"]
    }
    module.exit_json(changed=False, meta=theReturnValue)

if __name__ == '__main__':
    main()
