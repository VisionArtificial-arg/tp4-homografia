import cv2

from tp4_homografia.domain import Point
from tp4_homografia.domain.state_machine.state_event import (
    CancelSelectionEvent,
    EndSelectionEvent,
    StateEvent,
)


class OpenCVQRDetector:
    def __init__(
        self,
    ) -> None:

        self._detector = cv2.QRCodeDetector()

    def detect(
        self,
        frame,
        padding_factor: float = 1.15,
    ) -> StateEvent:
        success, corners = self._detector.detect(
            frame,
        )
        if not success:
            return CancelSelectionEvent()
        points = tuple(
            Point(
                x=float(corner[0]),
                y=float(corner[1]),
            )
            for corner in corners[0]
        )
        padded_points = self._expand_quad(
            points,
            padding_factor,
        )
        return EndSelectionEvent(
            padded_points,
        )

    def _expand_quad(
        self,
        points: tuple[Point, ...],
        factor: float,
    ) -> tuple[Point, ...]:
        center_x = sum(point.x for point in points) / 4.0
        center_y = sum(point.y for point in points) / 4.0
        expanded = []
        for point in points:
            dx = point.x - center_x
            dy = point.y - center_y
            expanded.append(
                Point(
                    x=center_x + dx * factor,
                    y=center_y + dy * factor,
                )
            )
        return tuple(
            expanded,
        )
