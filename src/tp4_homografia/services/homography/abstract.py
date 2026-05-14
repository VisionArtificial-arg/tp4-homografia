from abc import ABC, abstractmethod

from tp4_homografia.domain import (
    Homography,
    Point,
)


class HomographyService(ABC):
    @abstractmethod
    def compute(
        self,
        source: tuple[Point, ...],
        destination: tuple[Point, ...],
    ) -> Homography: ...
