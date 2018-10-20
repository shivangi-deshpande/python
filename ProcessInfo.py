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
