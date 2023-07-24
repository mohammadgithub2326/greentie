from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.core.window import Window



Builder.load_string('''
<HomeScreen>:
    #topbar items
    ScrollView:
        MDList:
            MDBoxLayout:              
                height:root.height
                size_hint_y: None
                FitImage:
                    size_hint_y: 0.3
                    source: 'sc01.png'
            MDBoxLayout:              
                height:root.height
                size_hint_y: None
                FitImage:
                    size_hint_y: 0.3
                    source: 'sc02.png'
            MDBoxLayout:              
                height:root.height
                size_hint_y: None
                FitImage:
                    size_hint_y: 0.3
                    source: 'sc03.png'
    MDBoxLayout:
        orientation:"vertical"
        title:"green tie"
    MDTopAppBar:
        md_bg_color: 9,6,9,0
        font_name:"fonts/font02.ttf " 
        font_color:0,1,0
        md_bg_color: app.theme_cls.primary_color
        
    # Scroll:
    #     id:scroll
    #     effect_cls:'ScrollEffect'
    #     bar_width:0
    #     MDBoxLayout:
    #         id:b1
    #         adaptive_height:True
    #         orientation:'vertical'
    #         MDBoxLayout:
    #             height:root.height
    #             size_hint_y: None
    #             FitImage:
    #                 size_hint_y: 0.3
    #                 source: 'sc01.png'
    #                 text:"green tie"
    
    # MDBottomAppBar:
    #     md_bg_color: 9,6,9,0
    #     MDTopAppBar:
            
    #         font_color:(1,0,0,1)
            
    #         type: "bottom"    
            
    # MDIconButton:
    #     icon: "arrow-left" 
    #     pos_hint: {"center_x": 0.1, "center_y":0.95}
       
    #     on_release: app.screen_manager.current = 'home'
                    
   
    MDLabel:
        text:"Green Tie"
        pos_hint:{"center_x": 0.6, "center_y":0.95}
                    


    
         #bottom bar items   
    MDIconButton:
        icon: 'home'
        pos_hint: {'center_x': 0.9, 'center_y': 0.15}
        md_bg_color: 0.7,.9,0.2
        on_release: app.screen_manager.current = 'page1'
    
                    
    MDIconButton:
        icon: "wardrobe" 
        pos_hint: {"center_x": 0.1, "center_y":.050}
       
        on_release: app.screen_manager.current = 'page2'
    MDIconButton:
        icon: "camera" 
        pos_hint: {"center_x": .35, "center_y":.050}
       
        on_release: app.screen_manager.current = 'page3'
    MDIconButton:
        icon: "shopping" 
        pos_hint: {"center_x": .65, "center_y":.050}
       
        on_release: app.screen_manager.current = 'page4'
    MDIconButton:
        icon: "spa" 
        pos_hint: {"center_x": .9, "center_y":.050}
       
        on_release: app.screen_manager.current = 'page5'
   
    
    


<Page1Screen>:
    MDTopAppBar:
        md_bg_color: 0.5, 1, 0.5
        MDTopAppBar:
            
            
            elevation: 6
            title:"Fashion Teaching Ai"
    
    MDLabel:
        text:"Wanna Update About You ?"
        pos_hint:{"center_x": 0.7, "center_y":0.58}

    MDFloatLayout:
        orientation:'vertical'
        spacing: '10dp'
        Image:
            source: 'gtlogo.png'
            allow_stretch: True
            pos_hint:{'center_x': 0.5, 'center_y': 0.8} 
        MDTextField:
            id: text_field2
            hint_text: 'Update Your Height'
            multiline: True
            pos_hint:{'center_x': 0.5, 'center_y': 0.5}
            size_hint_x:'.7'
        MDTextField:
            id: text_field2
            hint_text: 'Update Your Skin Type'
            multiline: True
            pos_hint:{'center_x': 0.5, 'center_y': 0.4}
            size_hint_x:'.7'
        MDTextField:
            id: text_field2
            hint_text: 'Update Your Hair Type'
            multiline: True
            pos_hint:{'center_x': 0.5, 'center_y': 0.3}
            size_hint_x:'.7'
        MDRoundFlatButton:
            text:"save"
            pos_hint:{'center_x':0.8,'center_y':0.95}
            md_bg_color:0,0.6,0.4
        MDTextButton:
            text:"Wanna Edit Your WardRobe ?"
            pos_hint:{'center_x': 0.4, 'center_y': 0.24}
            on_release: app.screen_manager.current = 'page2'            
                    
        MDTextButton:
            text:"Faviourets"
            pos_hint:{'center_x': 0.21, 'center_y': 0.18}
        MDIconButton:
            icon: "arrow-left" 
            pos_hint: {"center_x": 0.1, "center_y":0.95}
            on_release: app.screen_manager.current = 'home'
                        
<Page2Screen>:
   
   
    MDTopAppBar:
        md_bg_color: 0.5, 1, 0.5
        MDTopAppBar:
            
            
            elevation: 6
            title:"Fashion Teaching Ai"
            
            
        
    MDLabel:
        text:"Your Collecions"
        pos_hint:{"center_x": 0.7, "center_y":0.95}

   

   
    MDIconButton:
        icon: "arrow-left" 
        pos_hint: {"center_x": 0.1, "center_y":0.95}
       
        on_release: app.screen_manager.current = 'home'
    MDTextButton:
        text:"Party Wear"
        pos_hint:{'center_x': 0.5, 'center_y': 0.8}
        on_release:  app.screen_manager.current = 'weartype'
    MDTextButton:
        text:"Traditional Wear"
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        on_release:  app.screen_manager.current = 'weartype'
    MDTextButton:
        text:"Street Wear"
        pos_hint:{'center_x': 0.5, 'center_y': 0.4}
        on_release:  app.screen_manager.current = 'weartype'
    MDTextButton:
        text:"Formal Wear"
        pos_hint:{'center_x': 0.5, 'center_y': 0.2}
        on_release:  app.screen_manager.current = 'weartype'
    
<Page3Screen>:
                    
    MDTopAppBar:
        md_bg_color: 0.5, 1, 0.5
        MDTopAppBar:
            
            
            elevation: 6
            title:"Fashion Teaching Ai"
   
    MDLabel:
        text:"Show Me Your Collection"
        pos_hint:{"center_x": 0.7, "center_y":0.95}
    MDTextButton:
        text:"Party Wear"
        pos_hint:{'center_x': 0.5, 'center_y': 0.8}
        # on_release:  app.screen_manager.current = 'weartype'
    MDTextButton:
        text:"Traditional Wear"
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        # on_release:  app.screen_manager.current = 'weartype'
    MDTextButton:
        text:"Street Wear"
        pos_hint:{'center_x': 0.5, 'center_y': 0.4}
        # on_release:  app.screen_manager.current = 'weartype'
    MDTextButton:
        text:"Formal Wear"
        pos_hint:{'center_x': 0.5, 'center_y': 0.2}
        # on_release:  app.screen_manager.current = 'weartype'
    MDIconButton:
        icon: "arrow-left" 
        pos_hint: {"center_x": 0.1, "center_y":0.95}
       
        on_release: app.screen_manager.current = 'home'
<Page4Screen>:
    MDLabel:
        text:"Local Stores"
        pos_hint:{"center_x": 0.7, "center_y":0.95}
    MDTopAppBar:
        md_bg_color: 0.5, 1, 0.5
        MDTopAppBar:
            
            
            elevation: 6
            title:"Fashion Teaching Ai"
            
    MDIconButton:
        icon: "arrow-left" 
        pos_hint: {"center_x": 0.1, "center_y":0.95}
        
        on_release: app.screen_manager.current = 'home'
    MDIconButton:
        icon: "plus-circle" 
                    
        pos_hint: {"center_x": 0.9, "center_y":0.15}
       
                    
<Page5Screen>:
    MDLabel:
        text:"Local Saloons"
        pos_hint:{"center_x": 0.7, "center_y":0.95}
    MDTopAppBar:
        md_bg_color: 0.5, 1, 0.5
        MDTopAppBar:
            
            
            elevation: 6
            title:"Fashion Teaching Ai"
            
    MDIconButton:
        icon: "arrow-left" 
        pos_hint: {"center_x": 0.1, "center_y":0.95}
       
        on_release:  app.screen_manager.current = 'home'
<WearType>:
    MDTopAppBar:
        md_bg_color: 0.5, 1, 0.5
        MDTopAppBar:
            
            
            elevation: 6
            title:"Fashion Teaching Ai"
            
            
        
    MDLabel:
        text:"Your Collecions"
        pos_hint:{"center_x": 0.7, "center_y":0.95}

   

   
    MDIconButton:
        icon: "arrow-left" 
        pos_hint: {"center_x": 0.1, "center_y":0.95}
       
        on_release: app.screen_manager.current = 'page2'
    MDTextButton:
        text:"Tops"
        pos_hint:{'center_x': 0.5, 'center_y': 0.8}
    MDTextButton:
        text:"Bottoms"
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
    MDTextButton:
        text:"Accessoriess"
        pos_hint:{'center_x': 0.5, 'center_y': 0.4}
    MDTextButton:
        text:"Foot Wear"
        pos_hint:{'center_x': 0.5, 'center_y': 0.2}             

                    
''')


class HomeScreen(Screen):
    pass


class Page1Screen(Screen):
    pass


class Page2Screen(Screen):
    pass
class Page3Screen(Screen):
    pass
class Page4Screen(Screen):
    pass
class Page5Screen(Screen):

    pass
class WearType(Screen):
    pass
class GreenTie(MDApp):
    def build(self):
        self.theme_cls.primary_palette='LightGreen'
        self.theme_cls.theme_style='Dark'
        self.screen_manager = ScreenManager(transition=FadeTransition())
        self.icon = "logo.png"
       
        self.screen_manager.add_widget(HomeScreen(name='home'))
        self.screen_manager.add_widget(Page1Screen(name='page1'))
        self.screen_manager.add_widget(Page2Screen(name='page2'))
        self.screen_manager.add_widget(Page3Screen(name='page3'))
        self.screen_manager.add_widget(Page4Screen(name='page4'))
        self.screen_manager.add_widget(Page5Screen(name='page5'))
        self.screen_manager.add_widget(WearType(name='weartype'))
    
        return self.screen_manager
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition,SwapTransition,FadeTransition
Window.size = (340,640)
if __name__ == '__main__':
    GreenTie().run()
