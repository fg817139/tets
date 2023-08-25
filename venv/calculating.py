import exceptions


def monthly_quota(amount,interest,periods):
    p = interest/100
    if amount == 0:
        raise exceptions.Zero_amount
    elif interest*12 > 100:
        raise exceptions.Usura
    elif periods <= 0:
        raise exceptions.amountNegativa
    elif interest == 1:
        return amount
    elif interest == 0:
        return amount/periods
    else:
        return (amount * p)/(1 - (1 + p)**(-periods))


def interes_total(amount,interest,cuotas):
    valor_cuota = monthly_quota(amount, interest, cuotas)
    total_intereses = (valor_cuota * cuotas) - amount
    return total_intereses


def amortizacion(amount, interest, periods):
    valor_cuota = monthly_quota(amount, interest, periods)
    print(valor_cuota)
    saldo = amount
    interes_total=interest/100
    tabla_amortizacion = []
    if periods == 1:
        numero_cuota = 1
        interes_total = 0
        abono_capital = (valor_cuota - interes_total, )
        fila = [numero_cuota, saldo, interes_total, abono_capital]
        tabla_amortizacion.append(fila)
    else:
        for cuota in range(1, periods + 1):
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


amount = float( input("Monto de la compra:") )
cuotas = int( input("Numero de cuotas en que va a diferir la compra:") )
interest = float( input("Tasa de interés de la tarjeta:") )
abono_extra = float(input("ingrese abono extra:"))
cuota_extra = int(input("ingrese cuota extra:"))
tabla= amortizacion(amount,interest,cuotas)
valor_cuota = monthly_quota(amount,interest,cuotas)

print(extra(tabla,cuota_extra,abono_extra, interest, valor_cuota))
