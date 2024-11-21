# from HP54645D programming interface manual:
BAUDRATE_SLOWEST = 1200
BAUDRATE_SLOW = 2400
BAUDRATE_REGULAR = 9600
BAUDRATE_FAST = 19200


def process_bytes(waveform_data: bytes):
    header = waveform_data[:10]
    data = waveform_data[10:]
    d = [int(point) for point in data]
    h = [int(point) for point in header]
    return h, d
