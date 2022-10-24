from manim import *
from manim_slides import Slide

import math as m
import numpy as np

title_1 = Title("Függvények – ", "Határérték")
title_2 = Title("Függvények – ", "Folytonosság")


class Functions(Slide, MovingCameraScene):
    def construct(self):
        General.construct(self)
        Continuity.construct(self)
        self.play(Unwrite(title_2))


class General(MovingCameraScene, Slide):
    def construct(self):
        # Mobjects, etc
        d_d_1 = Tex(
            r"Azt mondjuk, hogy az $f$ függvény határértéke \\ az $a$ pontban $A$, ",
            r"ha $\forall \varepsilon > 0$ esetén $\exists \delta(\varepsilon)$, hogy \\ ",
            r"ha $|x - a| < \delta(\varepsilon)$, akkor $|f(x) - A| < \varepsilon$.",
        ).next_to(title_1, DOWN)

        ax = Axes(
            x_range=(0, 8),
            y_range=(0, 4),
            x_length=8,
            y_length=4,
        ).shift(2 * DOWN)
        x_label = ax.get_x_axis_label(r"x")
        y_label = ax.get_y_axis_label(r"f(x)")

        graph = ax.plot(
            lambda x: x / 10 * (np.sin(3 * x) + np.cos(2 * x) + 3.5),
            x_range=[0, 7.0, 0.01],
            use_smoothing=True,
        )

        d_0 = ax.get_vertical_line(
            ax.input_to_graph_point(6, graph),
            color=BLUE,
            stroke_width=6,
        )
        e_0 = ax.get_horizontal_line(
            ax.input_to_graph_point(6, graph),
            color=RED,
            stroke_width=6,
        )
        p_0 = Dot(ax.input_to_graph_point(6, graph), color=YELLOW)

        limit_lines = Group(d_0, e_0, p_0)

        def get_delta_line(o, d):
            return ax.get_horizontal_line(ax.i2gp(o + d, graph), color=RED)

        def get_epsilon_line(o, e):
            return ax.get_vertical_line(ax.i2gp(o + e, graph), color=BLUE)

        d_plus = get_delta_line(6, 0.5 / 2)
        d_minus = get_delta_line(6, -0.5)
        e_plus = get_epsilon_line(6, 0.5 / 2)
        e_minus = get_epsilon_line(6, -0.5)

        approx_lines_1 = Group(d_plus, d_minus, e_plus, e_minus)

        d_plus = get_delta_line(6, 0.25 / 1.2)
        d_minus = get_delta_line(6, -0.25)
        e_plus = get_epsilon_line(6, 0.25 / 1.2)
        e_minus = get_epsilon_line(6, -0.25)

        approx_lines_2 = Group(d_plus, d_minus, e_plus, e_minus)

        d_plus = get_delta_line(6, 0.125 / 1.1)
        d_minus = get_delta_line(6, -0.125)
        e_plus = get_epsilon_line(6, 0.125 / 1.1)
        e_minus = get_epsilon_line(6, -0.125)

        approx_lines_3 = Group(d_plus, d_minus, e_plus, e_minus)

        g = Group(ax, x_label, y_label, graph)

        # Animation starts here
        self.camera.frame.save_state()

        self.play(Write(title_1))
        self.pause()

        self.play(FadeIn(d_d_1))
        self.pause()

        self.play(FadeIn(g))
        self.pause()

        self.play(FadeIn(limit_lines))
        self.pause()

        self.play(FadeIn(approx_lines_1))
        self.pause()

        self.play(
            self.camera.frame.animate.scale(0.5).move_to(p_0),
            ReplacementTransform(approx_lines_1, approx_lines_2),
        )
        self.pause()

        self.play(
            self.camera.frame.animate.scale(0.25),
            ReplacementTransform(approx_lines_2, approx_lines_3),
        )
        self.pause()

        # Restore Camera
        self.play(Restore(self.camera.frame))
        self.pause()

        # cleanup
        self.play(FadeOut(Group(d_d_1, g, limit_lines, approx_lines_3)))
        self.pause()

        # Animation ends here
        self.wait()


class Continuity(MovingCameraScene, Slide):
    def construct(self):
        # Mobjects, etc
        d_d_1 = Tex(
            r"Azt mondjuk, hogy az $f$ függvény folytonos az \\ $a \in \mathcal D_f$ pontban, ",
            r"ha $\forall \varepsilon > 0$ esetén $\exists \delta(\varepsilon)$, hogy \\ ",
            r"ha $|x - a| < \delta(\varepsilon)$, akkor $|f(x) - f(a)| < \varepsilon$.",
        ).next_to(title_1, DOWN)

        ax = Axes(
            x_range=(0, 7),
            y_range=(0, 4),
            x_length=8,
            y_length=4,
        ).shift(2 * DOWN)
        x_label = ax.get_x_axis_label(r"x")
        y_label = ax.get_y_axis_label(r"f(x)")

        ax_group = Group(ax, x_label, y_label)

        fn_1 = lambda x: x / 2
        graph_1 = ax.plot(
            fn_1,
            x_range=[0, 6.28, 0.01],
        )

        fn_2 = lambda x: np.sign(x - 3.1415) * np.cos(x) + 1
        graph_2a = ax.plot(
            fn_2,
            x_range=[0, 3.13, 0.01],
        )
        graph_2b = ax.plot(
            fn_2,
            x_range=[3.15, 6.28, 0.01],
        )
        graph_2 = Group(graph_2a, graph_2b)

        t_1_minus = ValueTracker(1)
        t_1_plus = ValueTracker(5)
        t_2_minus = ValueTracker(PI - 2)
        t_2_plus = ValueTracker(PI + 2)

        p_1_minus = [ax.coords_to_point(1, fn_1(1))]
        p_1_plus = [ax.coords_to_point(5, fn_1(5))]
        p_2_minus = [ax.coords_to_point(PI - 2, fn_2(PI - 2))]
        p_2_plus = [ax.coords_to_point(PI + 2, fn_2(PI + 2))]

        d_1_minus = Dot(p_1_minus, color=BLUE, radius=0.1)
        d_1_plus = Dot(p_1_plus, color=RED, radius=0.1)
        d_2_minus = Dot(p_2_minus, color=BLUE, radius=0.1)
        d_2_plus = Dot(p_2_plus, color=RED, radius=0.1)

        d_1_minus.add_updater(
            lambda x: x.move_to(
                ax.c2p(t_1_minus.get_value(), fn_1(t_1_minus.get_value()))
            )
        )
        d_1_plus.add_updater(
            lambda x: x.move_to(
                ax.c2p(t_1_plus.get_value(), fn_1(t_1_plus.get_value()))
            )
        )
        d_2_minus.add_updater(
            lambda x: x.move_to(
                ax.c2p(t_2_minus.get_value(), fn_2(t_2_minus.get_value()))
            )
        )
        d_2_plus.add_updater(
            lambda x: x.move_to(
                ax.c2p(t_2_plus.get_value(), fn_2(t_2_plus.get_value()))
            )
        )

        p = ax.c2p(3, 1.5)
        d_0 = ax.get_vertical_line(p, color=YELLOW, stroke_width=6)
        e_0 = ax.get_horizontal_line(p, color=YELLOW, stroke_width=6)
        p_0 = Dot(p, color=YELLOW)

        limits_1 = Group(d_0, e_0, p_0)

        p_p = ax.c2p(PI, fn_2(PI + 0.01))
        p_m = ax.c2p(PI, fn_2(PI - 0.01))
        d_0_p = ax.get_vertical_line(p_p, color=YELLOW, stroke_width=6)
        e_0_p = ax.get_horizontal_line(p_p, color=YELLOW, stroke_width=6)
        d_0_m = ax.get_vertical_line(p_m, color=YELLOW, stroke_width=6)
        e_0_m = ax.get_horizontal_line(p_m, color=YELLOW, stroke_width=6)
        p_0_p = Dot(p_p, color=YELLOW)
        p_0_m = Dot(p_m, color=YELLOW)

        limits_2 = Group(d_0_p, d_0_m, e_0_p, e_0_m, p_0_p, p_0_m)

        # Animation begins here
        self.play(ReplacementTransform(title_1, title_2))
        self.pause()

        self.play(FadeIn(d_d_1))
        self.pause()

        self.play(FadeIn(ax_group))
        self.pause()

        # Case 1 - continous
        self.play(FadeIn(Group(limits_1, graph_1)))
        self.pause()

        self.play(FadeIn(d_1_minus), FadeIn(d_1_plus))
        self.pause()

        self.play(t_1_minus.animate.set_value(3))
        self.pause()

        self.play(t_1_plus.animate.set_value(3))
        self.pause()

        # Case 1 - cleanup
        self.play(FadeOut(Group(limits_1, graph_1, d_1_minus, d_1_plus)))
        self.pause()

        # Case 2 - non continous
        self.play(FadeIn(Group(limits_2, graph_2)))
        self.pause()

        self.play(FadeIn(d_2_minus), FadeIn(d_2_plus))
        self.pause()

        self.play(t_2_minus.animate.set_value(PI - 0.01))
        self.pause()

        self.play(t_2_plus.animate.set_value(PI + 0.01))
        self.pause()

        # cleanup
        self.play(
            FadeOut(Group(ax_group, d_d_1, limits_2, graph_2, d_2_minus, d_2_plus))
        )

        # Animation ends here
        self.wait()
