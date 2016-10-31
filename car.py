import attr
import logging
import binascii
import time
import bluetooth
from threading import Thread


def create_bt_socket():
    logging.info('Creating bluetooth socket. \( ﾟヮﾟ)/')
    return bluetooth.BluetoothSocket(bluetooth.RFCOMM)


@attr.s
class Car():
    name = attr.ib()
    mac = attr.ib()
    port = attr.ib()
    # sock = create_bt_socket()

    commands = {
        'no_steer': '8100',
        'light_off': '8500',
        'light_soft': '8501',
        'light_on': '8500',
        'horn_off': '8600',
        'max_left': '8141',
        'max_right': '813F',
        'speed_forward': ['8200','8201','8202','8203','8204','8205','8206','8207','8208','8209','820A','820B','820C','820D','820E','820F','8210','8211','8212','8213','8214','8215','8216','8217','8218','8219','821A','821B','821C','821D','821E','821F','8220','8221','8222','8223','8224','8225','8226','8227','8228','8229','822A','822B','822C','822D','822E','822F','8230','8231','8232','8233','8234','8235','8236','8237','8238','8239','823A','823B','823C','823D','823E','823F'],
        'speed_back': ['827F','827E','827D','827C','827B','827A','8279','8278','8277','8276','8275','8274','8273','8272','8271','8270','826F','826E','826D','826C','826B','826A','8269','8268','8267','8266','8265','8264','8263','8262','8261','8260','825F','825E','825D','825C','825B','825A','8259','8258','8257','8256','8255','8254','8253','8252','8251','8250','824F','824E','824D','824C','824B','824A','8249','8248','8247','8246','8245','8244','8243','8242','8241']
    }

    def connect(self):
        self.sock.connect((self.mac, self.port))
        logging.info('Connected to {name} on port {port}. (⚆ _ ⚆)'.format(
            name=self.name, port=self.port
        ))

    def create_keep_alive(self):
        # self.keep_alive = Thread(target=self.create_keep_alive, args=())
        # self.keep_alive.daemon = True
        # self.keep_alive.start()
        self.sock = create_bt_socket()
        time.sleep(5)
        self.sock.connect((self.mac, self.port))
        self.send_command('no_steer')
        while True:
            try:
                self.send_command('light_soft')
                self.send_command('speed_forward', 5)
                time.sleep(2.5)
                self.send_command('light_off')
                self.send_command('speed_back', 5)
                time.sleep(2.5)
                print('Sending keep alive to {name}'.format(
                    name=self.name
                ))
            except bluetooth._bluetooth.error:
                self.sock = create_bt_socket()
                self.sock.connect((self.mac, self.port))
            except bluetooth.btcommon.BluetoothError:
                self.sock = create_bt_socket()
                self.sock.connect((self.mac, self.port))
            # print('Is alive? {alive}'.format(
            #     alive=self.keep_alive.is_alive()
            # ))

    def send_command(self, command, value=None):
        if value:
            self.sock.send(binascii.a2b_hex(self.commands[command][value]))
        else:
            self.sock.send(binascii.a2b_hex(self.commands[command]))
        logging.info('Sent {command} to {name}'.format(
            name=self.name, command=command
        ))
