from manim import *

from manim_slides.slide import Slide

from .flow import BasicSlide

class Conclusion (BasicSlide):
    def construct(self):
        self.play(*self.get_basic_slide_anims("Fazit"))
        self.play(
            Write(
                Paragraph(
                    "Inwiefern bieten Zyklotron und Synchroton"
                    "gegenüber den klassischen Linearbeschleunigern",
                    "Vorteile?",
                    "",
                    "Zyklotron und Synchroton erlauben deutlich größere",
                    "Energiemengen und können Teilchen so auf größere",
                    "Gesamtenergien beschleunigen.",
                    "",
                    "",
                    "Quellen:",
                    "Metzler Physik SII",
                    "https://www.leifiphysik.de/elektrizitaetslehre/bewegte-ladungen-feldern/ausblick/zyklotron",
                    "https://www.leifiphysik.de/elektrizitaetslehre/bewegte-ladungen-feldern/ausblick/linearbeschleuniger",
                    font_size=20
                ).next_to(self.title, DOWN).to_edge(LEFT)
            )
        )