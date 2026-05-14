import cv2

from tp4_homografia.domain.homography import (
    Homography,
)


class WarpRenderer:
    def render(
        self,
        frame,
        homography: Homography,
    ) -> None:

        warped = cv2.warpPerspective(
            frame,
            homography.matrix,
            (300, 300),
        )

        cv2.imshow(
            "Warp",
            warped,
        )
