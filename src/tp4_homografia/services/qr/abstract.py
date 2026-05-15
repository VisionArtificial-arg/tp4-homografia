from abc import ABC, abstractmethod
from ...domain.state_machine import StateEvent


class QRDetector(ABC):
    @abstractmethod
    def detect(
        self,
        frame,
    ) -> StateEvent: ...
