from .abstract import State
from ..state_event import (
    NoActionEvent,
    StartManualSelectionEvent,
    StartQrPreDetectionEvent,
    StateEvent,
    StopEvent,
)


class VisualizationState(State):
    def update(self, frame) -> StateEvent:
        return NoActionEvent()

    def handle_key(self, key: int) -> StateEvent:
        if key == 27:
            return StopEvent()
        elif key == ord("q"):
            return StartQrPreDetectionEvent()
        elif key == ord("h"):
            return StartManualSelectionEvent()
        return NoActionEvent()

    def handle_click(self, x: int, y: int) -> StateEvent:
        return NoActionEvent()
