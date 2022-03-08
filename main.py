import json
from calc import calc_value, request_data, get_g, get_aaa
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Intr(App):
    def build(self):
                 
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.95,0.95)
        self.window.pos_hint = {'center_x':0.5,'center_y':0.5}

        self.message = Label(
            text = 'Benjamin Graham Intrinsic Value Calculator',
            font_size = 30,
            size_hint = (1,0.8),
            padding_y = (100,100),
            color = '#00FFCE',
            bold = True,underline = True
        )

        self.window.add_widget(self.message)

        self.user = TextInput(
            multiline=False,
            padding_y = (20,20),
            size_hint = (1,0.8),
            font_size = 20,
            background_color = '#000000',
            foreground_color = '#00FFCE',
            hint_text = 'Enter Ticker'
            )
        self.window.add_widget(self.user)
        self.button = Button(text='Analyse')
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        self.stock = Label(
            text=f'Stock: ',
            font_size = 17,
            size_hint = (1,0.5),color = '#00FFCE'
            )
        self.current = Label(
            text=f'Current Price: ',
            font_size = 17,
            size_hint = (1,0.5),color = '#00FFCE'
            )
        self.intrinsic = Label(
            text=f'Intrinsic Value: ',
            font_size = 17,
            size_hint = (1,0.5),color = '#00FFCE'
            )
        self.upside = Label(
            text=f'Upside: ',
            font_size = 17,
            size_hint = (1,0.5),color = '#00FFCE'
            )
        self.buy = Label(
            text=f'Buy or Sell: ',
            font_size = 17,
            size_hint = (1,0.5),color = '#00FFCE'
            )
        self.error = Label(
            text='',
            font_size= 17,
            size_hint = (1,0.5),
            color = '#FF0000',
        ) 
        self.window.add_widget(self.stock),self.window.add_widget(self.current)
        self.window.add_widget(self.intrinsic),self.window.add_widget(self.upside)
        self.window.add_widget(self.buy),self.window.add_widget(self.error)


        return self.window

    def callback(self,instance):
        try:

            data = request_data(self.user.text.upper())

            current_price = data[0]['ask']
            if current_price == 0:
                current_price = data[0]["regularMarketPrice"]
            long_name = data[0]['longName']
            self.stock.text = f'Stock: {long_name}'
            self.current.text = f'Current Price: £{current_price}'
            eps = data[0]['epsTrailingTwelveMonths']
            growth = get_g(self.user.text.upper())
            aaa = get_aaa()
            calc = calc_value(current_price,eps,growth,aaa)
            int_val, buy, upside = calc['int_val'],calc['buy'],calc['upside']
            print(int_val, upside)

            self.intrinsic.text = f'Intrinsic Value: £{int_val:.2f}'
            self.upside.text = f'Upside: {upside:.2f}%'
            self.buy.text = f'Buy or Sell: {buy}'

            

        except Exception as e:
            self.error.text = f"Error in fetching data for {self.user.text.upper()}. Either ticker is incorrect, Yahoo Finance doesn't have enough data to \nperform the necessary calculations, or daily API calls have expired"
            print(e)
            self.intrinsic.text = f'Intrinsic Value: N/A'
            self.upside.text = f'Upside: N/A'
            self.buy.text = f'Buy or Sell: N/A'



if __name__ == "__main__":
    Intr().run()
