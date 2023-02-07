import psutil

p = psutil.Process()


def get_CPU_usage():
    psutil.cpu_percent(interval=0.1)
    p_cpu = psutil.cpu_percent(interval=2)
    return str(p_cpu*10)


def get_RAM_postcalc(t, c):
    if c:
        return str(round(float(t) / 1024 / 1024 / 1024, 2))
    else:
        return str(round(float(t) / 1024 / 1024 / 1024, 2)) + " GiB"


def get_RAM(c):
    mem = psutil.virtual_memory()

    return [get_RAM_postcalc(mem.total, c), get_RAM_postcalc(mem.used, c), get_RAM_postcalc(mem.free, c)]


def get_DiskIO():
    i = psutil.disk_io_counters()
    return [bytesAutoformat(i.read_bytes), bytesAutoformat(i.write_bytes)]


def get_NetIO():
    i = psutil.net_io_counters()
    return [bytesAutoformat(i.bytes_recv), bytesAutoformat(i.bytes_sent)]


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
