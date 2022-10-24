from manim import *
from manim_slides import Slide

title = Title("Analitikus geometria")


class Vectors(Slide, ThreeDScene):
    def construct(self):
        General.construct(self)


class General(Slide, ThreeDScene):
    def construct(self):
        # Mobjects, etc
        defi = Tex(
            f"\\flushleft Egy $(v_1, v_2, v_3)$ valós számokból álló rendezett\\\\számhármast a térben ($\\mathbb R^3$) vektornak nevezünk.",
        )

        # 3D axes
        ax = ThreeDAxes().shift(np.array([0, 0, -1]))
        ax.add(ax.get_axis_labels())
        x_lab = ax.get_x_axis_label("x")

        # ax.axis_labels[0].rotate(PI / 2, axis=RIGHT)
        # ax.axis_labels[0].rotate(PI / 2, axis=OUT)
        # ax.axis_labels[1].rotate(PI / 2=RIGHT)
        # ax.axis_labels[1].rotate(PI / 2, axis=OUT)

        g = Group(ax, x_lab)

        # Animation starts here
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        self.pause()

        self.play(FadeIn(defi))
        self.pause()

        self.play(FadeOut(defi))
        self.pause()

        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.play(FadeIn(g))

        # Animation ends here
        self.wait()
