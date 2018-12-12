from db.models import Vm
from util import json_response


def vm_list(**kwargs):
    if len(kwargs.items()) is None:
        results = Vm.objects()
    else:
        results = Vm.objects(**kwargs)

    return json_response(results)


def get_vm_by_name(name):
    result = Vm(name=name)
    return json_response(result)
