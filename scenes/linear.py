from manim import *

from manim_slides.slide import Slide

from .flow import BasicSlide

POSITIVE = RED
NEGATIVE = BLUE

class LinearAccelerator (BasicSlide):
    def construct(self):
        self.play(*self.get_basic_slide_anims("Das Problem"))

        def linear_acc(num=4, init_l=0.5, b=2) -> tuple[VGroup, Mobject, Mobject, ValueTracker]:

            u = ValueTracker(0)

            l_acc_all = [
                x for i in range(num) for x in [
                    VGroup(
                        Line(ORIGIN, RIGHT * init_l * b**i),
                        Rectangle(
                            width=(init_l * b**i),
                            stroke_opacity=0
                        )
                        .add_updater(lambda d, i=i: d.set_fill(
                            interpolate_color(
                                POSITIVE,
                                NEGATIVE,
                                (((u.get_value() + 1) / 2) if i % 2 == 0
                                else (1 - ((u.get_value() + 1) / 2)))
                            ),
                            opacity=0.5
                        )),
                        Line(ORIGIN, RIGHT * init_l * b**i),
                    ).arrange(DOWN, buff=0),
                    Rectangle(
                        stroke_opacity=0,
                        width=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER
                    ).add_updater(lambda d: d.set_fill(ORANGE, opacity=abs(u.get_value())/2))
                ]
            ][:-1]

            l_acc = VGroup(l_acc_all).arrange(RIGHT, buff=0)

            self.play(FadeIn(l_acc))

            self.next_slide()
            self.play(u.animate.set_value(-1))

            self.next_slide(loop=True)

            for i in range(2):
                self.play(
                    u.animate.set_value(1 if u.get_value() == -1 else -1)
                )

            self.next_slide(loop=True)
            
            dot = Dot()
            dot.next_to(l_acc, LEFT)
            self.add(dot)
            
            # Bad Abs
            for i in range(num):
                self.play(
                    u.animate.set_value(1 if u.get_value() == -1 else -1),
                    dot.animate(
                        rate_func=linear
                    ).shift(
                        RIGHT * DEFAULT_MOBJECT_TO_MOBJECT_BUFFER,
                        RIGHT * init_l * b**i
                    )
                )

            self.play(
                u.animate.set_value(1 if u.get_value() == -1 else -1),
                dot.animate.shift(RIGHT * 4),
                rate_func=linear
            )

            self.play(
                u.animate.set_value(1 if u.get_value() == -1 else -1)
            )

            self.next_slide()

            dot.next_to(l_acc, LEFT)

            return VGroup(l_acc, dot), l_acc, dot, u

        acc, part_l_acc, part_dot, u = linear_acc()
        self.play(acc.animate.shift(UP * 1))
        uenergy = MathTex("\\Delta E = qU").next_to(acc, DOWN)
        self.play(FadeIn(uenergy))

        self.next_slide()

        ul = MathTex("U = 1 MV", color=GREY).to_edge(DL)
        ql = MathTex("q = e", color=GREY).next_to(ul, RIGHT)
        uenergyn = MathTex("\\Delta E = 1 MeV").next_to(uenergy, DOWN)

        self.play(FadeIn(ul), FadeIn(ql), Write(uenergyn))

        self.next_slide()

        probl = Text("Spannung über einigen Millionen Volt aufgrund selbständiger Entladungen nicht möglich", font_size=20).next_to(uenergyn, DOWN)
        probl_follow = Text("→ Teilchen nur schwer auf Gesamtenergien größer MeV beschleunigbar", font_size=20).next_to(probl, DOWN)
        self.play(Write(probl), Write(probl_follow))

        self.next_slide()