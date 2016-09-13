import bluetooth
import logging


logging.basicConfig(level=logging.INFO)


def connect():
    logging.info('Starting bluetooth.')
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    logging.info('Searching for nearby bluetooth devices.')
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    logging.info(
        'Finished search, devices found:\n{devices}'.format(
            devices=nearby_devices
        )
    )
    port = 1
    for mac, name in nearby_devices:
        if 'Micro' in name:
            logging.info(
                'Found {name}, {mac}'.format(name=name, mac=mac)
            )
            sock.connect((mac, port))
            logging.info(
                'Connected to {name} on port {port}'.format(
                    name=name, mac=mac, port=port
                )
            )
            port + 1


connect()
