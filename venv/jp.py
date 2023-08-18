import excepciones


def cuota_mensual(monto,tasa,cuotas):
    p = tasa/100
    if monto == 0:
        raise excepciones.MontoNulo
    elif tasa*12 > 100:
        raise excepciones.Usura
    elif cuotas <= 0:
        raise excepciones.CuotaNegativa
    elif cuotas == 1:
        return monto
    elif tasa == 0:
        return monto/cuotas
    else:
        return (monto * p)/(1 - (1 + p)**(-cuotas))


def interes_total(monto,tasa,cuotas):
    valor_cuota = cuota_mensual(monto, tasa, cuotas)
    total_intereses = (valor_cuota * cuotas) - monto
    return total_intereses


def amortizacion(monto, tasa, cuotas):
    valor_cuota = cuota_mensual(monto, tasa, cuotas)
    print(valor_cuota)
    saldo = monto
    interes_total=tasa/100
    tabla_amortizacion = []
    if cuotas == 1:
        numero_cuota = 1
        interes_total = 0
        abono_capital = (valor_cuota - interes_total, )
        fila = [numero_cuota, saldo, interes_total, abono_capital]
        tabla_amortizacion.append(fila)
    else:
        for cuota in range(1, cuotas + 1):
            numero_cuota = cuota
            interes = (interes_total * saldo)
            abono_capital = round(valor_cuota - interes)
            saldo = (saldo - abono_capital)

            fila = [numero_cuota, saldo, interes, abono_capital]
            tabla_amortizacion.append(fila)
            print(fila)

    return tabla_amortizacion

def extra(tabla_amortizacion, cuota, abono, interes, valor_cuotas):
    saldo_restante = tabla_amortizacion[cuota-2][1]
    porcentaje_interes = interes / 100
    tabla_amortizacion_abono_extra = []
    for j in range (tabla_amortizacion[cuota-1][0], 36):
        numero_cuota = j
        interes: float = round(porcentaje_interes * saldo_restante, 2)
        if numero_cuota == tabla_amortizacion[cuota-1][0]:
            abono_capital: float = round(abono - interes, 2)
        else:
            abono_capital: float = round(valor_cuotas - interes, 2)
        saldo_restante: float = round(saldo_restante - abono_capital, 2)
        if saldo_restante <= 0:
            saldo_restante = 0
        fila = [numero_cuota, saldo_restante, interes, abono_capital]
        tabla_amortizacion_abono_extra.append(fila)
        if saldo_restante <= 0:
            break
    return tabla_amortizacion_abono_extra



monto = float( input("Monto de la compra:") )
cuotas = int( input("Numero de cuotas en que va a diferir la compra:") )
tasa_interes = float( input("Tasa de interés de la tarjeta:") )
abono_extra = float(input("ingrese abono extra:"))
cuota_extra = int(input("ingrese cuota extra:"))
tabla= amortizacion(monto,tasa_interes,cuotas)
valor_cuota = cuota_mensual(monto,tasa_interes,cuotas)

print(extra(tabla,cuota_extra,abono_extra, tasa_interes, valor_cuota))
