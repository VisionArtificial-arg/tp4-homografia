from .state import State
from tp4_homografia.states import FinalState, ManualSelectionState
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
            case StateEvent.START_MANUAL_SELECTION:
                self._state = ManualSelectionState()
                print("Entered manual selection")
            case StateEvent.END_SELECTION:
                print("Selection ended")

    def is_running(self) -> bool:
        return not isinstance(self.current, FinalState)
