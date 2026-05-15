from typing import Sequence

import cv2
import numpy as np

from tp4_homografia.domain import (
    Homography,
    Point,
)


class GridRenderer:
    def __init__(self, rows: int = 3, columns: int = 3, plane_size: int = 300) -> None:

        self._rows = rows
        self._columns = columns
        self._cell_size = plane_size / rows

    def render(
        self,
        frame,
        homography: Homography,
    ) -> None:

        frontal_points = self._generate_grid_points()

        projected_points = self._project_to_image(
            frontal_points,
            homography,
        )

        self._draw_grid(
            frame,
            projected_points,
        )

    def _generate_grid_points(
        self,
    ) -> tuple[Point, ...]:

        points: list[Point] = []

        for row in range(
            self._rows + 1,
        ):
            for column in range(
                self._columns + 1,
            ):
                points.append(
                    Point(
                        x=column * self._cell_size,
                        y=row * self._cell_size,
                    )
                )

        return tuple(
            points,
        )

    def _project_to_image(
        self,
        points: Sequence[Point],
        homography: Homography,
    ) -> tuple[Point, ...]:

        frontal_array = np.array(
            [[[point.x, point.y]] for point in points], dtype=np.float32
        )

        inverse_matrix = np.linalg.inv(
            homography.matrix,
        )

        projected_array = cv2.perspectiveTransform(
            frontal_array,
            inverse_matrix,
        )

        projected_points = []

        for point in projected_array:
            x = float(
                point[0][0],
            )

            y = float(
                point[0][1],
            )

            projected_points.append(
                Point(
                    x=x,
                    y=y,
                )
            )

        return tuple(
            projected_points,
        )

    def _draw_grid(
        self,
        frame,
        points: Sequence[Point],
    ) -> None:

        width = self._columns + 1
        height = self._rows + 1

        #
        # horizontal lines
        #

        for row in range(
            height,
        ):
            for column in range(
                width - 1,
            ):
                left_index = row * width + column

                right_index = left_index + 1

                self._draw_line(
                    frame,
                    points[left_index],
                    points[right_index],
                )

        #
        # vertical lines
        #

        for column in range(
            width,
        ):
            for row in range(
                height - 1,
            ):
                top_index = row * width + column

                bottom_index = top_index + width

                self._draw_line(
                    frame,
                    points[top_index],
                    points[bottom_index],
                )

    def _draw_line(
        self,
        frame,
        start: Point,
        end: Point,
    ) -> None:

        cv2.line(
            frame,
            (
                int(
                    start.x,
                ),
                int(
                    start.y,
                ),
            ),
            (
                int(
                    end.x,
                ),
                int(
                    end.y,
                ),
            ),
            (0, 255, 0),
            2,
        )
