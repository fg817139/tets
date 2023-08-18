import unittest
import jp
import excepciones

class TestCalcularIntereses(unittest.TestCase):

    def test_calculo_intereses_1(self):
        monto = 200000
        tasa = 3.1
        cuotas = 36
        total_intereses_calculados = round(jp.interes_total(monto, tasa, cuotas),2)
        total_intereses_esperados = 134726.53
        self.assertAlmostEqual(total_intereses_calculados, total_intereses_esperados)

    def test_calcular_intereses_2(self):
        monto = 850000
        tasa = 3.4
        cuotas = 24
        total_intereses_calculados = round(jp.interes_total(monto, tasa, cuotas), 2)
        total_intereses_esperados = 407059.97
        self.assertAlmostEqual(total_intereses_calculados, total_intereses_esperados)

    def testNoIntereres(self):
        monto = 480000
        tasa = 0
        cuotas = 48
        resultado = round((jp.interes_total)(monto, tasa, cuotas), 2)
        esperado = 0
        self.assertEqual(resultado, esperado)

    def testUsura(self):
        monto = 50000
        tasa = 12.4
        coutas = 48
        self.assertRaises(excepciones.Usura,jp.cuota_mensual,monto,tasa,coutas)

    def testUnaCuota(self):
        monto = 90000
        tasa = 2.4
        cuotas = 1
        resultado = round(jp.interes_total(monto,tasa,cuotas),2)
        esperado = 0
        self.assertEqual(resultado,esperado)

    def testNOMonto(self):
        monto = 0
        tasa = 2.4
        coutas = 60
        self.assertRaises(excepciones.MontoNulo,jp.cuota_mensual, monto,tasa,coutas)

    def testCuotas(self):
        monto = 50000
        tasa = 1
        cuotas = -10
        self.assertRaises(excepciones.CuotaNegativa, jp.cuota_mensual, monto, tasa, cuotas)




if __name__ == '__main__':
    unittest.main()

