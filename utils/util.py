#encoding=utf-8
__author__ = 'g7842'


#时间转换为字符串
def time_2_ms_str(ms):
        if ms <= 0:
            return '00:00'
        time_sec, ms = ms / 1000, ms % 1000
        time_min, time_sec = time_sec / 60, time_sec % 60
        time_hor, time_min = time_min / 60, time_min % 60
        if time_hor == 0:
            return '%02d:%02d' % (time_min, time_sec)
        return '--:--'


def time_2_msz_str(ms):
    if ms <= 0:
        return '00:00.000'
    time_sec, ms = ms / 1000, ms % 1000
    time_min, time_sec = time_sec / 60, time_sec % 60
    time_hor, time_min = time_min / 60, time_min % 60
    if time_hor == 0:
        return '%02d:%02d.%02d' % (time_min, time_sec, ms)
    return '--:--.--'


def msz_str_2_time(msz):
    arr1 = str.split(msz, '.')
    time = int(arr1[1])
    ms = arr1[0]
    arr2 = str.split(ms, ':')
    time += int(arr2[0]) * 60 * 1000 + int(arr2[1]) * 1000
    return time