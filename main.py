from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
import requests

######COMPONENTES

#date/explanation/title/url
#################


link = "https://api.nasa.gov/planetary/apod?api_key=bQEMZvcXPqqhIKtBkZVTeqlkTxSJ0t4YZGa126gS"

resposta = requests.get(link)
content = resposta.json()

titulo = content["title"]
data = content["date"]
url = content["url"]
# E MAIS TARDE DEVO COLOCAR IMAGEM

kv = ''' 
<Tela>:
    orientation: "vertical"

    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "back.jpg"

    ActionBar:
        pos_hint: {"top": 1}
        background_color: 1, 1, 1, 0

        ActionView:
            ActionPrevious:
                title: "WikiNasa"
                app_icon: ''
                with_previous: False

    ScrollView:
        BoxLayout:
                
            orientation: "vertical"
            size_hint_y: None
                    
            
            GridLayout:
                cols: 1
                spacing: 30

                
                AsyncImage:
                    source: (root.image)
                    size_hint_y: None
                    size:self.image_ratio*root.height,root.height
                    mipmap: True     
                    
            GridLayout:
                cols: 1
                spacing: 25
                padding: [20, 110]

                Label:
                    text: str(root.title)
                    bold: True
                    font_size: self.width/20



                    

            GridLayout:
                cols: 1
                spacing: 30
                padding: [20, 120]

                Label:
                    text: str(root.lin)
                    font_size: self.width/40

                    
        
'''

Builder.load_string(kv)


class Tela(BoxLayout):
    title = titulo
    image = url
    lin = url


class WikiNasa(App):
    def build(self):
        return Tela()


WikiNasa().run()

