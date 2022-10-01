from manim import *
from manim_slides import Slide

import numpy as np


title = Title("Komplex számok")


class Complex(Slide):
    def construct(self):
        General.construct(self)
        Example.construct(self)
        Notations.construct(self)
        Interactive.construct(self)


class General(Slide):
    def construct(self):
        blist = BulletedList(
            r"A valós ($\mathbb {R}$) számok sok esetben kényelmesek.",
            r"A másodfokú egyenleteknek viszont negatív\\diszkrimináns esetén lehet nem valós megoldásuk is",
            r"Ezeket az eseteket is szeretnénk kezelni,\\ezért bevezetjük a komplex számokat",
            r"A komplex számok halmaza a valós számok\\halmazának bővítése, jelölése: $\mathbb C$",
        ).scale(0.8)

        # Animation begins here
        self.play(Write(title))
        self.pause()

        self.play(FadeIn(blist))
        self.pause()

        self.play(FadeOut(blist))
        self.pause()


class Example(Slide):
    def construct(self):
        # Example Equations
        math_base = MathTex("x^2 - 2x + 2 = 0").next_to(title, DOWN, buff=0.5)
        eq1 = MathTex(r"{{x_{12}}} = \frac{2 \pm \sqrt{2^2 - 4 \cdot 1 \cdot 2}}{2}")
        eq2 = MathTex(r"{{x_{12}}} = \frac{2 \pm \sqrt{4 - 8}}{2}")
        eq3 = MathTex(r"{{x_{12}}} = \frac{2 \pm \sqrt{-4}}{2}")
        eq4 = MathTex(r"{{x_{12}}} = \frac{2 \pm 2\sqrt{-1}}{2}")
        eq5 = MathTex(r"{{x_{12}}} = 1 \pm \sqrt{-1}")
        eq6 = MathTex(r"{{x_{12}}} = 1 \pm i")
        math_end = eq6.copy().next_to(title, DOWN).to_edge(LEFT)

        # Axes
        ax = Axes(
            x_range=(-2, 2.5),
            y_range=(-2, 2.5),
            x_length=6.5,
            y_length=6.5,
        ).shift(0.75 * DOWN)
        x_label = ax.get_x_axis_label(r"\Re")
        y_label = ax.get_y_axis_label(r"\Im")

        g = VGroup(ax, x_label, y_label)

        # Solutions on the plane
        d1 = Dot(ax.coords_to_point(1, 1), color=GREEN)
        d2 = Dot(ax.coords_to_point(1, -1), color=GREEN)
        label1 = MathTex("1+i").next_to(d1, UR, 0.1)
        label2 = MathTex("1-i").next_to(d2, DR, 0.1)

        p1 = VGroup(d1, label1)
        p2 = VGroup(d2, label2)
        p = VGroup(p1, p2)

        # Animation begins here
        self.add(title)

        # Write base equation
        self.play(Write(math_base))
        self.pause()

        # Transfrom equation
        self.play(Write(eq1))
        self.pause()
        self.play(TransformMatchingTex(eq1, eq2))
        self.pause()
        self.play(TransformMatchingTex(eq2, eq3))
        self.pause()
        self.play(TransformMatchingTex(eq3, eq4))
        self.pause()
        self.play(TransformMatchingTex(eq4, eq5))
        self.pause()
        self.play(TransformMatchingTex(eq5, eq6))
        self.pause()

        # Move solution to top left
        self.play(Unwrite(math_base))
        self.wait()
        self.play(Transform(eq6, math_end))
        self.pause()

        # Show plot
        self.play(Create(g))
        self.pause()

        # 1st solution
        self.play(Write(d1), Write(label1))
        self.pause()

        # 2nd solution
        self.play(Write(d2), Write(label2))
        self.pause()

        # Cleanup
        self.play(Unwrite(eq6), Uncreate(g), Unwrite(p))

        # Scene ends here
        self.wait()


class Notations(Slide):
    def construct(self):
        # Text
        notation = (
            Text("Matematikai leírásmódok:")
            .next_to(title, DOWN, buff=0.5)
            .to_edge(LEFT)
        )
        alg_text = (
            Text("1, Algebrai alak")
            .next_to(notation, DOWN * 2)
            .scale(0.8)
            .to_edge(LEFT)
            .shift(0.5 * RIGHT)
        )
        alg_math = (
            MathTex(r"z = a + bi").next_to(alg_text, DOWN).to_edge(LEFT).shift(RIGHT)
        )
        trig_text = (
            Text("2, Trigonometrikus alak")
            .next_to(alg_math, 1.5 * DOWN)
            .scale(0.8)
            .to_edge(LEFT)
            .shift(0.5 * RIGHT)
        )
        trig_math = (
            MathTex(r"z = r(\cos \varphi + i \sin \varphi)")
            .next_to(trig_text, DOWN)
            .to_edge(LEFT)
            .shift(RIGHT)
        )

        polar_text = (
            Text("3, Exponenciális alak")
            .next_to(trig_math, 1.5 * DOWN)
            .scale(0.8)
            .to_edge(LEFT)
            .shift(0.5 * RIGHT)
        )
        polar_math = (
            MathTex(r"z = r e^{i \varphi}")
            .next_to(polar_text, DOWN)
            .to_edge(LEFT)
            .shift(RIGHT)
        )

        alg_g = VGroup(alg_text, alg_math)
        trig_g = VGroup(trig_text, trig_math)
        polar_g = VGroup(polar_text, polar_math)
        notation_g = VGroup(notation, alg_g, trig_g, polar_g)

        # Axes
        ax = (
            Axes(
                x_range=(-0.2, 2.8),
                y_range=(-1.2, 3.8),
                x_length=3,
                y_length=5,
            )
            .to_edge(DR)
            .shift(LEFT)
        )
        x_label = ax.get_x_axis_label(r"\Re")
        y_label = ax.get_y_axis_label(r"\Im")

        # Coordinates
        dot_o = Dot(ax.coords_to_point(0, 0), color=GREEN)
        dot_a = Dot(ax.coords_to_point(2, 0), color=GREEN)
        dot_b = Dot(ax.coords_to_point(0, 3), color=GREEN)
        dot_r = Dot(ax.coords_to_point(2, 3), color=GREEN)

        # Helper lines
        line_a = Line(dot_o.get_center(), dot_a.get_center(), color=YELLOW)
        line_b = Line(dot_a.get_center(), dot_r.get_center(), color=YELLOW)
        line_r = Line(dot_o.get_center(), dot_r.get_center(), color=RED)
        lines = VGroup(line_r, line_a, line_b)

        # Braces to mark parameters a, b, r
        brace_a = Brace(line_a)
        text_a = brace_a.get_tex("a")
        brace_b = Brace(
            line_b, direction=line_b.copy().rotate(-PI / 2).get_unit_vector()
        )
        text_b = brace_b.get_tex("b")
        brace_r = Brace(
            line_r, direction=line_r.copy().rotate(PI / 2).get_unit_vector()
        )
        text_r = brace_r.get_tex("r")

        # Angle to mark phi
        angle = Angle(line_a, line_r, radius=1.2)
        text_angle = MathTex(r"\varphi").next_to(dot_o, 1.5 * RIGHT + 0.5 * UP)

        # Animation begins here
        self.add(title)

        # Header
        self.play(Write(notation))
        self.pause()

        # Alg
        self.play(Write(alg_g))
        self.play(Create(ax), Write(x_label), Write(y_label))
        self.play(Create(dot_r), Create(lines))
        self.play(Create(brace_a), Write(text_a), Create(brace_b), Write(text_b))
        self.pause()

        # Trig
        self.play(Write(trig_g))
        self.play(FadeOut(brace_a), FadeOut(text_a), FadeOut(brace_b), FadeOut(text_b))
        self.play(Create(brace_r), Write(text_r), Create(angle), Write(text_angle))
        self.pause()

        # Polar
        self.play(Write(polar_g))
        self.pause()

        # Cleanup
        self.play(
            Unwrite(title),
            Unwrite(notation_g),
            FadeOut(lines),
            FadeOut(dot_r),
            FadeOut(angle),
            FadeOut(text_angle),
            FadeOut(brace_r),
            FadeOut(text_r),
            FadeOut(ax),
            FadeOut(x_label),
            FadeOut(y_label),
        )

        # End of scene
        self.wait()


class Interactive(Slide):
    def construct(self):
        # Basic mobjects
        plane = NumberPlane()
        circle = Circle(radius=3)
        dot = Dot(color=YELLOW)
        horizontal = Line(LEFT, RIGHT)
        vertical = Line(ORIGIN, UP)

        # Helper functions
        def get_line():
            return Line(ORIGIN, dot.get_center(), color=RED)

        def get_real_line():
            return Line(ORIGIN, np.array([dot.get_x(), 0.0, 0.0]), color=GREEN)

        def get_imaginary_line():
            return Line(
                np.array([dot.get_x(), 0.0, 0.0]),
                np.array([dot.get_x(), dot.get_y(), 0.0]),
                color=GREEN,
            )

        # Helper lines
        line = always_redraw(get_line)
        re_line = always_redraw(get_real_line)
        im_line = always_redraw(get_imaginary_line)

        # Braces
        re_brace = always_redraw(lambda: Brace(line))
        im_brace = always_redraw(
            lambda: Brace(line, direction=re_line.get_unit_vector())
        )
        re_text = always_redraw(lambda: re_brace.get_tex("a"))
        im_text = always_redraw(lambda: im_brace.get_tex("b"))

        # Angle -- TODO: add angle
        # angle = Angle(horizontal, vertical)
        # angle.add_updater(lambda x: x.become(Angle(horizontal, line)))

        # Animation starts here
        self.play(Create(plane))
        self.add(line, re_line, im_line, re_brace, im_brace, re_text, im_text)
        self.pause()

        self.start_loop()
        self.play(MoveAlongPath(dot, circle), run_time=8, rate_func=linear)
        self.end_loop()

        # End of scene
        self.wait()


# class OldInteractive(Slide):
#     def construct(self):
#         plane = NumberPlane()
#         circle = Circle(radius=3)
#         dot = Dot(color=YELLOW)
#
#         def get_line():
#             return Line(ORIGIN, dot.get_center(), color=RED)
#
#         def get_real_line():
#             return Line(ORIGIN, np.array([dot.get_x(), 0.0, 0.0]), color=GREEN)
#
#         def get_imaginary_line():
#             return Line(
#                 np.array([dot.get_x(), 0.0, 0.0]),
#                 np.array([dot.get_x(), dot.get_y(), 0.0]),
#                 color=GREEN,
#             )
#
#         def get_angle(x, y):
#             a = np.arctan(y / x)
#
#             if y >= 0:
#                 if x >= 0:
#                     return a
#                 else:
#                     return a + PI
#             else:
#                 if x >= 0:
#                     return a + 2 * PI
#                 else:
#                     return a + PI
#
#         line = always_redraw(get_line)
#         re_line = always_redraw(get_real_line)
#         im_line = always_redraw(get_imaginary_line)
#
#         self.add(Tex("alma"))
#
#         re = DecimalNumber(3)
#         im = DecimalNumber(0)
#         r = DecimalNumber(3)
#         phi = DecimalNumber(0)
#         phi_dec = DecimalNumber(0)
#
#         re.add_updater(lambda x: x.set_value(dot.get_x()))
#         im.add_updater(lambda x: x.set_value(dot.get_y()))
#         phi.add_updater(
#             lambda x: x.set_value(get_angle(re.get_value(), im.get_value()))
#         )
#         phi_dec.add_updater(lambda x: x.set_value(phi.get_value() / PI * 180))
#
#         re_text = MathTex(r"\mathrm{Re} \; z = ").to_corner(UL)
#         im_text = MathTex(r"\mathrm{Im} \; z = ").next_to(re_text, DOWN).to_edge(LEFT)
#         r_text = MathTex(r"r = ").next_to(im_text, DOWN).to_edge(LEFT)
#         phi_text = MathTex(r"\varphi = ").next_to(r_text, DOWN).to_edge(LEFT)
#
#         re.next_to(re_text, RIGHT)
#         im.next_to(im_text, RIGHT)
#         r.next_to(r_text, RIGHT)
#         phi.next_to(phi_text, RIGHT)
#
#         g = VGroup(re, im, r, phi)
#         g_text = VGroup(re_text, im_text, r_text, phi_text)
#
#         self.play(Create(plane))
#         self.add(line, re_line, im_line, g, g_text)
#         self.pause()
#
#         self.start_loop()
#         self.play(MoveAlongPath(dot, circle), run_time=5, rate_func=linear)
#         self.end_loop()
#
#         self.wait()
