import exceptions_saving


class CalcPayment:

    def __int__(self,amount: float, interest_rate: float, number_payments: int):
        self.amount: float = amount
        self.interest_rate: float = interest_rate
        self.number_payments: int = number_payments
        self.interest_porcentage: float = self.interest_rate / 100

    def