# -*- coding: utf-8 -*-
import os
import yaml
import re
from pathlib import Path
from openstack_util import OpenstackUtil
from influx import influx_connection
from influxdb import InfluxDBClient

UNIX_CONFIG_HOME = os.path.join(os.path.expanduser(os.path.join('~', '.config')), 'openstack_influx')
UNIX_SITE_CONFIG_HOME = '/etc/openstack_influx'


CONFIG_SEARCH_PATH = [
    os.getcwd(),
    UNIX_CONFIG_HOME, UNIX_SITE_CONFIG_HOME
]


YAML_SUFFIXES = ('.yaml', '.yml')


CONFIG_FILES = [
    os.path.join(d, 'openstack_influx' + s)
    for d in CONFIG_SEARCH_PATH
    for s in YAML_SUFFIXES
]


def get_config():
    for path in CONFIG_FILES:
        if os.path.exists(path):
            with open(path, 'r') as f:
                return path, yaml.safe_load(f)
    raise Exception("Not load the config file, verify if files exists in %s." % CONFIG_FILES)

dbclient = InfluxDBClient('localhost',8086,'root','root','python')
json_data=OpenstackUtil('lab1').get_hypervisors()

dbclient.write_points(json_data)

