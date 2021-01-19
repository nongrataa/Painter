from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.uix.button import Button
from kivy.core.window import Window
from random import random


class PainterWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(random(), random(), random(), 1)
            rad = 5
            Ellipse(pos=(touch.x, touch.y), size=(rad, rad))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=5)

    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x, touch.y)


class PaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = PainterWidget()
        parent.add_widget(self.painter)
        parent.add_widget(Button(text='Clear', on_press=self.clear_canvas))
        parent.add_widget(Button(text='Save', on_press=self.save_canvas, pos=(100, 0)))
        parent.add_widget(Button(text='Screen', on_press=self.screen_canvas, pos=(200, 0)))
        return parent

    def clear_canvas(self, instance):
        self.painter.canvas.clear()

    def save_canvas(self, instance):
        self.painter.size = (Window.size[0], Window.size[1])
        self.painter.export_to_png('image.png')

    def screen_canvas(self, instance):
        Window.screenshot('screen.png')


if __name__ == "__main__":
    PaintApp().run()
