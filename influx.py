import configparser
from influxdb import InfluxDBClient

def influx_connection():
    settings = configparser.ConfigParser()
    settings.read('openstack_influx.ini')
    db_server=settings.get('influx', 'host')
    db_port=settings.get('influx', 'port')
    db_user=settings.get('influx', 'user')
    db_password=settings.get('influx', 'password')
    db_name=settings.get('influx', 'database')
    db_ssl=settings.get('influx', 'host')
    dbclient = InfluxDBClient(db_server,db_port,db_user,db_password,db_name,db_ssl)
    dblist = dbclient.get_list_database()
    influxconn = dbclient
    try:
        influxconn.ping()
    except ConnectionError:
        raise CantConnectToInfluxDBException('connection error')
    return influxconn


