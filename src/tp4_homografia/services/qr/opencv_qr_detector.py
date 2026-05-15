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
    ) -> StateEvent:

        success, corners = self._detector.detect(
            frame,
        )

        if not success:
            return CancelSelectionEvent()

        points = []

        for corner in corners[0]:
            x = float(
                corner[0],
            )

            y = float(
                corner[1],
            )

            points.append(
                Point(
                    x=x,
                    y=y,
                )
            )

        return EndSelectionEvent(
            tuple(
                points,
            )
        )
