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


def total_interest(amount,interest,periods):
    quota_value = monthly_quota(amount, interest, periods)
    total_interest = (quota_value * periods) - amount
    return total_interest


def amortizacion(amount, interest, periods):
    quota_value = monthly_quota(amount, interest, periods)
    print(quota_value)
    balance = amount
    total_interest=interest/100
    total_amortization = []
    if periods == 1:
        quota_number = 1
        total_interest = 0
        capital_credit = (quota_value - total_interest, )
        row = [quota_number, balance, total_interest, capital_credit]
        total_amortization.append(row)
    else:
        for periods in range(1, periods + 1):
            quota_number = periods
            interest = (total_interest * balance)
            capital_credit = round(quota_value - interest)
            balance = (balance - capital_credit)

            row = [quota_number, balance, interest, capital_credit]
            total_amortization.append(row)
            print(row)

    return total_amortization

def extra(total_amortization, periods, fertilizer, interest, quota_value):
    subtracting_balance = total_amortization[periods-2][1]
    interest_percentage = interest / 100
    bonus_amortization_table_extra_bonus = []
    for j in range (total_amortization[periods-1][0], 36):
        quota_number = j
        interest: float = round(interest_percentage * subtracting_balance, 2)
        if quota_number == total_amortization[periods-1][0]:
            capital_credit: float = round(fertilizer - interest, 2)
        else:
            capital_credit: float = round(quota_value - interest, 2)
        subtracting_balance: float = round(subtracting_balance - capital_credit, 2)
        if subtracting_balance <= 0:
            subtracting_balance = 0
        row = [quota_number, subtracting_balance, interest, capital_credit]
        bonus_amortization_table_extra_bonus.append(row)
        if subtracting_balance <= 0:
            break
    return bonus_amortization_table_extra_bonus


amount = float( input("Monto de la compra:") )
periods = int( input("Numero de cuotas en que va a diferir la compra:") )
interest = float( input("Tasa de interés de la tarjeta:") )
extra_mulch = float(input("ingrese abono extra:"))
extra_quota = int(input("ingrese cuota extra:"))
table= amortization(amount,interest,periods)
quota_value = monthly_quota(amount,interest,periods)

print(extra(table,extra_quota,extra_mulch, interest, quota_value))
