from manim import *
from manim_slides import Slide
import numpy as np
import math

title_1 = Title("Numerikus sorozatok – ", "Alapfogalmak")
title_2 = Title("Numerikus sorozatok – ", "Nevezetes sorozatok")
title_3 = Title("Numerikus sorozatok – ", "Rendőr elv")
title_4 = Title("Numerikus sorozatok – ", "Dominancia elv")
title_5 = Title("Numerikus sorozatok – ", "Monotonitás, korlátosság")


class Sequences(Slide):
    def construct(self):
        General.construct(self)
        Examples.construct(self)
        SqueezeTheorem.construct(self)
        Dominance.construct(self)
        Monotonity.construct(self)
        self.play(Unwrite(title_5))


class General(Slide):
    def construct(self):
        # Mobjects, etc
        d_t_1 = Tex(r"\textbf{Def}.: [Numerikus sorozatok]")
        d_t_2 = Tex(r"\textbf{Def}.: [Konvergencia]")

        d_d_1 = Tex(
            r"A pozitív valós számok halmazán értelmezett ",
            r"\\ $a_n : \mathbb N \rightarrow \mathbb R$ ",
            r"függvényt valós sorozatnak, a\\",
            r"$c_n : \mathbb N \rightarrow \mathbb C$ ",
            r"függvényt komplex sorozatnak \\ nevezzük.",
        )

        d_d_2 = Tex(
            r"Az $(a_n)$ sorozatot konvergensnek mondjuk, \\",
            r"ha $\exists$ olyan $a$ valós szám, ",
            r"hogy $\forall \varepsilon > 0$ esetén \\",
            r"$\exists N(\varepsilon)$ küszöbszám, "
            r"ha $n > N(\varepsilon)$, akkor $|a_n - a| < \varepsilon$.",
        )

        d_g_1 = (
            Group(
                Group(d_t_1, d_d_1).arrange(DOWN, buff=0.25),
                Group(d_t_2, d_d_2).arrange(DOWN, buff=0.25),
            )
            .arrange(DOWN, buff=0.5)
            .shift(DOWN / 2)
        )

        # Animation begins here
        self.play(Write(title_1))
        self.pause()

        self.play(FadeIn(d_g_1))
        self.pause()

        # Cleanup
        self.play(FadeOut(d_g_1))
        self.pause()

        # Animations ends here
        self.wait()


class Examples(Slide):
    def construct(self):
        # Mobjects, etc
        ax = Axes(
            x_range=(0, 20),
            y_range=(-1.5, 3.5),
            x_length=8,
            y_length=5,
        ).shift(0.75 * DOWN)
        x_label = ax.get_x_axis_label(r"n")
        y_label = ax.get_y_axis_label(r"a_n")

        g = VGroup(ax, x_label, y_label).shift(DOWN * 0.75)

        min = 1
        max = 20
        sequences = []
        points = []
        lines = []

        def generate_points(function):
            temp = Group()
            for i in range(min, max):
                temp.add(Dot(ax.coords_to_point(i, function(i)), color=GREEN))
            return temp

        def generate_line(x):
            return Line(
                ax.coords_to_point(0, x), ax.coords_to_point(max, x), color=YELLOW
            )

        # e
        sequences.append(
            MathTex(
                r"\lim_{n \rightarrow \infty}",
                r"\left( 1 + \frac{1}{n} \right)^n",
                r"=",
                r"e",
            )
        )
        points.append(generate_points(lambda x: (1 + 1 / x) ** x))
        lines.append(generate_line(2.71))

        # a^n / n!
        sequences.append(
            MathTex(r"\lim_{n \rightarrow \infty}", r"\frac{a^n}{n!}", r"=", r"0")
        )
        points.append(generate_points(lambda x: 2.5**x / math.factorial(x)))
        lines.append(generate_line(0))

        # a^{1 / n}
        sequences.append(
            MathTex(r"\lim_{n \rightarrow \infty}", r"\sqrt[n]{a}", r"=", r"1")
        )
        points.append(generate_points(lambda x: 3 ** (1 / x)))
        lines.append(generate_line(1))

        # n^{1 / n}
        sequences.append(
            MathTex(r"\lim_{n \rightarrow \infty}", r"\sqrt[n]{n}", r"=", r"1")
        )
        points.append(generate_points(lambda x: x ** (1 / x)))
        lines.append(generate_line(1))

        # a^n n^k, if |a| < 1
        sequences.append(
            MathTex(
                r"\lim_{n \rightarrow \infty}",
                r"a^n \cdot n^k",
                r"=",
                r"1",
                r"\text{, ha } |a| < 1",
            )
        )
        points.append(generate_points(lambda x: 0.6**x * x**2))
        lines.append(generate_line(0))

        # a^n, if a = 1
        sequences.append(
            MathTex(
                r"\lim_{n \rightarrow \infty}",
                r"a^n",
                r"=",
                r"1",
                r"\text{, ha } a = 1",
            )
        )
        points.append(generate_points(lambda _: 1))
        lines.append(generate_line(1))

        # a^n, if |a| < 1
        sequences.append(
            MathTex(
                r"\lim_{n \rightarrow \infty}",
                r"a^n",
                r"=",
                r"0",
                r"\text{, ha } |a| < 1",
            )
        )
        points.append(generate_points(lambda x: (-0.8) ** x))
        lines.append(generate_line(0))

        # a^n, if a > 1
        sequences.append(
            MathTex(
                r"\lim_{n \rightarrow \infty}",
                r"a^n",
                r"=",
                r"\infty",
                r"\text{, ha } a > 1",
            )
        )
        points.append(generate_points(lambda x: 1.075**x))
        lines.append(generate_line(20))

        # a^n, if a <= -1
        sequences.append(
            MathTex(
                r"\lim_{n \rightarrow \infty}",
                r"a^n",
                r"=",
                r"\nexists",
                r"\text{, ha } a \leq - 1",
            )
        )
        points.append(generate_points(lambda x: (-1) ** x))
        lines.append(generate_line(-20))

        # Arrangement for sequences
        for o in sequences:
            o.next_to(title_2, DOWN)

        # Animation begins here
        self.play(ReplacementTransform(title_1, title_2))
        self.pause()

        self.play(FadeIn(g))
        self.pause()

        self.play(Write(sequences[0]))
        self.play(FadeIn(points[0]), FadeIn(lines[0]))
        self.pause()

        m = len(lines) - 1
        for i in range(m):
            self.play(FadeOut(points[i]), FadeOut(lines[i]))
            self.play(ReplacementTransform(sequences[i], sequences[i + 1]))
            self.play(FadeIn(points[i + 1]), FadeIn(lines[i + 1]))
            self.pause()

        # Cleanup
        self.play(FadeOut(Group(g, sequences[m], points[m], lines[m])))
        self.pause()

        # Animation ends here
        self.wait()


class SqueezeTheorem(Slide):
    def construct(self):
        # Mobjects, etc
        text = (
            Tex(
                r"$!(a_n), (b_n), (c_n)$ numerikus sorozatok, ",
                r"melyekre $(a_n) \leq (b_n) \leq (c_n)$ \\",
                r"$\forall n$-re, vagy csak egy bizonyos $n$-től, ",
                # r"továbbá $\displaystyle\lim_{n \rightarrow \infty} a_n \lim{n \rightarrow \infty} c_n = a$. \\",
                r"továbbá $a_n, c_n \rightarrow a$. \\"
                r"Ekkor $\displaystyle\lim_{n \rightarrow \infty} b_n$ = a",
            )
            .next_to(title_3, DOWN)
            .scale(0.8)
        )

        ax = Axes(
            x_range=(0, 20),
            y_range=(0, 0.8),
            x_length=8,
            y_length=4.5,
        ).shift(2 * DOWN)
        x_label = ax.get_x_axis_label(r"n")
        y_label = ax.get_y_axis_label(r"a_n")

        g = VGroup(ax, x_label, y_label)

        min = 1
        max = 20
        points = []

        def generate_points(function, c):
            temp = Group()
            for i in range(min, max):
                temp.add(
                    Dot(ax.coords_to_point(i, function(i)), color=c, fill_opacity=0.8)
                )
            return temp

        points.append(generate_points(lambda x: 1 / 3**x, YELLOW))
        points.append(generate_points(lambda x: (2 / 3) ** x, BLUE))
        points.append(generate_points(lambda x: x / 3**x, RED))

        tex = (
            Group(
                MathTex(r"\frac{1}{3^n}", color=YELLOW),
                MathTex(r"\leq"),
                MathTex(r"\frac{n}{3^n}", color=RED),
                MathTex(r"\leq"),
                MathTex(r"\frac{2^n}{3^n}", color=BLUE),
            )
            .arrange(RIGHT)
            .shift(2 * RIGHT)
        )

        # Animation begins here
        self.play(ReplacementTransform(title_2, title_3))
        self.pause()

        self.play(Write(text))
        self.pause()

        self.play(FadeIn(g))
        self.play(FadeIn(tex))
        self.pause()

        self.play(FadeIn(Group(*points)))
        self.pause()

        # Cleanup
        self.play(FadeOut(Group(*points, g, tex, text)))
        self.pause()

        # Animation ends here
        self.wait()


class Dominance(Slide):
    def construct(self):
        # Mobjects, etc
        min = 1
        max_1 = 40
        max_2 = 15

        ax_1 = Axes(
            x_range=(0, max_1),
            y_range=(0, 10),
            x_length=8,
            y_length=6,
        ).shift(DOWN / 2)
        x_label = ax_1.get_x_axis_label(r"n")
        y_label = ax_1.get_y_axis_label(r"a_n")

        g_1 = VGroup(ax_1, x_label, y_label)

        ax_2 = Axes(
            x_range=(0, max_2),
            y_range=(0, 10),
            x_length=8,
            y_length=6,
        ).shift(DOWN / 2)
        x_label = ax_2.get_x_axis_label(r"n")
        y_label = ax_2.get_y_axis_label(r"a_n")

        g_2 = VGroup(ax_2, x_label, y_label)

        points_1 = []
        points_2 = []

        def generate_points(function, c, max, ax):
            temp = Group()
            for i in range(min, max):
                temp.add(Dot(ax.coords_to_point(i, function(i)), color=c))
            return temp

        points_1.append(
            generate_points(lambda x: math.log(2, x + 1), YELLOW, max_1, ax_1)
        )
        points_1.append(generate_points(lambda x: 2 ** (1 / x), GREEN, max_1, ax_1))
        points_1.append(generate_points(lambda x: math.log(x, 2), RED, max_1, ax_1))
        points_1.append(generate_points(lambda x: x ** (1 / 2), PURPLE, max_1, ax_1))
        points_2.append(generate_points(lambda x: x / 3, YELLOW, max_2, ax_2))
        points_2.append(generate_points(lambda x: x ** (1.5) / 5, GREEN, max_2, ax_2))
        points_2.append(generate_points(lambda x: (1.5) ** x / 9, RED, max_2, ax_2))
        points_2.append(
            generate_points(lambda x: math.factorial(x) / 100, PURPLE, max_2, ax_2)
        )

        t_1 = (
            Group(
                MathTex(r"\log_n a", color=YELLOW),
                MathTex(r"\leq"),
                MathTex(r"\sqrt[n]{a}", color=GREEN),
                MathTex(r"\leq"),
                MathTex(r"\log_a n", color=RED),
                MathTex(r"\leq"),
                MathTex(r"\sqrt[a]{n}", color=PURPLE),
            )
            .arrange(RIGHT)
            .shift(RIGHT + 2 * UP)
        )

        t_2 = (
            Group(
                MathTex(r"n", color=YELLOW),
                MathTex(r"\leq"),
                MathTex(r"n^a", color=GREEN),
                MathTex(r"\leq"),
                MathTex(r"a^n", color=RED),
                MathTex(r"\leq"),
                MathTex(r"n!", color=PURPLE),
            )
            .arrange(RIGHT)
            .shift(LEFT + 2 * UP)
        )

        # Animation begins here
        self.play(ReplacementTransform(title_3, title_4))
        self.pause()

        self.play(FadeIn(g_1))
        self.pause()

        self.play(FadeIn(t_1))
        self.pause()

        for i in range(4):
            self.play(FadeIn(points_1[i]))
            self.pause()

        self.play(FadeOut(Group(*points_1, t_1)))
        self.play(ReplacementTransform(g_1, g_2))
        self.pause()

        self.play(FadeIn(t_2))
        self.pause()

        for i in range(4):
            self.play(FadeIn(points_2[i]))
            self.pause()

        # Cleanup
        self.play(FadeOut(Group(*points_2, t_2, g_2)))
        self.pause()

        # Animation ends here
        self.wait()


class Monotonity(Slide):
    def construct(self):
        # Mobjects, etc
        list = BulletedList(
            r"Felülről korlátos: $\forall n\text{-re } a_n \leq K$",
            r"Alulról korlátos: $\forall n\text{-re } a_n \geq k$",
            r"Monotion nő: $a_n \leq a_{n+1}$",
            r"Monotion csökken: $a_n \geq a_{n+1}$",
        )

        ex_1 = MathTex(r"a_n = ", r"\frac{1}{n}").next_to(title_5, DOWN)
        ex_2 = MathTex(r"a_n = ", r"\cos(n)").next_to(title_5, DOWN)
        ex_3 = MathTex(r"a_n = ", r"\frac{n}{5}").next_to(title_5, DOWN)

        min = 0
        max = 10

        ax = Axes(
            x_range=(0, max),
            y_range=(-1.2, 2.6),
            x_length=8,
            y_length=5.5,
            axis_config={"include_numbers": True},
        ).shift(DOWN * 1.5)
        x_label = ax.get_x_axis_label(r"n")
        y_label = ax.get_y_axis_label(r"a_n")

        g = VGroup(ax, x_label, y_label)

        def generate_points(function):
            temp = Group()
            for i in range(min, max):
                temp.add(Dot(ax.coords_to_point(i, function(i)), color=RED))
            return temp

        def generate_line(x, c):
            return Line(ax.coords_to_point(0, x), ax.coords_to_point(max, x), color=c)

        # Animation begins here
        self.play(ReplacementTransform(title_4, title_5))
        self.pause()

        self.play(FadeIn(list))
        self.pause()

        self.play(FadeOut(list))
        self.play(FadeIn(g))
        self.pause()

        # Ex 1
        self.play(Write(ex_1))
        self.pause()

        points = generate_points(lambda x: x == 0 and 20 or 1 / x)
        self.play(FadeIn(points))
        self.pause()

        upper = generate_line(1, BLUE)
        self.play(FadeIn(upper))
        self.pause()

        lower = generate_line(0, YELLOW)
        self.play(FadeIn(lower))
        self.pause()

        self.play(FadeOut(Group(points, upper, lower)))
        self.pause()

        # Ex 2
        self.play(ReplacementTransform(ex_1, ex_2))
        self.pause()

        points = generate_points(lambda x: np.cos(x))
        self.play(FadeIn(points))
        self.pause()

        upper = generate_line(1, BLUE)
        self.play(FadeIn(upper))
        self.pause()

        lower = generate_line(-1, YELLOW)
        self.play(FadeIn(lower))
        self.pause()

        self.play(FadeOut(Group(points, upper, lower)))
        self.pause()

        # Ex 3
        self.play(ReplacementTransform(ex_2, ex_3))
        self.pause()

        points = generate_points(lambda x: x / 5)
        self.play(FadeIn(points))
        self.pause()

        lower = generate_line(0, YELLOW)
        self.play(FadeIn(lower))
        self.pause()

        # Cleanup
        self.play(FadeOut(Group(points, lower)))
        self.play(FadeOut(Group(g, ex_3)))
        self.pause()

        # Animation ends here
        self.wait()
