import cv2

from .interaction.input_controller import InputController
from .domain.state_machine import StateMachine
from .infrastructure import Camera


class Application:
    def __init__(self) -> None:
        self.camera = Camera()
        self.state_machine: StateMachine = StateMachine()

    def run(self):
        while self.state_machine.is_running():
            frame = self.camera.read()
            cv2.imshow("Perspective", frame)
            self.input_controller: InputController = InputController(
                self.state_machine, "Perspective"
            )
            input_event = self.input_controller.poll()
            self.state_machine.transition(input_event)
            update_event = self.state_machine.current.update(frame)
            self.state_machine.transition(update_event)
        self.camera.release()
