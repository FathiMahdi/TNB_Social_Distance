"""
Connect to InfluxDB 2.0 - write data and query them
"""

from datetime import datetime

from influxdb_client import Point, InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS



for i in range(1,1000):
    """
    Configure credentials
    """
    influx_cloud_url = 'https://eu-central-1-1.aws.cloud2.influxdata.com'
    influx_cloud_token = 'WEbhQGqTUVlsSYEnFRP0GWZdex3pjCjBl2HzxFWlpr6AY1j6L6_bzWs4jk1j2ao4hgRi9Mqq3--X-mTOANKt7A=='
    bucket = 'testunitenspatial'
    org = 'unitenspatial@gmail.com'

    with InfluxDBClient(url=influx_cloud_url, token=influx_cloud_token) as client:
        kind = ''
        device = 'cam22'

        """
        Write data by Point structure
        """
        point = Point('Person').tag('device', 'cam33').field('value', i).time(time=datetime.utcnow())
        write_api = client.write_api(write_options=SYNCHRONOUS)
        write_api.write(bucket=bucket, org=org, record=point)
        point = Point('sitting').tag('device', 'cam33').field('value', i*2).time(time=datetime.utcnow())
        write_api = client.write_api(write_options=SYNCHRONOUS)
        write_api.write(bucket=bucket, org=org, record=point)
        point = Point('Moving').tag('device', 'cam33').field('value', i*3).time(time=datetime.utcnow())
        write_api = client.write_api(write_options=SYNCHRONOUS)
        write_api.write(bucket=bucket, org=org, record=point)
        print(f'Writing to InfluxDB cloud: {point.to_line_protocol()} ...')
        print()
        print('success')
        print()
        print()
