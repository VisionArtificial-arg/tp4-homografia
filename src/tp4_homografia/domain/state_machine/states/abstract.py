from abc import ABC, abstractmethod

from ..state_event import StateEvent


class State(ABC):
    @abstractmethod
    def update(self, frame) -> StateEvent: ...

    @abstractmethod
    def handle_key(self, key: int) -> StateEvent: ...

    @abstractmethod
    def handle_click(self, x: int, y: int) -> StateEvent: ...
