from typing import List
from .abstract import State
from ...point import Point
from ..state_event import (
    CancelSelectionEvent,
    EndSelectionEvent,
    NoActionEvent,
    StateEvent,
)
import numpy as np


class ManualSelectionState(State):
    def __init__(self):
        self.points: List[Point] = []

    def update(self, frame) -> StateEvent:
        return NoActionEvent()

    def handle_click(self, x, y) -> StateEvent:
        self.points.append(Point(x, y))
        print(f"Click n°: {len(self.points)}")
        if len(self.points) == 4:
            return EndSelectionEvent(order_points(tuple(self.points)))
        return NoActionEvent()

    def handle_key(self, key: int) -> StateEvent:
        if key != 255:
            return CancelSelectionEvent()
        return NoActionEvent()


def order_points(
    points: tuple[Point, ...],
) -> tuple[Point, ...]:
    if len(points) != 4:
        raise ValueError(
            "Exactly 4 points required",
        )
    array = np.array(
        [[point.x, point.y] for point in points],
        dtype=np.float32,
    )
    sums = array.sum(
        axis=1,
    )
    diffs = array[:, 0] - array[:, 1]
    tl = array[
        np.argmin(
            sums,
        )
    ]
    br = array[
        np.argmax(
            sums,
        )
    ]
    tr = array[
        np.argmax(
            diffs,
        )
    ]
    bl = array[
        np.argmin(
            diffs,
        )
    ]
    return (
        Point(
            x=float(
                tl[0],
            ),
            y=float(
                tl[1],
            ),
        ),
        Point(
            x=float(
                tr[0],
            ),
            y=float(
                tr[1],
            ),
        ),
        Point(
            x=float(
                br[0],
            ),
            y=float(
                br[1],
            ),
        ),
        Point(
            x=float(
                bl[0],
            ),
            y=float(
                bl[1],
            ),
        ),
    )
