from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.list.list import MDListItemHeadlineText
from kivymd.uix.appbar.appbar import MDTopAppBar
from kivy.uix.widget import Widget

KV = '''
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: root.parent.set_color_item(self)

    Widget:
        id: icon
        icon: root.icon
        theme_text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            sourse: "data/logo/kivy-icon-256.png"

    MDLabel:
        text: "KivyMD library"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: "kivydevelopment@gmail.com"
        size_hint_y: None
        height: self.texture_size[1]



    ScrollView:

        DrawerList:
            id: md_list


            
Screen:

    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDScreen:
                        md_bg_color: self.theme_cls.secondaryContainerColor

                        MDTopAppBar:
                            type: "small"
                            size_hint_x: .8
                            pos_hint: {"center_x": .5, "center_y": .5}

                            MDTopAppBarLeadingButtonContainer:

                                MDActionTopAppBarButton:
                                    icon: "menu"

                            MDTopAppBarTitle:
                                text: "AppBar small"
                                pos_hint: {"center_x": .5}

                            MDTopAppBarTrailingButtonContainer:

                                MDActionTopAppBarButton:
                                    icon: "account-circle-outline"
                                    elevation: 10
                                    left_anchor_items:[['menu', lambda x: nav_driwer.set_state("open")]]

                    Widget:


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer


'''

class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(MDListItemHeadlineText):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(MDList, ThemableBehavior ):
    def set_color_item(self, instance_item):
        '''Вызывается, когда нажимаешь на вещь в меню'''

        #Можно установить цвет иконки и добавить текст для вещи в меню
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class TESTCS2GrenadeGuide (MDApp):
    def build(self):
        return Builder.load_string(KV)
    
    def on_start(self):
        Icons_item ={
            "folder": "my files",
            "account-multiple": "Shared with me",
            "star": "Stareed",
            "history": "Recent",
            "checkbox-marked": "Shared with me",
            "upload": "Upload",
        }
        for icon_name in Icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=Icons_item[icon_name])
            )

TESTCS2GrenadeGuide().run()