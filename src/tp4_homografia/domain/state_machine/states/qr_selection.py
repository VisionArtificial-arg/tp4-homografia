from ..state_event import DetectQrEvent, StateEvent, NoActionEvent
from .abstract import State


class QrPreDetectionState(State):
    def update(self, frame) -> StateEvent:
        return NoActionEvent()

    def handle_click(self, x: int, y: int) -> StateEvent:
        return NoActionEvent()

    def handle_key(self, key: int) -> StateEvent:
        if key != 255:
            return DetectQrEvent()
        return NoActionEvent()
