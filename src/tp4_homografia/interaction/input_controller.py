import cv2

from tp4_homografia.domain import StateMachine
from tp4_homografia.domain.state_event import StateEvent


class InputController:
    def __init__(
        self,
        state_machine: StateMachine,
    ):

        self._state_machine = state_machine

    def poll(self) -> StateEvent:

        key = (
            cv2.waitKey(
                1,
            )
            & 0xFF
        )

        return self._state_machine.current.handle_key(
            key,
        )
