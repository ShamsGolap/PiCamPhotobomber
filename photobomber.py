#!/usr/bin/python
from phue import Bridge
from time import sleep
import yaml
import logging
import random

config = yaml.safe_load(open("config.yml"))

logging.basicConfig();

b = Bridge(config['bridge_ip'])
lights = config['lights']
rand = config['rand']
flash_duration = config['flash_duration']

b.connect()

while True:
    randomTime = random.randint(rand[0] * 60, rand[1] * 60)
    print(randomTime)
    sleep(randomTime)

    for light in lights:
        b.set_light(light, 'on', True)
        b.set_light(light, 'xy', [0.3, 0.3])
        b.set_light(light, 'bri', 254)

    sleep(flash_duration)

    for light in lights:
        b.set_light(light, 'on', False)
