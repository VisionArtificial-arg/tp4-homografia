from .abstract import State
from ..state_event import NoActionEvent, StateEvent


class FinalState(State):
    def update(self, frame) -> StateEvent:
        return NoActionEvent()

    def handle_click(self, x: int, y: int) -> StateEvent:
        return NoActionEvent()

    def handle_key(self, key: int) -> StateEvent:
        return NoActionEvent()
