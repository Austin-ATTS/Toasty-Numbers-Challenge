from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from screens.home import Home
from screens.rounds_mode import RoundsMode
from screens.endless_mode import EndlessMode
from screens.settings import Settings
from screens.accounts import Account
from screens.leaderboard import Leaderboard

class ToastyNumbersApp(App):
    def build(self):
        return

if __name__ == '__main__':
    ToastyNumbersApp().run()
