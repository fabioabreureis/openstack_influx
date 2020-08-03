#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import openstack.cloud
import configparser
from measures import Hypervisor
from influx import influx_connection

#openstack.enable_logging(http_debug=True)

class OpenstackUtil:
    def __init__(self, cloud_name):
        self.cloud_name = cloud_name
        self.conn = openstack.connect(cloud=self.cloud_name)

    def get_hypervisors(self):
        for h in self.conn.list_hypervisors():
            hypervisors = []
            settings = configparser.ConfigParser()
            settings.read('openstack_influx.ini')
            cpu_ratio = settings.get('compute', 'cpu_ratio')
            hypervisors.append(Hypervisor(cloud_name=self.cloud_name,compute=h['name'],status=h['status'],running_vms=h['running_vms'],vcpus_used=h['vcpus_used'],memory_used=h['memory_used'],vcpus_size=h['vcpus'] * cpu_ratio,memory_size=h['memory_size']).to_measurement())
            return hypervisors








