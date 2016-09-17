import attr


@attr.s
class Car():
    name = attr.ib()
    mac = attr.ib()
    commands = {
        'light_off': '8500',
        'light_soft': '8501',
        'light_on': '8500'
    }
