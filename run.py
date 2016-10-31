import bluetooth
import logging
import sys
import time
from car import Car


logging.basicConfig(level=logging.INFO)


def get_cars():
        try:
            logging.info('Searching for nearby bluetooth devices. ʕ •ᴥ•ʔ')
            nearby_devices = bluetooth.discover_devices(lookup_names=True)
            if not nearby_devices:
                logging.critical(
                    'Couldn\'t find any bluetooth devices. ლ(ಠ益ಠლ)'
                )
                return
            logging.info(
                'Finished search, devices found:\n{devices}'.format(
                    devices=nearby_devices
                )
            )
            cars = []
            port = 1
            for mac, name in nearby_devices:
                if 'Micro' in name:
                    logging.info(
                        'Found {name}, {mac}'.format(name=name, mac=mac)
                    )
                    cars.append(Car(name=name, mac=mac, port=port))
                    port += 1
            if not cars:
                logging.critical(
                    'Couldn\'t find any cars. Bailing out. ლ(ಠ益ಠლ)'
                )
                return
            return cars
        except OSError as e:
            logging.critical(
                'Couldn\'t connect to bluetooth. Is it turned on? ಠ_ಠ'
            )
            sys.exit()


if __name__ == '__main__':
    while True:
        cars = get_cars()
        if cars:
            break
    # cars[0].connect()
    cars[0].create_keep_alive()
    while True:
        time.sleep(1)
