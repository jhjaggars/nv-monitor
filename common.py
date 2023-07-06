import socket

HOSTNAME = socket.getfqdn()
names = "gpu    pwr  gtemp  mtemp     sm    mem    enc    dec    jpg    ofa   mclk   pclk".split()
units = "Idx      W      C      C      %      %      %      %      %      %    MHz    MHz".split()
nu_map = dict(zip(names, units))

def convert(n, v):
    return {
        "measurement": f"gpu_{n}",
        "tags": {
            "hostname": HOSTNAME,
        },
        "fields": {
            "value": v,
            "unit": nu_map[n],
        }
    }

def get_influx_client():
    import os
    from influxdb import InfluxDBClient

    user = os.environ.get("INFLUX_USER", "nvmon")
    password = os.environ.get("INFLUX_PASSWORD", "changeme")

    return InfluxDBClient("homeassistant", 8086, user, password, "homeassistant")
