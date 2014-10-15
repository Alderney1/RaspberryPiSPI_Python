from spi import SPI

s = SPI()
s.send_data([0x1A])
s.rec_data(len=4)
