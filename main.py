from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

from kivy.lang import Builder
from kivy.core.window import Window




toolbar_helper = """
MDTopAppBar:
    type: "large"

    MDTopAppBarLeadingButtonContainer:

        MDActionTopAppBarButton:
            icon: "arrow-left"

    MDTopAppBarTitle:
        text: "AppBar small"

    MDTopAppBarTrailingButtonContainer:

        MDActionTopAppBarButton:
            icon: "attachment"

        MDActionTopAppBarButton:
            icon: "calendar"

        MDActionTopAppBarButton:
            icon: "dots-vertical"

"""

class DemoApp(MDApp):

    def build(self):
        screen = MDScreen(md_bg_color=self.theme_cls.backgroundColor)
        appbar = Builder.load_string(toolbar_helper)
        screen.add_widget(appbar)
        
        return screen



DemoApp().run()