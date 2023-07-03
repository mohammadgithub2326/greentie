from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton,MDTextButton
from kivy.core.window import Window
from kivy.uix.image import Image

username_input = """
MDTextField:
    hint_text: "Enter your email.id"
    helper_text_mode: "on_focus"
    icon_right:"account"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width:300
"""


username_input2 = """
MDTextField:
    hint_text: "Enter password"
    icon_right: "eye_off"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.4}
    size_hint_x:None
    width:300
"""
KV = '''
BoxLayout:
    orientation: 'vertical'

    BoxLayout:
        Image:
            source: 'gtlogo.png'
            allow_stretch: True
            pos_hint:{'center_x': 0.5, 'center_y': 0.8}
    
'''


class Green_tie(MDApp):
    def build(self):
        self.theme_cls.primary_palette='Green'
        self.theme_cls.theme_style='Dark'
        layout = MDFloatLayout()
        button = MDFlatButton(text="signin" , pos_hint={'center_x':0.5, 'center_y':0.2} )
        button2= MDTextButton(text="forgot password ?" , pos_hint={'center_x':0.4 , 'center_y':0.3} )
        username = Builder.load_string(username_input)
        username2 = Builder.load_string(username_input2)
        image = Builder.load_string(KV)
        layout.add_widget(username)
        layout.add_widget(username2)
        layout.add_widget(button)
        layout.add_widget(button2)
        layout.add_widget(image)
       
        return layout
    
Window.size = (360,640)
Green_tie().run()













