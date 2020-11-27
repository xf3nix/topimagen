import kivy
kivy.require('1.11.1')
from kivy.config import Config
Config.set('graphics', 'width', 340)
Config.set('graphics', 'height', 640)
Config.set('graphics', 'resizable', True)
from os import listdir
from kivymd.app import MDApp
from kivy.lang import Builder
from mysqli import consultaimagen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty


KV = '''
<ContentNavigationDrawer>:  

    orientation: "vertical"
    padding: "60dp"
    spacing: "60dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height        
        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "logo.png"

    ScrollView:    
        MDList:            
            OneLineListItem:
                text: "Inicio"
                on_press:
                    root.nav_drawer.set_state("close")                    
                    root.screen_manager.current = "srcInicio"
                                        
            OneLineListItem:
                text: "Screen 0"
                on_press:
                    app.g1(0)
                    root.nav_drawer.set_state("close")
                    root.screen_manager.transition.direction = "left"                                       
                    root.screen_manager.current = "src0"
            
            OneLineListItem:
                text: "Screen 1"
                on_press:  
                    app.g1(1)
                    root.nav_drawer.set_state("close")
                    root.screen_manager.transition.direction = "left"                                       
                    root.screen_manager.current = "src1"
            
            OneLineListItem:
                text: "Screen 2"
                on_press:
                    app.g1(2)
                    root.nav_drawer.set_state("close")                                       
                    root.screen_manager.transition.direction = "left"
                    root.screen_manager.current = "src2"
            OneLineListItem:
                text: "Screen 3"
                on_press:
                    app.g1(3)
                    root.nav_drawer.set_state("close")                                       
                    root.screen_manager.transition.direction = "left"
                    root.screen_manager.current = "src3"           
                        
            OneLineListItem:                                           
                text: "Salir"
                on_press:
                    app.get_running_app().stop() 
                    
Screen:     
    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager
            Screen:
                name: "srcInicio"                
                MDToolbar:
                    id: toolbar
                    pos_hint: {"top": 1}
                    elevation: 10
                    title: "Empresa"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]                 
                MDLabel:
                    size_hint: 1, 1.7
                    text: app.subtitle
                    halign: "center"    
                        
            Screen:
                name: "src0"
                BoxLayout:
                    padding: [10,10,10,80]                                                                                                                                          
                    Image:                            
                        id: image1Src0
                        source: ''                        
                        allow_stretch: True                        
                BoxLayout:
                    MDIconButton:                                              
                        icon: "arrow-left-bold-circle"
                        size_hint: 0.05, 0.1                         
                        halign:'left'                                       
                        on_press:                            
                            app.ga(0)                                                                                  
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color 
                        user_font_size: "64sp"                    
                    MDIconButton:
                        icon: "close-circle"
                        size_hint: 0.05, 0.1                         
                        halign:'left'
                        on_press: 
                            screen_manager.current = "srcInicio"
                            screen_manager.transition.direction = "right"
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color
                        user_font_size: "64sp"                                
                    MDIconButton:                                           
                        icon: "arrow-right-bold-circle"
                        size_hint: 0.05, 0.1                         
                        halign:'right'                                       
                        on_press:                            
                            app.g1(0)                                                                                 
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color 
                        user_font_size: "64sp"
            Screen:
                name: "src1"
                BoxLayout:
                    padding: [10,10,10,70]                     
                    Image:                            
                        id: image1Src1
                        source: ''
                        allow_stretch: True 
                BoxLayout:
                    MDIconButton:
                        icon: "arrow-left-bold-circle"
                        size_hint: 0.05, 0.1                         
                        halign:'left'                                       
                        on_press:                            
                            app.ga(1)                                                                                  
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color 
                        user_font_size: "64sp"                       
                    MDIconButton:
                        icon: "close-circle"
                        size_hint: 0.05, 0.1                         
                        halign:'left'
                        on_press:                             
                            screen_manager.current = "srcInicio"
                            screen_manager.transition.direction = "right"
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color
                        user_font_size: "64sp"                                
                    MDIconButton:
                        icon: "arrow-right-bold-circle"
                        size_hint: 0.05, 0.1                         
                        halign:'right'                                       
                        on_press:
                            app.g1(1)
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color 
                        user_font_size: "64sp"
            Screen:
                name: "src2"
                BoxLayout:
                    padding: [10,10,10,70]                    
                    Image:                            
                        id: image1Src2
                        source: '' 
                        allow_stretch: True
                BoxLayout:
                    MDIconButton:
                        icon: "arrow-left-bold-circle"
                        size_hint: 0.05, 0.1                         
                        halign:'left'                                       
                        on_press:                            
                            app.ga(2)                                                                                  
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color 
                        user_font_size: "64sp"                       
                    MDIconButton:
                        icon: "close-circle"
                        size_hint: 0.05, 0.1                         
                        halign:'left'
                        on_press:                             
                            screen_manager.current = "srcInicio"
                            screen_manager.transition.direction = "right"
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color
                        user_font_size: "64sp"                                
                    MDIconButton:
                        icon: "arrow-right-bold-circle"
                        size_hint: 0.05, 0.1                         
                        halign:'right'                                       
                        on_press:
                            app.g1(2)
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color 
                        user_font_size: "64sp"
            Screen:
                name: "src3"
                BoxLayout:
                    padding: [10,10,10,70]                    
                    Image:                            
                        id: image1Src3
                        source: '' 
                        allow_stretch: True
                BoxLayout:
                    MDIconButton:
                        icon: "arrow-left-bold-circle"
                        size_hint: 0.05, 0.1                         
                        halign:'left'                                       
                        on_press:                            
                            app.ga(3)                                                                                  
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color 
                        user_font_size: "64sp"                       
                    MDIconButton:
                        icon: "close-circle"
                        size_hint: 0.05, 0.1                         
                        halign:'left'
                        on_press:                             
                            screen_manager.current = "srcInicio"
                            screen_manager.transition.direction = "right"
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color
                        user_font_size: "64sp"                                
                    MDIconButton:
                        icon: "arrow-right-bold-circle"
                        size_hint: 0.05, 0.1                         
                        halign:'right'                                       
                        on_press:
                            app.g1(3)
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color 
                        user_font_size: "64sp"                      
        
        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:    
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.screen = Builder.load_string(KV)

    subtitle = StringProperty("Bienvenidos")
    ruta = 'imagenes/'
    id = []
    x0 = []
    x1 = []
    x2 = []
    x3 = []

    def cimagen(self):
        image = consultaimagen()
        try:
            for row in image:
                self.id.append(row)
                foto = row[2]
                fout = open('imagenes/foto' + str(row[3]) + str(row[0]), 'wb')
                fout.write(foto)
                fout.close()
        except:
            self.subtitle = "Sin Conexion"
            pass

    def lista(self):

        esrc0 = []
        esrc1 = []
        esrc2 = []
        esrc3 = []

        try:
            for i in listdir(self.ruta):
                if i[4] == "0":
                    esrc0.append(self.ruta + i)
                elif i[4] == "1":
                    esrc1.append(self.ruta + i)
                elif i[4] == "2":
                    esrc2.append(self.ruta + i)
                elif i[4] == "3":
                    esrc3.append(self.ruta + i)

            self.itr0 = iter(esrc0)
            self.itr1 = iter(esrc1)
            self.itr2 = iter(esrc2)
            self.itr3 = iter(esrc3)

        except:
            pass

    def g1(self, event):
        try:
            if event == 0:
                self.x0.append(self.screen.ids.image1Src0.source)
                self.screen.ids.image1Src0.source = self.itr0.__next__()
            elif event == 1:
                self.x1.append(self.screen.ids.image1Src1.source)
                self.screen.ids.image1Src1.source = self.itr1.__next__()
            elif event == 2:
                self.x2.append(self.screen.ids.image1Src2.source)
                self.screen.ids.image1Src2.source = self.itr2.__next__()
            elif event == 3:
                self.x3.append(self.screen.ids.image1Src3.source)
                self.screen.ids.image1Src3.source = self.itr3.__next__()

        except StopIteration:
            self.lista()
            self.g1(0)
            self.g1(1)
            self.g1(2)
            self.g1(3)
        except AttributeError:
            pass

    def ga(self, event):
        try:
            if event == 0:
                self.screen.ids.image1Src0.source = self.x0.pop()
            elif event == 1:
                self.screen.ids.image1Src1.source = self.x1.pop()
            elif event == 2:
                self.screen.ids.image1Src2.source = self.x2.pop()
            elif event == 3:
                self.screen.ids.image1Src3.source = self.x3.pop()

        except IndexError:
            self.lista()
            self.g1(0)
            self.g1(1)
            self.g1(2)
            self.g1(3)

    def build(self):
        self.cimagen()
        self.lista()
        return self.screen


class MainApp(MDApp):
    title = "App Presenta"

    def build(self):
        #self.theme_cls.theme_style = "Light"  # "Light" o "Dark"
        #self.theme_cls.primary_palette = "Red"  # 'Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue',
        # 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange',
        # 'Brown', 'Gray', 'BlueGray'
        return Test().run()


if __name__ == "__main__":
    MainApp().run()
