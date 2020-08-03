from measures import Hypervisor
import os

os.environ['REQUESTS_CA_BUNDLE'] = '/etc/ssl/certs/rootCA.pem'

class OpenstackUtil:
    def __init__(self, cloud_name):
        self.cloud_name = cloud_name
        self.conn = openstack.connect(cloud=self.cloud_name)

    def get_hypervisors(self):
            hypervisors = []
            settings = configparser.ConfigParser()
            settings.read('openstack_influx.ini')
            cpu_ratio = settings.get('compute', 'cpu_ratio')
            for h in self.conn.list_hypervisors(): 
                    hypervisors.append(Hypervisor(cloud_name=self.cloud_name,compute=h['name'],status=h['status'],running_vms=h['running_vms'],vcpus_used=h['vcpus_used'],memory_used=h['memory_used'],vcpus_size=h['vcpus'],memory_size=h['memory_size']).to_measurement()) 
            return hypervisors





