from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import BooleanProperty

class HoverButton(Button, ButtonBehavior):  # Switched the order here!
    hover = BooleanProperty(False)

    def on_hover(self, instance, value):
        if value:
            self.background_color = (0.5, 0.5, 0.5, 1)  # Change background color on hover
        else:
            self.background_color = (1, 1, 1, 1) # Reset background color on exit

class Calculator(App):
    def build(self):
        widget_root = BoxLayout(orientation="vertical")
        self.label_output = Label(size_hint_y=1, font_size=51)
        symbol_button = ("1", "2", "3", "+", "4", "5", "6", "*", "7", "8", "9", ".", "0", "/", "-", "=")
        grid_button = GridLayout(cols=4, size_hint_y=3)
        for symbol in symbol_button:
            btn = HoverButton(text=symbol)
            if (symbol == "="):
                btn.bind(on_press=self.result)
            else:
                btn.bind(on_press=self.text_print_button)
            grid_button.add_widget(btn)
        button_clear = HoverButton(text="X", size_hint_y=None, height=100)
        button_clear.bind(on_press=self.label_clear)
        widget_root.add_widget(self.label_output)
        widget_root.add_widget(grid_button)
        widget_root.add_widget(button_clear)
        return widget_root

    def text_print_button(self, instance):
        self.label_output.text += instance.text

    def result(self, instance):
        try:
            self.label_output.text = str(eval(self.label_output.text))
        except Exception as e:
            print(e)

    def label_clear(self, instance):
        self.label_output.text = ''

if (__name__ == "__main__"):
    Calculator().run()
