import bluetooth
import logging
import sys
from car import Car


logging.basicConfig(level=logging.INFO)


def get_cars():
    try:
        logging.info('Searching for nearby bluetooth devices. ʕ •ᴥ•ʔ')
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        if not nearby_devices:
            logging.critical(
                'Couldn\'t find any bluetooth devices. Bailing out. ლ(ಠ益ಠლ)'
            )
            sys.exit()
        logging.info(
            'Finished search, devices found:\n{devices}'.format(
                devices=nearby_devices
            )
        )
        cars = []
        for mac, name in nearby_devices:
            if 'Micro' in name:
                logging.info('Found {name}, {mac}'.format(name=name, mac=mac))
                cars.append(Car(name=name, mac=mac))
        if not cars:
            logging.critical(
                'Couldn\'t find any cars. Bailing out. ლ(ಠ益ಠლ)'
            )
            sys.exit()
        return cars
    except OSError as e:
        logging.critical(
            'Couldn\'t connect to bluetooth. Is it turned on? ಠ_ಠ'
        )
        sys.exit()


def create_bt_socket():
    logging.info('Creating bluetooth socket. \( ﾟヮﾟ)/')
    return bluetooth.BluetoothSocket(bluetooth.RFCOMM)


def connect(sock, car, port):
            sock.connect((car.mac, port))
            logging.info('Connected to {name} on port {port}. (⚆ _ ⚆)'.format(
                name=car.name, port=port
            ))


if __name__ == '__main__':
    import binascii
    sock = create_bt_socket()
    cars = get_cars()
    port = 1
    connect(sock, cars[0], port)
    import time
    while True:
        sock.send(binascii.a2b_hex('8500'))
        time.sleep(2.5)
        sock.send(binascii.a2b_hex('8501'))
        time.sleep(2.5)
        sock.send(binascii.a2b_hex('8502'))
        time.sleep(2.5)
