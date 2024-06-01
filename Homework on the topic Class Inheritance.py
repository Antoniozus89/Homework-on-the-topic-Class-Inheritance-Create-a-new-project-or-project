class Car:
    PRICE = 1000000

    def __init__(self, model):
        self.model = model

    def horse_powers(self):
        self.horse_powers = 400
        return self.horse_powers

    def __str__(self):
        return '{} цена {}, мощность двигателя {}'.format( self.model, self.PRICE,
                                                             self.horse_powers)

class Nissan(Car):
    PRICE = 1300000

    def horse_powers(self):
        self.horse_powers = 500


class Kia(Car):
    PRICE = 1100000

    def horse_powers(self):
        self.horse_powers = 450


kashkai = Nissan(model = 'Кашкай')
kashkai.horse_powers()
print(kashkai)

cerato = Kia(model = 'Серато')
cerato.horse_powers()
print(cerato)