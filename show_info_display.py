from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont
import time
import psutil

I2C_PORT = 3

font = ImageFont.truetype("/usr/share/fonts/d2conding/D2Coding/D2Coding-Ver1.3.2-20180524.ttf", 24)

serial = i2c(port=I2C_PORT, address=0x3C)
device = ssd1306(serial)


while True:
    # Vim3 info
    cpu_percent = str(psutil.cpu_percent())
    cpu_run = str(round(psutil.cpu_freq().current/1024, 1))
    cpu_max = str(round(psutil.cpu_freq().max/1024, 1))

    mem = psutil.virtual_memory()
    mem_run = str(round(mem.available/1024**3, 1))
    mem_max = str(round(mem.total/1024**3))

    temps = psutil.sensors_temperatures()
    cpu_temp = str(temps['soc_thermal'][0].current) 
    mem_temp = str(temps['ddr_thermal'][0].current)
    
    with canvas(device) as draw:
        #font = ImageFont.load_default()

        draw.text((0, 0), f'CPU {cpu_percent}%', fill="white", font=font)
        draw.text((0, 22), f'MEM {mem_run}GB', fill="white", font=font)
        draw.text((0, 45), f'TEM {cpu_temp}˚C', fill="white", font=font)
        

        time.sleep(1)
    