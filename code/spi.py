import spidev
LOG_LEVEL = 2
def log(msg, log_level=LOG_LEVEL):
    """
    Print a message, and track, where the log is invoked
    Input:
    -msg: message to be printed, ''
    -log_level: informationlevel, i
    """
    global LOG_LEVEL
    if log_level <= LOG_LEVEL:
        print(str(log_level) + ' : ' + __file__ + '.py::' + traceback.extract_stack()[-2][2] + ' : ' + msg)
        
class SPI(object):
    def __init__(self,**kwargs):
        self._spi = spidev.SpiDev(0,0)
        self._spi.max_speed_hz = 25000000

    def send_data(self,data):
        resp = self._spi.xfer2(data)

    def rec_data(self,len):
        resp = self._spi.readbytes(len)
        print(resp)
        
