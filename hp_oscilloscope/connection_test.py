import time
from .oscilloscope_auxiliary import process_bytes
import serial

connection = serial.Serial(
    port='COM5', baudrate=19200, timeout=0.2, parity=serial.PARITY_NONE,
    xonxoff=True, dsrdtr=False, stopbits=serial.STOPBITS_ONE
)


def execute(connection_instance: serial.Serial, command_):
    print(command_)
    connection_instance.write(
        chr(17).encode('ASCII') + command_ + chr(10).encode('ASCII') + chr(19).encode('ASCII')
    )
    data = connection_instance.read(4020)
    if "WAVEFORM:DATA" in command_:
        return process_bytes(data)
    else:
        print(data)


# from HP54645D programming interface manual:
# :ANALOG1:RANGE 0.4 -> 50 mV
# :ANALOG1:RANGE 4 -> 500 mV
# :ANALOG1:RANGE 1 -> 125 mV
# :TIM:RANG 1 -> 100ms
# :TIM:RANG 10 -> 1s
# :TIM:RANG 0.1 -> 10ms
# :TRIG:MODE AUTL -> set triggering to automatic level
# :DIGITIZE -> prepares next waveform to be saved and made available for sending through RS232
# :WAVEFORM:DATA? -> can acquire visual representation of waveform (up to 4k points) after digitizing
# AC coupling is not available for Glitch triggering!!!
# LF/HF reject is not available for Glitch triggering!!!
# Noise reject is available for Glitch triggering, as well as trigger mode (normal/auto/autolvl)

commands = [
    # b'*IDN?',
    # b'*RST',
    # b':ANALOG1:RANGE .4;',
    # b':ANAL1:RANG?',
    # b':TRIGGER:GLITCH:QUALIFIER RANGE;',
    # semicolon is mandatory as the size of the query is too big
    # this collides with the next query in line
    # b':TRIG:GLIT:RANGE .0000007,.0000016;',
    # b':TRIG:GLIT:RANGE?',
    # b':TRIG:GLIT:POL NEG;',
    # b':TRIG:GLIT:POL?',
    # b':DISPLAY:GRID ON',
    # b':DISPlay:CONNect?',
    # b':DISPLAY:COLUMN 20',
    # b':DIGITIZE',
    # b':WAVEFORM:POINTS 4000',
    # b':WAVEFORM:PREAMBLE?',
    b':WAVEFORM:DATA?',
    # b'*RST',
    # b':ACQ:DATA?',
]


for command in commands:
    execute(connection_instance=connection, command_=command)
    time.sleep(0.5)
