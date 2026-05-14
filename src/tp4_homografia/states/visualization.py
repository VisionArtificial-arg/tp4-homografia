from tp4_homografia.domain import State
from tp4_homografia.domain.state_event import StateEvent


class VisualizationState(State):
    def update(self, frame) -> StateEvent:
        return StateEvent.NO_ACTION

    def handle_key(self, key: int) -> StateEvent:
        if key == 27:
            return StateEvent.STOP
        elif key == ord("h"):
            return StateEvent.START_MANUAL_SELECTION
        return StateEvent.NO_ACTION

    def handle_click(self, x: int, y: int) -> StateEvent:
        return StateEvent.NO_ACTION
