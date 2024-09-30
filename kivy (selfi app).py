from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import BooleanProperty

class HoverButton(Button, ButtonBehavior):  # Switched the order here!
    hover = BooleanProperty(False)

    def on_hover(self, instance, value):
        if value:
            self.background_color = (0.5, 0.5, 0.5, 1)  # Change background color on hover
        else:
            self.background_color = (1, 1, 1, 1) 
class SelfieApp(App):
    def build(self):
        try:
            self.camera_obj = Camera(resolution=(1000, 1000), index=0)
            self.camera_obj.play = True
        except Exception as e:  # Handle potential errors
            print("Error creating camera:", e)
            return None  # Exit if camera creation fails

        # Button and layout creation
        button_obj = Button(text="Click!", on_press=self.capture_selfie)
        button_obj.size_hint = (0.6, 0.3)
        button_obj.pos_hint = {"center_x": 0.5, "center_y": 0.35}

        layout_obj = BoxLayout(orientation='vertical')
        layout_obj.add_widget(self.camera_obj)
        layout_obj.add_widget(button_obj)

        return layout_obj

    def capture_selfie(self, instance):
        print("Selfie taken successfully!")
        self.camera_obj.export_to_png("My_first_selfie_with_my_code.png")

if __name__ == "__main__":
    SelfieApp().run()
