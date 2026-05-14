from typing import Deque, Tuple
import cv2

from tp4_homografia.domain import StateMachine
from tp4_homografia.domain.state_machine import StateEvent


from collections import deque


class InputController:
    def __init__(self, state_machine: StateMachine, window_name: str):
        self._state_machine = state_machine
        self._mouse_clicks: Deque[Tuple[int, int]] = deque()
        self._window_name = window_name
        cv2.setMouseCallback(self._window_name, self._on_mouse)

    def _on_mouse(self, event, x: int, y: int, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self._mouse_clicks.append((x, y))

    def poll(self) -> StateEvent:
        key = cv2.waitKey(1) & 0xFF
        if self._mouse_clicks:
            mouse_click = self._mouse_clicks.popleft()
            return self._state_machine.current.handle_click(
                mouse_click[0], mouse_click[1]
            )
        return self._state_machine.current.handle_key(key)
