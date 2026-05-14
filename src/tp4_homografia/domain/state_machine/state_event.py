from dataclasses import dataclass

from ..point import Point


@dataclass(frozen=True)
class NoActionEvent: ...


@dataclass(frozen=True)
class StopEvent: ...


@dataclass(frozen=True)
class StartManualSelectionEvent: ...


@dataclass(frozen=True)
class CancelSelectionEvent: ...


@dataclass(frozen=True)
class EndSelectionEvent:
    corners: tuple[Point, ...]


StateEvent = (
    NoActionEvent
    | StopEvent
    | StartManualSelectionEvent
    | EndSelectionEvent
    | CancelSelectionEvent
)
