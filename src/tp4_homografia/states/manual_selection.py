from typing import List
from tp4_homografia.domain import State
from tp4_homografia.domain import StateEvent
from tp4_homografia.domain import Point


class ManualSelectionState(State):
    def __init__(self):
        self.points: List[Point] = []

    def update(self, frame) -> StateEvent:
        return StateEvent.NO_ACTION

    def handle_click(self, x, y) -> StateEvent:
        self.points.append(Point(x, y))
        if len(self.points) == 4:
            return StateEvent.END_SELECTION
        return StateEvent.NO_ACTION

    def handle_key(self, key: int) -> StateEvent:
        return StateEvent.NO_ACTION
