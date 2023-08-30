import unittest
import calculating
import exceptions

class TestCalcularIntereses(unittest.TestCase):

    def test_calculo_intereses_1(self):
        amount = 200000
        interest = 3.1
        periods = 36
        total_calculated_interest = round(calculating.interes_total(amount,interest , periods),2)
        total_expected_interest = 134726.53
        self.assertAlmostEqual(total_calculated_interest, total_expected_interest)

    def test_calcular_intereses_2(self):
        amount = 850000
        interest = 3.4
        periods = 24
        total_calculated_interest = round(calculating.interes_total(amount, interest, periods), 2)
        total_expected_interest = 407059.97
        self.assertAlmostEqual(total_calculated_interest, total_expected_interest)

    def testNoIntereres(self):
        amount = 480000
        interest = 0
        periods = 48
        result = round((calculating.interes_total)(amount, interest, periods), 2)
        expected = 0
        self.assertEqual(result, expected)

    def testUsura(self):
        amount = 50000
        interest = 12.4
        periods = 48
        self.assertRaises(exceptions.Usura,calculating.cuota_mensual,amount,interest,periods)

    def testUnaCuota(self):
        amount = 90000
        interest = 2.4
        periods = 1
        result = round(calculating.interes_total(amount,interest,periods),2)
        expected = 0
        self.assertEqual(result,expected)

    def testNOMonto(self):
        amount = 0
        interest = 2.4
        periods = 60
        self.assertRaises(exceptions.MontoNulo,calculating.cuota_mensual, amount,interest,periods)

    def testCuotas(self):
        amount = 50000
        interest = 1
        periods = -10
        self.assertRaises(exceptions.CuotaNegativa, calculating.cuota_mensual, amount, interest, periods)




if __name__ == '__main__':
    unittest.main()

