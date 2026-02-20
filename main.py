import os

# 🔹 Forcer un backend graphique compatible
# "angle_sdl2" ou "software" pour éviter SIGSEGV sur Samsung/Exynos
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

# 🔹 Optionnel : désactiver la mise à l'échelle Kivy pour tests
os.environ['KIVY_NO_CONSOLELOG'] = '1'
os.environ['KIVY_NO_FILELOG'] = '1'

from kivy.app import App
from kivy.uix.label import Label
from kivy.logger import Logger

Logger.info("APP: Starting main.py")

class SafeApp(App):
    def build(self):
        Logger.info("APP: build() called")
        return Label(text='Hello World!')

if __name__ == '__main__':
    Logger.info("APP: Running SafeApp")
    SafeApp().run()
