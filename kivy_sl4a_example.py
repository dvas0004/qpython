import androidhelper
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
	def buttonPress(self,instance):
	    droid = androidhelper.Android()
	    line = droid.dialogGetInput()
    	    s = 'Hello %s' % line.result
            droid.makeToast(s)

        def build(self):
	    btn1 = Button(text='Hello world 1')
            btn1.bind(on_press=self.buttonPress)
            return btn1

TestApp().run()
