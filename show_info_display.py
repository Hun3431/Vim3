from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont
import time
import psutil

I2C_PORT = 3
FONT = ('Arial',10)

serial = i2c(port=I2C_PORT, address=0x3C)
device = ssd1306(serial)

while True:
    cpu = f'{str(psutil.cpu_percent())}'
    cpu_run = f'{str(round(psutil.cpu_freq().current/1024, 1))}/{str(round(psutil.cpu_freq().max/1024, 1))}GHz'
    mem = psutil.virtual_memory()
    mem_run = f'{str(round(mem.available/1024**3, 1))}/{str(round(mem.total/1024**3))}GB'
    
    with canvas(device) as draw:
        font = ImageFont.load_default()
        draw.text((10, 1), "Hello World!", fill="white", font=font)
        draw.text((10, 11), f'CPU {cpu} {cpu_run}', fill="white", font=font)
        draw.text((10, 21), f'MEM {mem_run}', fill="white", font=font)

    