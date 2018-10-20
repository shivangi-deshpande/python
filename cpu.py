import psutil
from time import sleep

class cpuInfo:

    def __init__(self):
        data = psutil.cpu_times()

        print(data)

        # for x in range(10):
        #     psutil.cpu_percent(interval=1, percpu=True)
        #     print(psutil.net_io_counters(pernic=False, nowrap=True))
        # print(psutil.cpu_count(logical=True))
        #
        # print(int(psutil.sensors_battery ( ).percent),"%")
        # print(int(psutil.boot_time ( ))/60)
        # print(psutil.users())
        # print(psutil.cpu_stats())
        # print(len(psutil.Process().cpu_affinity()))
        #
        # print(psutil.net_connections ( kind='inet' ))

class memoryInfo:
    def __init__(self):
        x = 0

class batteryInfo:
    def __init__(self):
        print(int(psutil.sensors_battery ().percent),"%")
class networkInfo:
    def __init__(self):
        while True:
            print(psutil.net_io_counters ( pernic=False, nowrap=True ))
            sleep(3)

cpuInfo()
batteryInfo()
networkInfo()
