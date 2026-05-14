from .state import State
from tp4_homografia.states import FinalState
from .state_event import StateEvent


class StateMachine:
    def __init__(
        self,
        initial_state,
    ):
        self._state = initial_state

    @property
    def current(self) -> State:
        return self._state

    def transition(
        self,
        event: StateEvent,
    ):
        match event:
            case StateEvent.NO_ACTION:
                return
            case StateEvent.STOP:
                self._state = FinalState()
