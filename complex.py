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
        Operations.construct(self)


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
        # tracker = ComplexValueTracker()
        # tracker.add_updater(
        #     lambda x: x.animate.set_value(dot.get_x() + dot.get_y() * 1j)
        # )

        # Helper functions
        def get_line():
            return Arrow(ORIGIN, dot.get_center(), color=RED, buff=0)

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
        re_text = always_redraw(
            lambda: re_brace.get_tex(f"a = {np.round(dot.get_x(),2)}")
        )
        im_text = always_redraw(
            lambda: im_brace.get_tex(f"b = {np.round(dot.get_y(),2)}")
        )

        def get_angle(r):
            v1 = line.get_unit_vector()
            v2 = horizontal.get_unit_vector()

            if np.abs(v1[0] == v2[0]):
                return False

            return Angle(horizontal, line, radius=r, color=YELLOW)

        def angle_updater(x):
            angle = get_angle(1)

            if angle == False:
                return

            return x.become(angle)

        def phi_updater(x):
            angle = get_angle(1.5)

            if angle == False:
                return

            return x.move_to(angle.point_from_proportion(0.5))

        # Angle -- TODO: add angle
        angle = Angle(horizontal, vertical)
        angle.add_updater(angle_updater)
        phi = MathTex(r"\varphi")
        phi.add_updater(phi_updater)

        # Animation starts here
        self.play(Create(plane))
        self.add(
            line, re_line, im_line, re_brace, im_brace, re_text, im_text, angle, phi
        )
        self.pause()

        self.start_loop()
        self.play(MoveAlongPath(dot, circle), run_time=6, rate_func=linear)
        self.end_loop()

        # Cleanup
        self.play(Uncreate(plane))
        self.play(
            FadeOut(
                VGroup().add(
                    line,
                    re_line,
                    im_line,
                    re_brace,
                    im_brace,
                    re_text,
                    im_text,
                    dot,
                    angle,
                    phi,
                )
            )
        )

        # End of scene
        self.wait()


class Operations(Slide):
    def construct(self):
        # Opetaions
        title1 = Title("Műveletek -- ", " Konjugált")
        title2 = Title("Műveletek -- ", " Inverz")
        title3 = Title("Műveletek -- ", " Összeadás / kivonás")
        title4 = Title("Műveletek -- ", " Szorzás")
        title5 = Title("Műveletek -- ", " Hatványozás")
        title6 = Title("Műveletek -- ", " Gyökvonás")

        # Math notation
        math1 = MathTex(r"\overline z = \overline{(a + bi)} = a - bi").next_to(
            title1, DOWN, buff=0.5
        )
        math2 = MathTex(
            r"z^{-1}",
            r"= \frac{1}{z}",
            r"= \frac{\overline z}{z \overline z}",
            r"= \frac{a - bi}{a^2 + b^2}",
        ).next_to(title2, DOWN, buff=0.5)
        math3 = MathTex(r"z_1 + z_2 = (a_1 + a_2) + i (b_1 + b_2)").next_to(
            title3, DOWN, buff=0.5
        )
        math4_a = MathTex(
            r"z_1 \cdot z_2",
            r"= r_1 r_2 (\cos(\varphi_1 + \varphi_2) + i\sin(\varphi_1 + \varphi_2))",
        ).next_to(title4, DOWN, buff=0.5)
        math4_b = MathTex(
            r"z_1 \cdot z_2",
            r"= r_1 r_2 e^{i(\varphi_1 + \varphi_2)}",
        ).next_to(title4, DOWN, buff=0.5)
        math5 = MathTex(
            r"z^n",
            r"=r^n (\cos(n \varphi) + i \sin(n \varphi))",
            r"=r^n e^{i n \varphi}",
        ).next_to(title5, DOWN, buff=0.5)
        math6_a = MathTex(
            r"\sqrt[n]{z}",
            r"=\sqrt[n]{r} \left( \cos \frac{\varphi + 2k\pi}{n} + i \sin \frac{\varphi + 2k\pi}{n} \right)",
        ).next_to(title6, DOWN, buff=0.5)
        math6_b = MathTex(
            r"\sqrt[n]{z}",
            r"=\sqrt[n]{r} e^{i \frac{\varphi + 2k\pi}{n}} \qquad k \in \{0,1, \dots, n-1\}",
        ).next_to(title6, DOWN, buff=0.5)

        # Axes
        ax = Axes(
            x_range=(-2, 2.5),
            y_range=(-2, 2.5),
            x_length=5,
            y_length=5,
        ).shift(2 * DOWN)
        x_label = ax.get_x_axis_label(r"\Re")
        y_label = ax.get_y_axis_label(r"\Im")

        g = VGroup(ax, x_label, y_label)

        # Vectors
        center = ax.coords_to_point(0, 0)

        # No.1
        z11 = ax.coords_to_point(2, 1.5)
        z12 = ax.coords_to_point(2, -1.5)

        z11_vec = Arrow(center, z11, color=BLUE, stroke_width=8, buff=0)
        z11_tex = MathTex("z").next_to(z11, RIGHT)
        z12_vec = Arrow(center, z12, color=RED, stroke_width=8, buff=0)
        z12_tex = MathTex(r"\overline z").next_to(z12, RIGHT)
        g1 = Group(z11_vec, z11_tex, z12_vec, z12_tex)

        # No.2
        z21 = z11.copy()
        z22 = ax.coords_to_point(
            2 / np.sqrt(2**2 + 1.5**2), -1.5 / np.sqrt(2**2 + 1.5**2)
        )

        z21_vec = Arrow(center, z21, color=BLUE, stroke_width=8, buff=0)
        z21_tex = MathTex("z").next_to(z21, RIGHT)
        z22_vec = Arrow(center, z22, color=RED, stroke_width=8, buff=0)
        z22_tex = MathTex(r"z^{-1}").next_to(z22, RIGHT)
        g2 = Group(z21_vec, z21_tex, z22_vec, z22_tex)

        # No.3
        z31 = ax.coords_to_point(2, 0.5)
        z32 = ax.coords_to_point(-1, 1)
        z33 = ax.coords_to_point(1, 1.5)

        z31_vec = Arrow(center, z31, color=BLUE, stroke_width=8, buff=0)
        z31_tex = MathTex("z_1").next_to(z31, RIGHT)
        z32_vec = Arrow(center, z32, color=BLUE, stroke_width=8, buff=0)
        z32_tex = MathTex("z_2").next_to(z32, LEFT)
        z33_vec = Arrow(center, z33, color=RED, stroke_width=8, buff=0)
        z33_tex = MathTex(r"z_1 + z_2").next_to(z33, UR)

        l31 = DashedLine(z31, z33, color=GREEN)
        l32 = DashedLine(z32, z33, color=GREEN)

        g3 = Group(z31_vec, z31_tex, z32_vec, z32_tex, z33_vec, z33_tex, l31, l32)

        # No.4
        z41 = ax.coords_to_point(1.5, 1)
        z42 = ax.coords_to_point(0.5, 1)
        z43 = ax.coords_to_point(-1.25, 3.5)

        z41_vec = Arrow(center, z41, color=BLUE, stroke_width=8, buff=0)
        z41_tex = MathTex("z_1").next_to(z41, RIGHT)
        z42_vec = Arrow(center, z42, color=BLUE, stroke_width=8, buff=0)
        z42_tex = MathTex("z_2").next_to(z42, RIGHT)
        z43_vec = Arrow(center, z43, color=RED, stroke_width=8, buff=0)
        z43_tex = MathTex(r"z_1 \cdot z_2").next_to(z43, LEFT)

        g4 = Group(z41_vec, z41_tex, z42_vec, z42_tex, z43_vec, z43_tex)

        # No.5
        z5 = 9

        def get_nth_power(b, n):
            t = b**n
            return [np.real(t), np.imag(t)]

        z5_vec = []
        z5_tex = []
        for k in range(z5):
            [x, y] = get_nth_power(0.9 + 0.7j, k + 1)
            z5_vec.append(
                Arrow(
                    center, ax.coords_to_point(x, y), buff=0, color=BLUE, stroke_width=8
                )
            )
            z5_tex.append(
                MathTex(f"z^{k + 1}").move_to(
                    ax.coords_to_point(
                        ((1.14 ** (k + 1) + 0.35) * np.cos((k + 1) * 0.661)),
                        ((1.14 ** (k + 1) + 0.35) * np.sin((k + 1) * 0.661)),
                    )
                )
            )

        g5 = VGroup(*z5_vec, *z5_tex)

        # No.6
        z6 = 8

        def get_nth_roots(n):
            list = []
            for k in range(n):
                list.append(
                    [1.75 * np.cos(2 * k * np.pi / n), 1.75 * np.sin(2 * k * np.pi / n)]
                )

            return list

        z6_in = []
        z6_out = []
        g6 = VGroup()
        for k in range(z6):
            roots = get_nth_roots(k + 1)
            # group = VGroup()
            z6_in.append([])
            z6_out.append([])
            for v in range(k + 1):
                # group.add(
                a = Arrow(
                    center,
                    ax.coords_to_point(roots[v][0], roots[v][1]),
                    buff=0,
                    color=BLUE,
                    stroke_width=8,
                )
                t = MathTex(
                    # r"e^{\frac{",
                    # 2 * v,
                    # r" \pi }{ ",
                    # k + 1,
                    # r"}i}",
                    f"e^{{\\frac{{{2 * v} \\pi}}{{{k + 1}}}i}}"
                )
                t.move_to(ax.coords_to_point(roots[v][0], roots[v][1]))
                t.shift(
                    (
                        UP * np.cos(v * 2 * np.pi / (k + 1))
                        - RIGHT * np.sin(v * 2 * np.pi / (k + 1))
                    )
                    * 0.6
                )

                # t = MathTex(
                #     f"{np.round(roots[v][0] / 1.75,2)}{'+' if roots[v][1] >= 0 else ''}{np.round(roots[v][1] / 1.75, 2)}i",
                # ).move_to(ax.coords_to_point(1.25 * roots[v][0], 1.25 * roots[v][1]))
                z6_in[k].append(Create(a))
                z6_in[k].append(Write(t))
                z6_out[k].append(FadeOut(a))
                z6_out[k].append(FadeOut(t))
                g6.add(a)
                g6.add(t)
            # z6_vec.append(group)

        # Animation begins here
        self.play(Write(title1), Write(math1))
        self.pause()
        self.play(Create(g))
        self.play(Create(z11_vec), Write(z11_tex))
        self.pause()
        self.play(Create(z12_vec), Write(z12_tex))
        self.pause()

        self.play(FadeOut(math1), FadeOut(g1))
        self.play(ReplacementTransform(title1, title2), Write(math2))
        self.pause()
        self.play(Create(z21_vec), Write(z21_tex))
        self.pause()
        self.play(Create(z22_vec), Write(z22_tex))
        self.pause()

        self.play(FadeOut(math2), FadeOut(g2))
        self.play(ReplacementTransform(title2, title3), Write(math3))
        self.pause()
        self.play(Create(z31_vec), Write(z31_tex), Create(z32_vec), Write(z32_tex))
        self.pause()
        self.play(Create(l31), Create(l32), Create(z33_vec), Write(z33_tex))
        self.pause()

        self.play(FadeOut(math3), FadeOut(g3))
        self.play(ReplacementTransform(title3, title4), Write(math4_a))
        self.pause()
        self.play(ReplacementTransform(math4_a, math4_b))
        self.pause()
        self.play(Create(z41_vec), Write(z41_tex), Create(z42_vec), Write(z42_tex))
        self.pause()
        self.play(Create(z43_vec), Write(z43_tex))
        self.pause()

        self.play(FadeOut(math4_b), FadeOut(g4))
        self.play(ReplacementTransform(title4, title5), Write(math5))
        self.play(g.animate.shift(1.25 * UP))
        g5.shift(1.25 * UP)
        self.pause()
        for i in range(z5):
            self.play(Create(z5_vec[i]), Write(z5_tex[i]))
            if i == 0:
                self.pause()
        self.pause()

        self.play(FadeOut(math5), FadeOut(g5))
        self.play(g.animate.shift(1.25 * DOWN))
        self.play(ReplacementTransform(title5, title6), Write(math6_a))
        self.pause()
        self.play(ReplacementTransform(math6_a, math6_b))
        self.play(g.animate.shift(UP))
        g6.shift(UP)
        self.pause()
        for k in range(z6):
            if k != 0:
                self.play(*z6_out[k - 1])
            self.play(*z6_in[k])
        self.pause()

        # Cleanup
        self.play(FadeOut(math6_b), *z6_out[z6 - 1], FadeOut(g), FadeOut(title6))

        # Scene ends here
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
