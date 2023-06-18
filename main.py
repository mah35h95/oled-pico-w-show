from machine import Pin, SPI
from ssd1306 import SSD1306_SPI
import framebuf
from time import sleep
from utime import sleep_ms


def display_logo(oled):
    # Display the Raspberry Pi logo on the OLED
    buffer = bytearray(
        b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    )
    fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)

    oled.fill(0)
    oled.blit(fb, 96, 0)
    oled.show()


spi = SPI(0, 100000, mosi=Pin(19), sck=Pin(18))

# oled = SSD1306_SPI(WIDTH, HEIGHT, spi, dc,rst, cs) use GPIO PIN NUMBERS
oled = SSD1306_SPI(128, 64, spi, Pin(17), Pin(20), Pin(16))

# while True:
#     try:
#         for i in range(40):
#             for j in range(56):
#                 oled.fill(0)
#                 oled.show()
#                 # sleep(1)
#                 oled.text("HELLO WORLD", i, j)
#                 oled.show()
#                 sleep_ms(10)
#     except KeyboardInterrupt:
#         break

oled.fill(0)
oled.show()
oled.text("HELLO WORLD!!", 0, 0)
oled.text("yup HERE we are", 0, 16)
oled.show()

display_logo(oled)

# oled.fill(0)
# oled.show()
