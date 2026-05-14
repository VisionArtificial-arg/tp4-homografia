from enum import Enum


class StateEvent(Enum):
    NO_ACTION = 1
    STOP = 2
    START_MANUAL_SELECTION = 3
    END_SELECTION = 4
