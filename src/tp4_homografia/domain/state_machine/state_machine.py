from .state_event import (
    CancelSelectionEvent,
    EndSelectionEvent,
    NoActionEvent,
    StartManualSelectionEvent,
    StateEvent,
    StopEvent,
)
from .states import State, FinalState, ManualSelectionState, VisualizationState


class StateMachine:
    def __init__(self):
        self._current = VisualizationState()

    @property
    def current(self) -> State:
        return self._current

    def transition(
        self,
        event: StateEvent,
    ):
        match event:
            case NoActionEvent():
                return
            case StopEvent():
                self._current = FinalState()
            case StartManualSelectionEvent():
                self._current = ManualSelectionState()
                print("Entered manual selection")
            case EndSelectionEvent():
                print("Selection ended")
                self._current = VisualizationState()
            case CancelSelectionEvent():
                print("Selection canceled")
                self._current = VisualizationState()

    def is_running(self) -> bool:
        return not isinstance(self.current, FinalState)
