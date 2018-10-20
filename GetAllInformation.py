import psutil

# the Process Information data ...
def getProcessHeader():
    process_header = ['Process Name', 'User', '% CPU', 'ID', 'Status']

    return process_header


# getting Information about the Process

def getProcessInfo():
    process_info = []

    for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
        list_info = list()

        p = psutil.Process(int(proc.info['pid']))
        list_info.append(proc.info['name'])
        list_info.append(proc.info['username'])
        list_info.append(p.cpu_percent())
        list_info.append(proc.info['pid'])
        list_info.append(p.status())
        process_info.append(tuple(list_info))

    return process_info



def getFSHeader():
    FS_Header = ['Device', 'Directory', 'Type', 'Total', 'Available', 'Used', '%']

    return FS_Header


# getting Information about the Process

def getFSInfo():
    FS_info = []

    check = psutil.disk_partitions(all=True)

    for item in check:

        list_info = list()

        list_info.append(item.device)
        list_info.append(item.mountpoint)
        list_info.append(item.fstype)

        percent =  psutil.disk_usage(item.mountpoint)

        list_info.append(percent.total)
        list_info.append(percent.free)
        list_info.append(percent.used)
        list_info.append(percent.percent)


        FS_info.append(tuple(list_info))
    print(FS_info)
    return FS_info



