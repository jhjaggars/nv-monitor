from pprint import pprint
import time

import pynvml as gpu

import common

stats = dict.fromkeys(["pwr", "gtemp", "mtemp", "mclk", "pclk"])

# set it up
gpu.nvmlInit()
DEVICE = gpu.nvmlDeviceGetHandleByIndex(0)

def read_stats(client):
    read_stats_instant()
    points = [common.convert(k, v) for k, v in stats.items()]
    client(points)


def read_stats_instant():
    stats["pwr"] = gpu.nvmlDeviceGetPowerUsage(DEVICE) / 1000 # milliwatts
    stats["gtemp"] = gpu.nvmlDeviceGetTemperature(DEVICE, 0)
    stats["mclk"] = gpu.nvmlDeviceGetClockInfo(DEVICE, 2)
    stats["pclk"] = gpu.nvmlDeviceGetClockInfo(DEVICE, 0)


if __name__ == "__main__":

    while(True):
        read_stats(pprint)
        time.sleep(1)
