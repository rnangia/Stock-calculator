import re
import subprocess
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.lang import Builder
import kivy

Builder.load_string('''
<ScrollableLabel>:
    Label:
        size_hint: 1, None
        height: self.texture_size[1]
        text: root.text
''')

class ScrollableLabel(ScrollView):
    text = StringProperty('')

class FloatInput(TextInput):
    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)

class CalculateSharesCanBuyForMoney(GridLayout):
    def __init__(self, **kwargs):
        super(CalculateSharesCanBuyForMoney, self).__init__(**kwargs)
        self.cols = 2

        def on_money_change(instance, value):
            print('The widget', instance, 'have:', value)
            self.money = value

        self.add_widget(Label(text='Money'))
        money = FloatInput(multiline=False)
        money.bind(text=on_money_change)
        self.add_widget(money)

        def on_share_price_change(instance, value):
            print('The widget', instance, 'have:', value)
            self.share_price = value

        self.add_widget(Label(text='Share Price'))
        share_price = FloatInput(multiline=False)
        share_price.bind(text=on_share_price_change)
        self.add_widget(share_price)

        self.first_trade = False
        def on_checkbox_active(checkbox, value):
            if value:
                print('The checkbox', checkbox, 'is active')
                self.first_trade = True
            else:
                print('The checkbox', checkbox, 'is inactive')
                self.first_trade = False

        self.add_widget(Label(text='First Trade'))
        first_trade = CheckBox()
        first_trade.bind(active=on_checkbox_active)
        self.add_widget(first_trade)

        # m = 'yay moo cow foo bar moo baa ' * 500
        def calculate_shares_for_money(instance):
            # scroll = ScrollView()
            print("The button is being pressed ", instance.text)
            print(self.money, self.share_price, self.first_trade)
            op = subprocess.check_output("python /Users/jinxedin/Documents/Stocks/code/shareforpricecalc.py {} {} -ft {}".format(self.money, self.share_price, self.first_trade), shell=True)
            res = Popup(title="Result", content=ScrollableLabel(text=op.decode('ascii')))
            # res = Popup(title="Result", content=ScrollableLabel(text=m))
            res.open()

        # print("The variables are", self.money.text, self.share_price.text, self.first_trade.active)
        calculate = Button(text='Calculate')
        calculate.bind(on_press=calculate_shares_for_money)
        self.add_widget(calculate)





class StockApp(App):
    def build(self):
        return CalculateSharesCanBuyForMoney(row_force_default=True, row_default_height=50, col_force_default=True, col_default_width=kivy.metrics.dp(100))

StockApp().run()
