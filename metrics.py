#!/usr/bin/env python
import psutil,shutil
import os
import pynvml as nv

def get_ram_usage():
    """
    Obtains the absolute number of RAM bytes currently in use by the system.
    :returns: System RAM usage in bytes.
    :rtype: int
    """
    return int(psutil.virtual_memory().total - psutil.virtual_memory().available)

        
def get_cpu_temp():
    """
    Obtains the current value of the CPU temperature.
    :returns: Current value of the CPU temperature if successful, zero value otherwise.
    :rtype: float
    """
    # Initialize the result.
    result = 0.0
    # The first line in this file holds the CPU temperature as an integer times 1000.
    # Read the first line and remove the newline character at the end of the string.
    if os.path.isfile('/sys/class/thermal/thermal_zone0/temp'):
        with open('/sys/class/thermal/thermal_zone0/temp') as f:
            line = f.readline().strip()
            # Test if the string is an integer as expected.
            if line.isdigit():
                # Convert the string with the CPU temperature to a float in degrees Celsius.
                result = float(line) / 1000
    # Give the result back to the caller.
    return result

def get_cpu_frequency():
    """
    Obtains the real-time value of the current CPU frequency.
    :returns: Current CPU frequency in MHz.
    :rtype: int
    """
    return int(psutil.cpu_freq().current)


def get_cpu_usage_pct():
    """
    Obtains the system's average CPU load as measured over a period of 500 milliseconds.
    :returns: System CPU load as a percentage.
    :rtype: float
    """
    return psutil.cpu_percent(interval=0.5)

def get_cpu_load():
    """
    Obtains the system's average CPU load over time.
    :returns: System CPU load over time.
    :rtype: float
    """
    load1, load5, load15 = psutil.getloadavg()
    cpu_usage = (load5/os.cpu_count()) * 100
    return cpu_usage


def get_ram_total():
    """
    Obtains the total amount of RAM in bytes available to the system.
    :returns: Total system RAM in bytes.
    :rtype: int
    """
    return int(psutil.virtual_memory().total)


def get_ram_usage_pct():
    """
    Obtains the system's current RAM usage.
    :returns: System RAM usage as a percentage.
    :rtype: float
    """
    return psutil.virtual_memory().percent


def get_gpu_stats():
    """
    Obtains the system's current GPU (nvidia) temperature.
    :returns: ...
    :rtype: float... usage,temp,power
    """
    nv.nvmlInit()
    handle = nv.nvmlDeviceGetHandleByIndex(0)
    gpu_util = nv.nvmlDeviceGetUtilizationRates(handle).gpu
    gpu_temp = nv.nvmlDeviceGetTemperature(handle, nv.NVML_TEMPERATURE_GPU)
    print (dir(nv))
    mem = nv.nvmlDeviceGetMemoryInfo(handle)
    print (mem)
    print (dir(mem))
    gpu_power = int(nv.nvmlDeviceGetPowerUsage(handle)/1000)
    nv.nvmlShutdown()
    return gpu_util,gpu_temp,gpu_power


def get_disk_usage_pct():
    """
    Obtains the system's current / disk usage.
    :returns: System disk usage as a percentage.
    :rtype: float
    """
    path = "/"
    bytes_avail = psutil.disk_usage(path).free
    gigabytes_avail = bytes_avail / 1024 / 1024 / 1024
    bytes_avail = psutil.disk_usage(path).total
    total_avail = bytes_avail / 1024 / 1024 / 1024
    disk = (gigabytes_avail/total_avail)*100

    path = "/"
    disk = shutil.disk_usage(path)
    disk = (disk.used/disk.total)*100
    return disk

        
def get_metrics():
    mem_usage = int(get_ram_usage() / 1024 / 1024)
    cpu_temp = get_cpu_temp()
    cpu_freq = get_cpu_frequency()
    cpu_usage = get_cpu_usage_pct()
    mem_total = int(get_ram_total() / 1024 / 1024)
    mem_pct = get_ram_usage_pct()
    disk_usage = get_disk_usage_pct()
    cpu_load = get_cpu_load()
    gpu_util,gpu_temp,gpu_power = get_gpu_stats()
    
    return (mem_usage,cpu_temp,cpu_freq,cpu_usage,mem_total,mem_pct,disk_usage,gpu_util,gpu_temp,gpu_power)

if __name__ == "__main__":
    print('RAM usage is {} MB'.format(int(get_ram_usage() / 1024 / 1024)))
    print('CPU temperature is {} degC'.format(get_cpu_temp()))
    print('CPU frequency is {} MHz'.format(get_cpu_frequency()))
    print('System CPU load is {} %'.format(get_cpu_usage_pct()))
    print('System CPU load5 is {} %'.format(get_cpu_load()))
    print('RAM total is {} MB'.format(int(get_ram_total() / 1024 / 1024)))
    print('RAM usage is {} %'.format(get_ram_usage_pct()))
    print('Disk usage is {} %'.format(get_disk_usage_pct()))
    gpu_util,gpu_temp,gpu_power = get_gpu_stats()
    print('GPU usage is {} %'.format(gpu_util))
    print('GPU temp is {} C'.format(gpu_temp))
    print('GPU power_usage is {} W'.format(gpu_power))
    
    print (get_metrics())
    


