from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton,MDFillRoundFlatButton,MDIconButton,MDTextButton

username_input = """
MDTextField:
    hint_text: "Enter your email.id"
    helper_text_mode: "on_focus"
    icon_right:"account"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.6}
    size_hint_x:None
    width:300
"""


username_input2 = """
MDTextField:
    hint_text: "Enter password"
    icon_right: "eye_off"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
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

    MDLabel:
        text: "Hello, World!"
        halign: 'center'
        font_style: 'H4'
'''


class Green_tie(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Green"
        screen = Screen()
        button = MDFlatButton(text="signin" , pos_hint={'center_x':0.5 , 'center_y':0.3} )
        button2= MDTextButton(text="forgot password ?" , pos_hint={'center_x':0.4 , 'center_y':0.4} )
        username = Builder.load_string(username_input)
        username2 = Builder.load_string(username_input2)
        screen.add_widget(username)
        screen.add_widget(username2)
        screen.add_widget(button)
        screen.add_widget(button2)

    
        return Builder.load_string(KV)

       
       
        





Green_tie().run()