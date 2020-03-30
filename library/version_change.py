#!/usr/bin/python
# https://blog.toast38coza.me/custom-ansible-module-hello-world/
from ansible.module_utils.basic import *

def main():
    fields = {
        "version_no": {"default": True, "type": "str"},
        "version_name": {"default": True, "type": "str"},
       "unchanged_value": {"default": True, "type": "str"}
    }

    module = AnsibleModule(argument_spec=fields)
    module.params.update({"version_name": "After"})
    mylist = module.params["version_no"].split('.')
    mylist[2] = str(int(mylist[2]) + 2 )
    mylist[1] = str(int(mylist[1]) + 1)
    mystr = '.'.join(mylist)
    module.params.update({"version_no": mystr})

    module.exit_json(changed=True, meta=module.params)

if __name__ == '__main__':
    main()

