from manim import *
from manim_slides import Slide

title_1 = Title("Halmazelmélet – ", "Alapfogalmak")
title_2 = Title("Halmazelmélet – ", "Műveletek")


class Sets(Slide):
    def construct(self):
        General.construct(self)
        Operations.construct(self)
        DeMorgan.construct(self)

        self.play(Unwrite(title_2))


class General(Slide):
    def construct(self):
        # Mobjects, etc
        list = BulletedList(
            "A halmaz egy nem definiált alapfogalom.",
            "Jelölés: $A ,B, C$",
            "Elemek: $a, b, c$",
            "Ha $x$ eleme $A$ halmaznak, akkor $x \\in A$",
            "Ha $x$ nem eleme $A$ halmaznak, akkor $x \\notin A$",
        )

        # Animation starts here
        self.play(Write(title_1))
        self.pause()

        self.play(FadeIn(list))
        self.pause()

        self.play(FadeOut(list))
        self.play(ReplacementTransform(title_1, title_2))

        # Animation ends here
        self.wait()


class Operations(Slide):
    def construct(self):
        # Mobjects, etc
        A = Circle(radius=1.5, fill_opacity=0.5, color=BLUE, stroke_width=6).shift(
            LEFT * 0.75
        )
        B = Circle(radius=1.5, fill_opacity=0.5, color=RED, stroke_width=6).shift(
            RIGHT * 0.75
        )
        A_text = MathTex("A").next_to(A, 2 * UP)
        B_text = MathTex("B").next_to(B, 2 * UP)

        sets = Group(A, B, A_text, B_text).shift(UP * 0.75)

        union = Union(A, B, color=GREEN, fill_opacity=0.5)
        union_text = MathTex(r"A \cup B")

        intersection = Intersection(A, B, color=ORANGE, fill_opacity=0.5)
        intersection_text = MathTex(r"A \cap B")

        difference = Difference(A, B, color=GOLD, fill_opacity=0.5)
        difference_text = MathTex(r"A \setminus B")

        group_1 = Group(
            sets,
            union,
            union_text,
            intersection,
            intersection_text,
            difference,
            difference_text,
        )

        # Operation props
        subtitle_1 = Tex(r"Metszet és unió tulajdonságai ($A, B, C \in X$)").next_to(
            title_2, DOWN, buff=0.5
        )

        t = (
            Group(
                Tex("Kommutatív"),
                Tex("Asszociatív"),
                Tex("Idempotens"),
                Tex("Disztributív"),
            )
            .arrange(direction=DOWN, buff=0.525, aligned_edge=LEFT)
            .to_edge(LEFT)
        )

        u = (
            Group(
                MathTex("A", r"\cup", "B = B", r"\cup", "A"),
                MathTex(
                    "(A", r"\cup", "B)", r"\cup", "C = A", r"\cup", "(B", r"\cup", "C)"
                ),
                MathTex("A", r"\cup", "A = A"),
                MathTex(
                    "(A",
                    r"\cup",
                    "B)",
                    r"\cap",
                    "C = (A",
                    r"\cap",
                    "C)",
                    r"\cup",
                    "(B",
                    r"\cap",
                    "C)",
                ),
                MathTex("A", r"\cup", r"\emptyset =", "A"),
                MathTex("A", r"\cup", r"\overline A = ", "X"),
            )
            .arrange(direction=DOWN, buff=0.5, aligned_edge=RIGHT)
            .align_to(t, UP)
            .to_edge(RIGHT)
        )

        i = (
            Group(
                MathTex("A", r"\cap", "B = B", r"\cap", "A"),
                MathTex(
                    "(A", r"\cap", "B)", r"\cap", "C = A", r"\cap", "(B", r"\cap", "C)"
                ),
                MathTex("A", r"\cap", "A = A"),
                MathTex(
                    "(A",
                    r"\cap",
                    "B)",
                    r"\cup",
                    "C = (A",
                    r"\cup",
                    "C)",
                    r"\cap",
                    "(B",
                    r"\cup",
                    "C)",
                ),
                MathTex("A", r"\cap", r"\emptyset = ", r"\emptyset"),
                MathTex("A", r"\cap", r"\overline A = ", r"\emptyset"),
            )
            .arrange(direction=DOWN, buff=0.5, aligned_edge=RIGHT)
            .align_to(t, UP)
            .to_edge(RIGHT)
        )

        # Animation starts here
        self.add(title_2)

        self.play(FadeIn(sets))
        self.pause()

        self.play(union.animate.scale(0.5).move_to(DOWN * 3 + LEFT * 3))
        union_text.next_to(union, UP)
        self.play(FadeIn(union_text))
        self.pause()

        self.play(intersection.animate.scale(0.5).move_to(DOWN * 3))
        intersection_text.next_to(intersection, UP)
        self.play(FadeIn(intersection_text))
        self.pause()

        self.play(difference.animate.scale(0.5).move_to(DOWN * 3 + RIGHT * 3))
        difference_text.next_to(difference, UP)
        self.play(FadeIn(difference_text))
        self.pause()

        self.play(FadeOut(group_1))
        self.play(Write(subtitle_1))
        self.play(FadeIn(t))
        self.play(FadeIn(u))
        self.pause()

        b = u.copy()
        self.play(ReplacementTransform(u, i))
        self.pause()

        self.play(ReplacementTransform(i, b))
        self.pause()

        self.play(FadeOut(Group(t, b, subtitle_1)))

        # Animation ends here
        self.wait()


subtitle_d1 = Tex(
    r"De Morgan azonosságok – ", r"$\overline{A \cup B} = \overline A \cap \overline B$"
).next_to(title_2, DOWN, buff=0.5)
subtitle_d2 = Tex(
    r"De Morgan azonosságok – ", r"$\overline{A \cap B} = \overline A \cup \overline B$"
).next_to(title_2, DOWN, buff=0.5)


class DeMorgan(Slide):
    def construct(self):
        # Mobjects, etc
        X = RoundedRectangle(
            0.5, height=4.5, width=6, fill_opacity=0.1, stroke_width=6, color=RED
        ).shift(UP / 3)
        A = Circle(radius=1.5, fill_opacity=0.1, color=BLUE, stroke_width=6).shift(
            LEFT * 0.75
        )
        B = Circle(radius=1.5, fill_opacity=0.1, color=GREEN, stroke_width=6).shift(
            RIGHT * 0.75
        )
        X_text = MathTex("X").align_to(X, UL).shift(DR / 4)
        A_text = MathTex("A").next_to(A, 1 * UP)
        B_text = MathTex("B").next_to(B, 1 * UP)

        sets = Group(X, A, B, X_text, A_text, B_text).shift(DOWN).to_edge(LEFT)

        updater = lambda x, y: x.move_to(y.get_top() + UP / 2)

        s1 = Union(A, B, color=YELLOW, fill_opacity=0.5)
        s1_text = MathTex(r"A \cup B").move_to(s1)

        s2 = Difference(X, s1, color=PURPLE, fill_opacity=0.5)
        s2_text = MathTex(r"\overline{A \cup B}")
        s2_text.add_updater(lambda x: updater(x, s2))

        s3 = Difference(X, A, color=YELLOW, fill_opacity=0.5)
        s3_text = MathTex(r"\overline{A}").move_to(s1).shift(RIGHT * 1.5)

        s4 = Difference(X, B, color=TEAL, fill_opacity=0.5)
        s4_text = MathTex(r"\overline{B}").move_to(s1).shift(LEFT * 1.5)

        s5 = Intersection(s3, s4, color=PURPLE, fill_opacity=0.5)
        s5_text = MathTex(r"\overline{A} \cap \overline{B}")
        s5_text.add_updater(lambda x: updater(x, s5))

        # Animation begins here
        self.add(title_2)
        self.play(Write(subtitle_d1), FadeIn(sets))
        self.pause()

        self.play(FadeIn(s1), FadeIn(s1_text))
        self.pause()

        self.play(FadeOut(s1_text))
        self.play(ReplacementTransform(s1, s2), FadeIn(s2_text))
        self.pause()

        self.play(s2.animate.scale(0.33).move_to(3 * RIGHT))
        self.pause()

        self.play(FadeIn(s3), FadeIn(s3_text))
        self.pause()

        self.play(FadeIn(s4), FadeIn(s4_text), FadeOut(s3), FadeOut(s3_text))
        self.pause()

        self.play(FadeOut(s4_text), FadeIn(s3))
        self.pause()

        self.play(ReplacementTransform(Group(s3, s4), s5), FadeIn(s5_text))
        self.pause()

        self.play(s5.animate.scale(0.33).move_to(3 * RIGHT + 3 * DOWN))
        self.pause()

        # First part ends here
        self.play(FadeOut(Group(s2, s5, s2_text, s5_text)))

        # Mobjects, etc
        s1 = Intersection(A, B, color=YELLOW, fill_opacity=0.5)
        s1_text = MathTex(r"A \cap B").move_to(s1)

        s2 = Difference(X, s1, color=PURPLE, fill_opacity=0.5)
        s2_text = MathTex(r"\overline{A \cap B}")
        s2_text.add_updater(lambda x: updater(x, s2))

        s3 = Difference(X, A, color=YELLOW, fill_opacity=0.5)
        s3_text = MathTex(r"\overline{A}").move_to(s1).shift(RIGHT * 1.5)

        s4 = Difference(X, B, color=TEAL, fill_opacity=0.5)
        s4_text = MathTex(r"\overline{B}").move_to(s1).shift(LEFT * 1.5)

        s5 = Union(s3, s4, color=PURPLE, fill_opacity=0.5)
        s5_text = MathTex(r"\overline{A} \cup \overline{B}")
        s5_text.add_updater(lambda x: updater(x, s5))

        # Animation begins here
        self.play(ReplacementTransform(subtitle_d1, subtitle_d2))
        self.pause()

        self.play(FadeIn(s1), FadeIn(s1_text))
        self.pause()

        self.play(FadeOut(s1_text))
        self.play(ReplacementTransform(s1, s2), FadeIn(s2_text))
        self.pause()

        self.play(s2.animate.scale(0.33).move_to(3 * RIGHT))
        self.pause()

        self.play(FadeIn(s3), FadeIn(s3_text))
        self.pause()

        self.play(FadeIn(s4), FadeIn(s4_text), FadeOut(s3), FadeOut(s3_text))
        self.pause()

        self.play(FadeOut(s4_text), FadeIn(s3))
        self.pause()

        self.play(ReplacementTransform(Group(s3, s4), s5), FadeIn(s5_text))
        self.pause()

        self.play(s5.animate.scale(0.33).move_to(3 * RIGHT + 3 * DOWN))
        self.pause()

        # Animation ends here
        self.play(FadeOut(Group(s2, s5, s2_text, s5_text, sets, subtitle_d2)))
        self.wait()
