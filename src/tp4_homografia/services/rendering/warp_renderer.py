import cv2

from tp4_homografia.domain.homography import (
    Homography,
)


class WarpRenderer:
    def render(self, frame, homography: Homography, size: int = 300) -> None:

        warped = cv2.warpPerspective(
            frame,
            homography.matrix,
            (size, size),
        )

        cv2.imshow(
            "Warp",
            warped,
        )
