from .state_event import (
    EndSelectionEvent,
    NoActionEvent,
    StartManualSelectionEvent,
    StateEvent,
    StopEvent,
)
from .states import State, FinalState, ManualSelectionState, VisualizationState


class StateMachine:
    def __init__(self):
        self._state = VisualizationState()

    @property
    def current(self) -> State:
        return self._state

    def transition(
        self,
        event: StateEvent,
    ):
        match event:
            case NoActionEvent():
                return
            case StopEvent():
                self._state = FinalState()
            case StartManualSelectionEvent():
                self._state = ManualSelectionState()
                print("Entered manual selection")
            case EndSelectionEvent():
                print("Selection ended")

    def is_running(self) -> bool:
        return not isinstance(self.current, FinalState)
