from manim import *

from manim_slides.slide import Slide

class BasicSlide(Slide):
    def get_basic_title(self, text):
        return Text(text).to_edge(UL)

    def get_basic_title_anim(self, text):
        self.title = self.get_basic_title(text)
        return FadeIn(self.title)
    
    def get_basic_slide_anims(self, title):
        return [
            self.get_basic_title_anim(title)
        ]