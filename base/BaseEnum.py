from enum import Enum


class RobotMode(Enum):
    mastermode = 1
    slavemode = 2
    selfmode = 3


class OS(Enum):
    mac = 'mac'
    win = 'win'
    mumu = 'mumu'

class App(Enum):
    desk = 1
    moniqi = 2


class ScreenSize(Enum):
    size2560 = 1
    size1280 = 2

