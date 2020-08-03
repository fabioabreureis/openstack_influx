import os
import json
import logging
import re
import openstack.cloud
from pathlib import Path

class Hypervisor:
    def __init__(self, cloud_name=None,compute=None, status=None, running_vms=None, vcpus_used=None,memory_used=None, vcpus_size=None,memory_size=None ): 
        self.cloud_name = cloud_name
        self.compute = compute
        self.status = status
        self.running_vms = running_vms
        self.vcpus_used = vcpus_used
        self.memory_used = memory_used
        self.vcpus_size = vcpus_size
        self.memory_size = memory_size

    def to_measurement(self):
        return [{"measurement":"Computes",
            "tags": {
            'cloud_name': self.cloud_name,
            'compute': self.compute,
            'status': self.status,
            'running_vms': self.running_vms,
            'vcpus_used': self.vcpus_used,
            'memory_used': self.memory_used,
            'vcpus_size': self.vcpus_size,
            'memory_size': self.memory_size
            },
                  "fields":
            {
                "SessionDuration":1.2
            } }]