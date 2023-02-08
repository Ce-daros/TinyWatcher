import psutil
import time

p = psutil.Process()


def get_CPU_usage():
    psutil.cpu_percent(interval=0.1)
    p_cpu = psutil.cpu_percent(interval=2)
    return str(p_cpu)


def get_RAM_postcalc(t):
    return str(round(float(t) / 1024 / 1024 / 1024, 2))


def get_RAM(c):
    mem = psutil.virtual_memory()

    return [get_RAM_postcalc(mem.total), get_RAM_postcalc(mem.used), get_RAM_postcalc(mem.free)]


def get_DiskIO():
    send1 = psutil.disk_io_counters()[0]
    recv1 = psutil.disk_io_counters()[1]
    time.sleep(1)
    send2 = psutil.disk_io_counters()[0]
    recv2 = psutil.disk_io_counters()[1]
    return [bytesAutoformat(send2-send1), bytesAutoformat(recv2-recv1)]


def get_NetIO():
    send1 = psutil.net_io_counters()[0]
    recv1 = psutil.net_io_counters()[1]
    time.sleep(1)
    send2 = psutil.net_io_counters()[0]
    recv2 = psutil.net_io_counters()[1]
    return [bytesAutoformat(send2-send1), bytesAutoformat(recv2-recv1)]


def bytesAutoformat(b):
    fmtxt = ""
    ratio = 1
    if b <= 1024-1:
        fmtxt = "Bytes"
    elif b <= 1024*1024-1:
        ratio = 1024
        fmtxt = "KiB"
    elif b <= 1024*1024*1024-1:
        ratio = 1024*1024
        fmtxt = "MiB"
    elif b <= 1024*1024*1024*1024-1:
        ratio = 1024*1024*1024
        fmtxt = "MiB"
    b /= ratio
    return str(round(b, 2))+" "+fmtxt
