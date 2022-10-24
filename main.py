from manim_slides import Slide
from manim import MovingCameraScene

from sets import Sets
from complex import Complex
from sequences import Sequences
from functions import Functions


class FullScene(Slide, MovingCameraScene):
    def construct(self):
        Sets.construct(self)
        Complex.construct(self)
        Sequences.construct(self)
        Functions.construct(self)
