from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class Homography:
    matrix: np.ndarray
