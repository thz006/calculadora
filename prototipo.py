from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

from kivy.core.window import Window
Window.size = (400,700)

class Mycalc(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.display = Label(text='Bem vindo')


        
        caixa_botoes= GridLayout(cols=4)
        self.botao1 = Button(text='0')
        self.botao2 = Button(text='1')
        self.botao3 = Button(text='2')
        self.botao4 = Button(text='3')
        self.botao5 = Button(text='4')
        self.botao6 = Button(text='5')
        self.botao7 = Button(text='6')
        self.botao8 = Button(text='7')
        self.botao9 = Button(text='8')
        self.botao10 = Button(text='9')
        self.botao_mais = Button(text='+')
        self.botao_menos = Button(text='-')
        self.botao_vezes = Button(text='*')
        self.botao_divido = Button(text='/')
        self.botao_potencia = Button(text='^')
        self.botao_raiz4 = Button(text='√4')
        self.botao_igual = Button(text='=')
        self.botao0= Button(text='C')
        self.botao_delete1 = Button(text='<-')

        caixa_botoes.add_widget(self.botao1)
        caixa_botoes.add_widget(self.botao2)
        caixa_botoes.add_widget(self.botao3)
        caixa_botoes.add_widget(self.botao4)
        caixa_botoes.add_widget(self.botao5)
        caixa_botoes.add_widget(self.botao6)
        caixa_botoes.add_widget(self.botao7)
        caixa_botoes.add_widget(self.botao8)
        caixa_botoes.add_widget(self.botao9)
        caixa_botoes.add_widget(self.botao10)
        caixa_botoes.add_widget(self.botao_mais)
        caixa_botoes.add_widget(self.botao_menos)
        caixa_botoes.add_widget(self.botao_vezes)
        caixa_botoes.add_widget(self.botao_divido)
        caixa_botoes.add_widget(self.botao_potencia)
        caixa_botoes.add_widget(self.botao_raiz4)
        caixa_botoes.add_widget(self.botao0)
        caixa_botoes.add_widget(self.botao_delete1)
        caixa_botoes.add_widget(self.botao_igual)


        layout.add_widget(self.display)
        layout.add_widget(caixa_botoes)

        self.botao0.bind(on_press = self.zerar)
        self.botao1.bind(on_press = self.armazenar)
        self.botao2.bind(on_press = self.armazenar)
        self.botao3.bind(on_press = self.armazenar)
        self.botao4.bind(on_press = self.armazenar)
        self.botao5.bind(on_press = self.armazenar)
        self.botao6.bind(on_press = self.armazenar)
        self.botao7.bind(on_press = self.armazenar)
        self.botao8.bind(on_press = self.armazenar)
        self.botao9.bind(on_press = self.armazenar)
        self.botao10.bind(on_press = self.armazenar)
        self.botao_mais.bind(on_press = self.armazenar)
        self.botao_menos.bind(on_press = self.armazenar)
        self.botao_vezes.bind(on_press = self.armazenar)
        self.botao_divido.bind(on_press = self.armazenar)
        self.botao_potencia.bind(on_press = self.armazenar)
        self.botao_raiz4.bind(on_press = self.armazenar)
        self.botao_igual.bind(on_press = self.calcular)
        self.botao_delete1.bind(on_press = self.apagar)


        return layout

    def zerar(self,event):
        self.display.text = ''

    def apagar(self,event):
         if self.display.text:
          current_text = self.display.text
          self.display.text = current_text[:-1]
    
    def armazenar(self,event):
        self.display.text += event.text

    def calcular(self,event):
         
        if "+" in self.display.text:
             numbers= self.display.text.split("+")
             soma = int(numbers[0]) + int(numbers[1])
             self.display.text = str(soma)
        
        elif "-" in self.display.text:
             numbers= self.display.text.split("-")
             sub = int(numbers[0]) - int(numbers[1])
             self.display.text = str(sub)
            
        elif "*" in self.display.text:
             numbers= self.display.text.split("*")
             vezes = int(numbers[0]) * int(numbers[1])
             self.display.text = str(vezes)
            
        elif "/" in self.display.text:
             numbers= self.display.text.split("/")
             divsao = int(numbers[0]) / int(numbers[1])
             self.display.text = str(divsao)
        
        elif "^" in self.display.text:
             numbers= self.display.text.split("^")
             potencia = int(numbers[0]) ** int(numbers[1])
             self.display.text = str(potencia)

        elif "√4" in self.display.text:
             numbers= self.display.text.split("√4")
             raiz4 = int(numbers[0]) ** 0.5
             self.display.text = str(raiz4)



if __name__ == "__main__":
    Mycalc().run()