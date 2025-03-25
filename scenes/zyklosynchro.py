from textwrap import fill
from turtle import left
from manim import *

from manim_slides.slide import Slide
from networkx import radius

from scenes.flow import BasicSlide
from scenes.linear import NEGATIVE, POSITIVE

# Bad abs

class ZykloAndSync (BasicSlide):
    def construct(self):
        self.play(*self.get_basic_slide_anims("Das Zyklotron"))

        def zyklo():
            RAD = 2
            EXTRA_RAD = 0.1
            EL_L = 0.4
            MAG_EXTRA_RAD = 4 * EXTRA_RAD
            MAX_ROUNDS = 6.5

            u = ValueTracker(0)

            def e_arrow_updater(d: Mobject):
                d = d.set_opacity(abs(u.get_value())/2)

                if u.get_value() > 0 and d.get_start()[0] <= d.get_end()[0]:  # If pointing right
                    return d.flip()
                
                if u.get_value() < 0 and d.get_start()[0] >= d.get_end()[0]:  # If pointing right
                    return d.flip()
                
                # if u.get_value() == 0:
                #    return d.set_fill(color=d.fill_color, opacity=0)
                
                return d

            zyklo = VGroup(
                Arc(radius=RAD, angle=PI, start_angle=PI/2).add_updater(lambda d: d.set_fill(
                    interpolate_color(
                        POSITIVE,
                        NEGATIVE,
                        (u.get_value() + 1) / 2
                    ),
                    opacity=0.5
                )),
                VGroup(
                    Rectangle(
                            stroke_opacity=0,
                            width=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER,
                            height=RAD*2
                        ).add_updater(lambda d: d.set_fill(ORANGE, opacity=abs(u.get_value())/2)
                    ),
                    Arrow(
                        LEFT * DEFAULT_MOBJECT_TO_MOBJECT_BUFFER/2, RIGHT * DEFAULT_MOBJECT_TO_MOBJECT_BUFFER/2
                    ).add_updater(e_arrow_updater).shift(UP * RAD/2),
                    Arrow(
                        LEFT * DEFAULT_MOBJECT_TO_MOBJECT_BUFFER/2, RIGHT * DEFAULT_MOBJECT_TO_MOBJECT_BUFFER/2
                    ).add_updater(e_arrow_updater).shift(DOWN * RAD/2)
                ),
                VGroup(
                    Arc(radius=RAD+EXTRA_RAD, angle=PI, start_angle=3/2 * PI).add_updater(lambda d: d.set_fill(
                        interpolate_color(
                            POSITIVE,
                            NEGATIVE,
                            1 - ((u.get_value() + 1) / 2)
                        ),
                        opacity=0.5
                    )),
                    Line(DOWN * (RAD+EXTRA_RAD), DOWN * (RAD+EXTRA_RAD) + LEFT * EL_L, color=BLUE)
                )
            ).arrange(RIGHT, buff=0).move_to(RIGHT * 4)
            
            # Bad abs, TODO: Auslenk
            zyklo[2].shift(DOWN * EXTRA_RAD + LEFT * EL_L)


            mag = Circle(radius=RAD + MAG_EXTRA_RAD, fill_color=ORANGE, fill_opacity=0.4, stroke_opacity=0).move_to(LEFT * 4)
            mtex = Text("starker Magnet (B > 1T)", font_size=20).next_to(mag, DOWN)
            self.play(FadeIn(mag), Write(mtex))
            self.next_slide()

            ztex = Text("Zwei \"Ds\"", font_size=20).next_to(zyklo, DOWN)
            self.play(FadeIn(zyklo), Write(ztex))
            self.next_slide()

            self.play(FadeOut(mtex), FadeOut(ztex), mag.animate.move_to(ORIGIN), zyklo.animate.move_to(ORIGIN))
            self.play(u.animate.set_value(0))
            # self.next_slide()

            # self.play(u.animate.set_value(-1))
            self.next_slide(loop=True)
            halfCircles = ValueTracker(0)

            u.add_updater(lambda d: d.set_value(np.sin((halfCircles.get_value()) * PI)))
            self.play(halfCircles.animate.set_value(2), rate_func=linear, run_time=2)

            self.next_slide()

            dot = Dot()

            def s(t):
                return np.array([
                    (t * 0.1 * PI) * np.cos(-t * PI),
                    (t * 0.1 * PI) * np.sin(-t * PI),
                    0
                ])
            
            dot_updatr = lambda d: d.move_to(
                np.array([
                    s(halfCircles.get_value())
                ])
            ) if halfCircles.get_value() <= MAX_ROUNDS else d.move_to(s(MAX_ROUNDS) + LEFT * (halfCircles.get_value() - MAX_ROUNDS) * MAX_ROUNDS)

            dot.add_updater(dot_updatr)
            
            self.add(dot)
            halfCircles.set_value(4.2)
            dot.update()
            lorenz = VGroup(
                Arrow(dot, ORIGIN, color=GREEN),
                Label("F_L").shift(RIGHT * 1 + DOWN * 0.2)
            )

            self.play(FadeIn(lorenz))

            self.next_slide()
            halfCircles.set_value(0)
            self.remove(lorenz)
            self.next_slide(loop=True)

            self.play(halfCircles.animate.set_value(8), run_time=8, rate_func=linear)
            self.next_slide()
            halfCircles.set_value(4.2)
            dot.update()

            dot.remove_updater(dot_updatr)

            zyk_all = VGroup(zyklo, dot, mag)
            return zyk_all



        z = zyklo()

        self.play(z.animate.to_edge(LEFT))
        self.next_slide()
        crad = MathTex("r = \\frac{v}{B(q/m)}").arrange().next_to(z, RIGHT).shift(UP * 2)
        crad2 = MathTex("v = ", "rB(q/m)").next_to(crad)
        self.play(Write(crad))
        self.next_slide()
        self.play(Write(crad2))
        self.next_slide()
        umld = MathTex("T = \\frac{2 \\pi r}{v}").next_to(crad, DOWN)
        self.play(Write(umld))
        self.next_slide()
        umld2 = MathTex("= ", "\\frac{2 \\pi}{B(q/m)}").next_to(umld)
        f1 = SurroundingRectangle(crad2[1])
        self.play(Write(umld2), Create(f1))
        self.next_slide()
        f2 = SurroundingRectangle(umld2[1])
        ufollow = Text("→ Umlaufzeit(T) und Frequenz(f) von Radius(r)\nund Geschwindigkeit(v) unabhängig", font_size=20).next_to(z, RIGHT).shift(DOWN)
        self.play(ReplacementTransform(f1, f2), Write(ufollow))

        self.next_slide()


class Syn (BasicSlide):
    def construct(self):
        self.play(*self.get_basic_slide_anims("Das Synchroton"))
        self.next_slide()

        em = VGroup(
            Text("(Für Protonen im  Zyklotron)", font_size=20),
            MathTex("E_{max} = 20 MeV \\thickapprox 20\\% c "),
            Text("relativistische  Effekte  lassen  Teilchen außer Takt der Wechselspannung geraten", font_size=20),
        ).arrange(DOWN)
        ul = MathTex("c = Lichtgeschwindigkeit", color=GREY).to_edge(DL)
        
        self.play(Write(em), FadeIn(ul))
        self.next_slide()

        emc = MathTex("E = mc^2").next_to(self.title, DOWN).to_edge(LEFT)
        self.play(Transform(em, emc))

        self.next_slide()
        mec = MathTex("\\Delta m = \\frac{E_{kin}}{c^2}").next_to(emc, DOWN).to_edge(LEFT)
        self.play(Write(mec))

        self.next_slide()
        ufollow = Text("→ Takt der Wechselspannung wird synchron mit der Geschwindigkeit erhöht", font_size=20).next_to(mec, DOWN).to_edge(LEFT)
        ufollow2 = Text("→ Statt Magnet hintereinander aufgestellte Magnetspulen", font_size=20).next_to(ufollow, DOWN).to_edge(LEFT)
        self.play(FadeIn(ufollow))
        self.next_slide()
        self.play(FadeIn(ufollow2))

        self.next_slide()
        crad = MathTex("r = \\frac{v}{B(q/m)}", color=GREY).arrange().next_to(ufollow2, DOWN).to_edge(LEFT)
        crad2 = MathTex("\\rightarrow B = \\frac{(\\Delta m + m)c}{qr}").arrange().next_to(crad)
        self.play(Write(crad))
        self.next_slide()
        self.play(Write(crad2))

        self.next_slide()