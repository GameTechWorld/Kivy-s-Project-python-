from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class lib_grid(GridLayout):
    def __init__(self,**kwargs):
        super(lib_grid,self).__init__()
        self.cols=2
        self.add_widget(Label(text="Student's Name"))
        self.name_one=TextInput()
        self.add_widget(self.name_one)
        self.add_widget(Label(text="Name of the Book: "))
        self.book_one=TextInput()
        self.add_widget(self.book_one)
        self.add_widget(Label(text="Issue Date: "))
        self.issue_one=TextInput()
        self.add_widget(self.issue_one)
        self.add_widget(Label(text="return Book"))
        self.return_one=TextInput()
        self.add_widget(self.return_one)
        self.add_widget(Label(text="Fine(if any): "))
        self.fine_one=TextInput()
        self.add_widget(self.fine_one)
        self.print_info=Button(text="Get Info")
        self.print_info.bind(on_press=self.click_button)
        self.add_widget(self.print_info)

    def click_button(self,instance):
        print(f"Name of Student: {self.name_one.text}")
        print(f"Name of Book: {self.book_one.text}")
        print(f"Issue Date of book: {self.issue_one.text}")
        print(f"Return Date of Book: {self.return_one.text}")
        print(f"Any Fine: {self.fine_one.text}")

class AppLibrary(App):
    def build(self):
        return lib_grid()
if (__name__ == "__main__"):
    AppLibrary().run()
