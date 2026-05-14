from tp4_homografia.domain.state import State
from tp4_homografia.domain.state_event import StateEvent


class FinalState(State):
    def update(self, frame) -> StateEvent:
        return StateEvent.NO_ACTION

    def handle_click(self, x: int, y: int) -> StateEvent:
        return StateEvent.NO_ACTION

    def handle_key(self, key: int) -> StateEvent:
        return StateEvent.NO_ACTION
