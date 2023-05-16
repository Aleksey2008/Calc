from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.scores = []

    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Введите оценку от 2 до 5:")
        layout.add_widget(self.label)

        self.text_input = TextInput(multiline=False)
        layout.add_widget(self.text_input)

        button = Button(text="Добавить", on_release=self.add_score)
        layout.add_widget(button)

        self.result_label = Label(text="")
        layout.add_widget(self.result_label)

        return layout

    def add_score(self, instance):
        try:
            score = int(self.text_input.text)
            if score >= 2 and score <= 5:
                self.scores.append(score)
            else:
                self.result_label.text = "Неверное значение. Введите оценку от 2 до 5"
        except ValueError:
            self.result_label.text = "Неверное значение"

        self.text_input.text = ""

        if len(self.scores) > 0:
            average = sum(self.scores) / len(self.scores)
            self.result_label.text = "Средняя оценка: {:.2f}".format(average)

if __name__ == '__main__':
    MyApp().run()
