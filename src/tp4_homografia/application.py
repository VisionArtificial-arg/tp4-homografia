import cv2

from .interaction.input_conctroller import InputController
from .domain.state_machine import StateMachine
from .states import VisualizationState
from .infrastructure import Camera


class Application:
    def __init__(self) -> None:
        self.camera = Camera()
        self.state_machine: StateMachine = StateMachine(VisualizationState())
        self.running = True
        self.input_controller: InputController = InputController(self.state_machine)

    def run(self):
        while self.running:
            frame = self.camera.read()
            cv2.imshow("Perspective", frame)
            key = cv2.waitKey(1)

            if key == 27:
                self.running = False

            self.state_machine.current.update(frame)
        self.camera.release()
