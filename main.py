from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from screens.home import Home
from screens.rounds_mode import RoundsMode
from screens.endless_mode import EndlessMode
from screens.settings import Settings
from screens.accounts import Accounts
from screens.leaderboard import Leaderboard

class ToastyNumbersChallengeScreenManager(ScreenManager):
    pass

class ToastyNumbersApp(App):
    def build(self):
        self.title = 'Toasty Numbers Challenge'
       #self.icon = 'assets/images/icon'

        Builder.load_file('kv/home.kv')
        Builder.load_file('kv/rounds_mode.kv')
        Builder.load_file('kv/endless_mode.kv')
        Builder.load_file('kv/settings.kv')
        Builder.load_file('kv/accounts.kv')
        Builder.load_file('kv/leaderboard.kv')

        screen_manager = ToastyNumbersChallengeScreenManager()
        screen_manager.add_widget(Home(name='home'))
        screen_manager.add_widget(RoundsMode(name='rounds_mode'))
        screen_manager.add_widget(EndlessMode(name='endless_mode'))
        screen_manager.add_widget(Settings(name='settings'))
        screen_manager.add_widget(Accounts(name='accounts'))
        screen_manager.add_widget(Leaderboard(name='leaderboard'))

        self.root = screen_manager

        return screen_manager

if __name__ == '__main__':
    ToastyNumbersApp().run()
