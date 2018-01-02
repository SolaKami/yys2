from enum import Enum


class RobotMode(Enum):
    mastermode = 1
    slavemode = 2
    selfmode = 3


class OS(Enum):
    mac = 1
    win = 2