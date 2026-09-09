TRIP_COST = 20

class TransportCard:
    def __init__(self, owner):
        self.__owner = owner
        self.__balance = 0

    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return self.__balance

    def add_money(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть больше нуля")
        self.__balance += amount

    def pay_for_trip(self):
        if self.__balance < TRIP_COST:
            raise ValueError("Недостаточно средств на карте")
        self.__balance -= TRIP_COST

if __name__ == "__main__":
    card1 = TransportCard("Паша")
    card2 = TransportCard("Александр")

    try:
        card1.add_money(50)
        card2.add_money(15)
    except ValueError as e:
        print("Ошибка пополнения:", e)

    try:
        card1.pay_for_trip()
        card1.pay_for_trip()
    except ValueError as e:
        print("Ошибка при поездке Паши:", e)

    try:
        card2.pay_for_trip()
    except ValueError as e:
        print("Ошибка при поездке Александра:", e)

    print("Владелец:", card1.get_owner(), "Баланс:", card1.get_balance())
    print("Владелец:", card2.get_owner(), "Баланс:", card2.get_balance())


















