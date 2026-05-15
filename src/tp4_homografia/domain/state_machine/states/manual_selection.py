from typing import List
from .abstract import State
from ...point import Point
from ..state_event import (
    CancelSelectionEvent,
    EndSelectionEvent,
    NoActionEvent,
    StateEvent,
)


class ManualSelectionState(State):
    def __init__(self):
        self.points: List[Point] = []

    def update(self, frame) -> StateEvent:
        return NoActionEvent()

    def handle_click(self, x, y) -> StateEvent:
        self.points.append(Point(x, y))
        print(f"Click n°: {len(self.points)}")
        if len(self.points) == 4:
            return EndSelectionEvent(tuple(self.points))
        return NoActionEvent()

    def handle_key(self, key: int) -> StateEvent:
        if key != 255:
            return CancelSelectionEvent()
        return NoActionEvent()
