from tp4_homografia.domain.state import State
from tp4_homografia.domain.state_event import StateEvent


class ManualSelectionState(State):
    def __init__(self):
        self.points = []

    def update(self, frame) -> StateEvent:
        return StateEvent.NO_ACTION

    def handle_click(self, x, y) -> StateEvent:

        self.points.append(
            (x, y),
        )
        return StateEvent.NO_ACTION

    def handle_key(self, key: int) -> StateEvent:
        return StateEvent.NO_ACTION
