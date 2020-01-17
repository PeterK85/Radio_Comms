# guizero on the interwebs
from guizero import App, Text, PushButton, Window
app = App(title="Hello World")

message = Text(app, text="This is some text")
text = Text(app)

def say_hello():
    text.value = "hello world"

button = PushButton(app, command=say_hello)

window = Window(app, title="second window")

app.display()
