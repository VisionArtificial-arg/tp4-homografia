from tp4_homografia.domain.homography import Homography
from tp4_homografia.domain.point import Point
from .abstract import HomographyService
import numpy as np
import cv2


class OpenCVHomographyService(
    HomographyService,
):
    def compute(
        self,
        source: tuple[Point, ...],
        destination: tuple[Point, ...],
    ) -> Homography:

        source_array = np.array([[p.x, p.y] for p in source], dtype=np.float64)

        destination_array = np.array(
            [[p.x, p.y] for p in destination], dtype=np.float64
        )

        matrix = cv2.getPerspectiveTransform(
            source_array,
            destination_array,
        )

        return Homography(
            matrix=matrix,
        )
