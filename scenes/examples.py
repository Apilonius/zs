from manim import *

from manim_slides.slide import Slide

from .flow import BasicSlide

# very Bad abstr!!

class Example (BasicSlide):
    pass

class Examples (Example):
    def construct(self):
        self.play(*self.get_basic_slide_anims("Beispielaufgabe 1"))

        self.next_slide()

        task = Paragraph(
        "Emitteln Sie die Spannung, die Protonen",
        "in einem elektrischem Feld auf dieselbe",
        "Endgeschwindigkeit wie in  einem  Zyklotron mit",
        "r = 0,8m und B = 1,5T beschleunigen würde.",
        font_size=20
        ).next_to(self.title, DOWN).to_edge(LEFT)

        self.play(FadeIn(task))

        self.next_slide()

        taskinfo = VGroup(
            Text("Berechnen Sie  die Spannung, die  für Protonen in einem einzelnen vergleichbaren E-Feld erforderlich wäre.", font_size=20).to_edge(LEFT),
            VGroup(MathTex("r = ", "0,8m"), MathTex("B = ", "1,5 T"), MathTex("q=+e\\thickapprox", "1,6*10^-19"), MathTex("m \\thickapprox ", "1,6*10^-27g")).scale(0.7).arrange().to_edge(LEFT),
            MathTex("U_{Feld} = ?").scale(0.7).to_edge(LEFT)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(self.title, DOWN).to_edge(LEFT)

        values = taskinfo[1]

        self.play(ReplacementTransform(task, taskinfo))

        self.next_slide()
        crad = MathTex("r = \\frac{v}{B(q/m)}", color=GREY).arrange().next_to(taskinfo, DOWN).to_edge(LEFT)
        crad2 = MathTex("\\rightarrow v = rB(\\frac{q}{m})").arrange().next_to(crad)
        self.play(Write(crad))
        self.next_slide()
        self.play(Write(crad2))
        self.next_slide()

        fs = VGroup([SurroundingRectangle(item[1]) for item in values])
        self.play(Create(fs))

        self.next_slide()
        crad3 = MathTex("\\rightarrow v = 0.8 * 1,5(\\frac{1,6 * 10^{-19}}{1,6 * 10^{-27}})").arrange().next_to(crad2, DOWN).to_edge(LEFT)
        crad4 = MathTex("v = ", "120 000 000").arrange().next_to(crad3, DOWN).to_edge(LEFT)
        self.play(Write(crad3))
        self.next_slide()
        self.play(Write(crad4), FadeOut(fs))
        self.next_slide()
        self.play(crad4.animate.next_to(self.title, DOWN).to_edge(LEFT), FadeOut(taskinfo, crad, crad2, crad3))

        self.next_slide()
        ek = MathTex("E_{kin} = \\frac{1}{2}mv^2").next_to(crad4, DOWN).to_edge(LEFT)
        self.play(Write(ek))
        self.next_slide()
        f0 = SurroundingRectangle(crad4[1])
        ek2 = MathTex("= 1,6 * 10^{-27} * (120 000 000)^2").next_to(ek)
        self.play(Write(ek2), Create(f0))
        self.next_slide()
        ek3 = MathTex("E_{kin} = ", "1,152 * 10^{-11}").next_to(ek2, DOWN).to_edge(LEFT)
        self.play(Write(ek3), FadeOut(f0))
        self.next_slide()

        ek4 = MathTex("E = eU", color=GREY).next_to(ek3).next_to(ek3, DOWN, 1).to_edge(LEFT)
        self.play(Write(ek4))
        self.next_slide()
        ek5 = MathTex("\\rightarrow U = \\frac{E}{e}").next_to(ek4)
        self.play(Write(ek5))
        self.next_slide()
        f1 = SurroundingRectangle(ek3[1])
        ek6 = MathTex("U = \\frac{1,52*10^{-11}}{1,6*10^{-19}}").next_to(ek5, DOWN).to_edge(LEFT)
        self.play(Write(ek6), Create(f1))
        self.next_slide()
        ek7 = MathTex("= 72 MV").next_to(ek6)
        self.play(Write(ek7), FadeOut(f1))

        self.next_slide()

class Examples2 (Example):
    def construct(self):
        self.play(*self.get_basic_slide_anims("Beispielaufgabe 2"))

        self.next_slide()

        task = Paragraph(
        "Ein Zyklotron mit B = 2T gibt \\alpha Teilchen mit E = 2,5 J ab.",
        "Berechnen Sie den größten Krümmungsradius der Bahnkurven.",
        font_size=20
        ).next_to(self.title, DOWN).to_edge(LEFT)

        self.play(FadeIn(task))

        self.next_slide()

        taskinfo = VGroup(
            Text("Berechnen Sie den größten Krümmungsradius der Bahnkurven.", font_size=20).to_edge(LEFT),
            VGroup(MathTex("B = ", "2 T"), MathTex("E = ", "2,5 J"), MathTex("q=", "+2e"), MathTex("m=", "6,64 * 10^{-27}")).scale(0.7).arrange().to_edge(LEFT),
            MathTex("r = ?").scale(0.7).to_edge(LEFT)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(self.title, DOWN).to_edge(LEFT)

        values = taskinfo[1]

        fs = VGroup(SurroundingRectangle(values[1][1]), SurroundingRectangle(values[3][1]))

        self.play(ReplacementTransform(task, taskinfo))

        crad = MathTex("E = \\frac{1}{2}mv^2", color=GREY).arrange().next_to(taskinfo, DOWN).to_edge(LEFT)
        crad2 = MathTex("\\rightarrow v = \\sqrt{2 \\frac{E}{m}}").arrange().next_to(crad)
        self.play(Write(crad))
        self.next_slide()
        self.play(Write(crad2))
        self.next_slide()
        crad3 = MathTex("v \\thickapprox \\sqrt{2 \\frac{2,5J}{6,64 * 10^{-27}}}").next_to(crad2, DOWN).to_edge(LEFT)
        self.play(Write(crad3), FadeIn(fs))
        self.next_slide()
        crad4 = MathTex("v \\thickapprox ", "2,76 * 10^{13} \\frac{m}{s}").next_to(crad3, DOWN).to_edge(LEFT)
        self.play(Write(crad4), FadeOut(fs))
        self.next_slide()

        self.play(FadeOut(crad, crad2, crad3), crad4.animate.next_to(taskinfo, DOWN).to_edge(LEFT))
        self.next_slide()
        ru = MathTex("r = \\frac{U}{B q/m}").next_to(crad4, DOWN).to_edge(LEFT)
        self.play(Write(ru))
        self.next_slide()
        fs2 = VGroup(SurroundingRectangle(values[0][1]), SurroundingRectangle(values[2][1]), SurroundingRectangle(values[3][1]), SurroundingRectangle(crad4[1]))
        ru1 = MathTex("r \\thickapprox \\frac{2,76 * 10^{13} \\frac{m}{s}}{2T \\frac{1,6*10^{-19}}{6,64*10^{-27}}}").next_to(ru, DOWN).to_edge(LEFT)
        self.play(Write(ru1), FadeIn(fs2))
        self.next_slide()
        ru2 = MathTex("r \\thickapprox 286350m").next_to(ru1, DOWN).to_edge(LEFT)
        self.play(Write(ru2), FadeOut(fs2))
        self.next_slide()

        self.next_slide()

class Examples3 (Example):
    def construct(self):
        self.play(*self.get_basic_slide_anims("Beispielaufgabe 3"))
        task = Paragraph(
        "Berechnen Sie die Feldstärke des koventionell",
        "erzeugten Magnetfeldes in einem SPS mit",
        "einer Tunnellänge von 7km und E = 450 GeV",
        font_size=20
        ).next_to(self.title, DOWN).to_edge(LEFT)
        self.play(FadeIn(task))
        self.next_slide()

        taskinfo = VGroup(
            Text("Berechnen Sie die magnetische Feldstärke.", font_size=20).to_edge(LEFT),
            VGroup(MathTex("q = ", "+e"), MathTex("m_0 = ", "1,67 * 10^{-27}"), MathTex("E_{kin} = ", "450 GeV"), MathTex("Umf = 7km = ", "7 * 10^3m")).scale(0.7).arrange().to_edge(LEFT),
            MathTex("B = ?").scale(0.7).to_edge(LEFT)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(self.title, DOWN).to_edge(LEFT)
        values = taskinfo[1]

        self.play(ReplacementTransform(task, taskinfo))
        self.next_slide()

        crad = MathTex("Umf = 2 \\pi r", color=GREY).arrange().next_to(taskinfo, DOWN).to_edge(LEFT)
        crad2 = MathTex("\\rightarrow r = \\frac{Umf}{2\\pi}").arrange().next_to(crad)
        self.play(Write(crad))
        self.next_slide()
        self.play(Write(crad2))
        self.next_slide()

        fs = SurroundingRectangle(values[3][1])
        crad3 = MathTex("r \\thickapprox \\frac{7 * 10^3}{2\\pi}").next_to(crad2, DOWN).to_edge(LEFT)
        self.play(Write(crad3), FadeIn(fs))
        self.next_slide()
        crad4 = MathTex("r \\thickapprox ", "1114m").next_to(crad3, DOWN).to_edge(LEFT)
        self.play(Write(crad4), FadeOut(fs))
        self.next_slide()
        self.play(FadeOut(crad, crad2, crad3), crad4.animate.next_to(taskinfo, DOWN).to_edge(LEFT))
        self.next_slide()

        crad = MathTex("E = mc^2", color=GREY).arrange().next_to(crad4, DOWN).to_edge(LEFT)
        crad2 = MathTex("\\rightarrow \\Delta m = \\frac{E_{kin}}{c^2}").arrange().next_to(crad)
        self.play(Write(crad))
        self.next_slide()
        self.play(Write(crad2))
        self.next_slide()
        fs = VGroup(SurroundingRectangle(values[1][1]), SurroundingRectangle(values[2][1]))
        crad3 = MathTex("\\Delta m \\thickapprox \\frac{450 * 10^9 * 1,6 * 10^{-19}}{(3*10^8 \\frac{m}{s})^2}").next_to(crad2, DOWN).to_edge(LEFT)
        crad4_2 = MathTex("\\Delta m \\thickapprox ", "8 * 10^{-25}kg").next_to(crad3, DOWN).to_edge(LEFT)
        self.play(Write(crad3), FadeIn(fs))
        self.next_slide()
        self.play(Write(crad4_2), FadeOut(fs))
        self.next_slide()
        self.play(crad4_2.animate.next_to(crad4), FadeOut(crad, crad2, crad3))
        
        self.next_slide()
        crad = MathTex("r = \\frac{v}{B(q/m)}", color=GREY).arrange().next_to(crad4, DOWN).to_edge(LEFT)
        crad2 = MathTex("\\rightarrow B = \\frac{(m + \\Delta m)c}{qr}").arrange().next_to(crad)
        self.play(Write(crad))
        self.next_slide()
        self.play(Write(crad2))
        self.next_slide()
        fs = VGroup(SurroundingRectangle(values[0][1]), SurroundingRectangle(values[1][1]), SurroundingRectangle(crad4[1]), SurroundingRectangle(crad4_2[1]))
        crad3 = MathTex("B = \\frac{8 * 10^{-25}kg * 3 * 10^8 \\frac{m}{s}}{1,6 * 10^{-19}As * 1114}").next_to(crad2, DOWN).to_edge(LEFT)
        crad4_3 = MathTex("B = 1,35T").next_to(crad3, DOWN).to_edge(LEFT)
        self.play(Write(crad3), FadeIn(fs), Write(MathTex("v \\thickapprox c", color=GREY).next_to(crad4_2)))
        self.next_slide()
        self.play(Write(crad4_3), FadeOut(fs))
        self.next_slide()