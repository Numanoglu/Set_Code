class Card():
    def __init__(self, name, colour, quantity, form, plenty):
        self.name = name
        self.colour = colour
        self.form = form
        self.plenty = plenty
        self.quantity = quantity
        self.card_attr = {
            'full':
                {
                    'Spade': '♠',
                    'Heart': '♥',
                    'Club': '♣'
                },
            'empty':
                {
                    'Spade': '♤',
                    'Heart': '♡',
                    'Club': '♧'
                },
            'dashed':
                {
                    'Spade': '🂡',
                    'Heart': '🂱',
                    'Club': '🃑'
                },
        }
        self.card_color = {
            'lila':(204,0,204),
            'blue': (0,0,255),
            'green': (0,255,0)
        }


    def __repr__(self):
        return "<" + " ".join((self.name, self.colour, self.form, self.plenty, self.quantity)) + ">"

    def __str__(self):
        return " ".join((self.name, self.colour, self.form, self.plenty, self.quantity))

    def pretty_print(self):
        return self.card_attr[self.plenty][self.form] * int(self.quantity)

    def get_color(self):
        return self.card_color[self.colour]