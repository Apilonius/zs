from manim import *

from manim_slides.slide import Slide

from .flow import BasicSlide

class Intro(BasicSlide):
    def construct(self):
        # Date?
        title = VGroup(
            Text("Kräfte im Magnetfeld", color=GREY),
            Text(
            "Inwiefern bieten Zyklotron und Synchroton\ngegenüber den klassischen Linearbeschleunigern\nVorteile?"
            ),
            Text("apilonius", color=GREY)
        ).arrange(DOWN)

        self.play(FadeIn(title))

        self.next_slide()

        # Bad Abs
        agenda = VGroup(
            Text("1. Das Problem").to_edge(LEFT),
            Text("2. Das Zyklotron").to_edge(LEFT),
            Text("3. Weiterentwicklung zum Synchrozyklotron").to_edge(LEFT),
            Text("4. Beispiele").to_edge(LEFT),
            Text("5. Zusammenfassung").to_edge(LEFT)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT)

        self.play(Transform(title, self.get_basic_title("Agenda")), FadeIn(agenda))

        self.next_slide()