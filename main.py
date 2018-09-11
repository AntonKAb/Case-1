previous_tax = float(input())  # Фактическая сумма платежа за последний квартал предыдущего года.

profitI = float(input())  # Прибыль за I квартал.
deductionsI = float(input())  # Вычеты за I квартал.

profitII = float(input())  # Прибыль за II квартал.
deductionsII = float(input())  # Вычеты за II квартал.

profitIII = float(input())  # Прибыль за III квартал.
deductionsIII = float(input())  # Вычеты за III квартал.

profitIV = float(input())  # Прибыль за IV квартал.
deductionsIV = float(input())  # Вычеты за IV квартал.

advance_sumI = float(previous_tax / 3)  # Сумма авансовых платежей за I квартал. (руб/месяц)
actual_taxI = float((profitI - deductionsI) * 0.2)  # Фактическая сумма налога за I квартал. (Полная)

print('Сумма авансовых платежей за январь, февраль и март составила',advance_sumI,'рублей в месяц.')
print('Фактический налог за первый квартал составил',actual_taxI,'рублей.')
if actual_taxI > previous_tax:
    print("До 28 апреля необходимо доплатить", actual_taxI - previous_tax, "руб. за I квартал. ")
elif actual_taxI < previous_tax:
    print("Переплата за I квартал составила:", previous_tax - actual_taxI, "руб.")
else:
    print("Задолженности по налогу за I квартал нет.")


advance_sumII = float(actual_taxI / 3)  # Сумма авансовых платежей за II квартал.
actual_taxII = float((profitII - deductionsII) * 0.2)  # Фактическая сумма налога за II квартал.

print('Сумма авансовых платежей за апрель, май и июнь составила',advance_sumII,'рублей в месяц.')
print('Фактический налог за второй квартал составил',actual_taxII,'рублей.')
if actual_taxII > actual_taxI:
    print("До 28 июля необходимо доплатить", actual_taxII - actual_taxI, "руб. за II квартал. ")
elif actual_taxII < actual_taxI:
    print("Переплата за II квартал составила:", actual_taxI - actual_taxII, "руб.")
else:
    print("Задолженности по налогу за II квартал нет.")


advance_sumIII = float(actual_taxII / 3)  # Сумма авансовых платежей за III квартал.
actual_taxIII = float((profitIII - deductionsIII) * 0.2)  # Фактическая сумма налога за III квартал.

print('Сумма авансовых платежей за июль, август и сентябрь составила',advance_sumIII,'рублей в месяц.')
print('Фактический налог за третий квартал составил',actual_taxIII,'рублей.')
if actual_taxIII > actual_taxII:
    print("До 28 октября необходимо доплатить", actual_taxIII - actual_taxII, "руб. за III квартал. ")
elif actual_taxIII < actual_taxII:
    print("Переплата за III квартал составила:", actual_taxII - actual_taxIII, "руб.")
else:
    print("Задолженности по налогу за III квартал нет.")


advance_sumIV = float(actual_taxIII / 3)  # Сумма авансовых платежей за IV квартал.
actual_taxIV = float((profitIV - deductionsIV) * 0.2)  # Фактическая сумма налога за IV квартал.

print('Сумма авансовых платежей за октябрь, ноябрь и декабрь составила',advance_sumIV,'рублей в месяц.')
print('Фактический налог за четвертый квартал составил',actual_taxIV,'рублей.')
if actual_taxIV > actual_taxIII:
    print("До 28 января необходимо доплатить", actual_taxIV - actual_taxIII, "руб. за IV квартал. ")
elif actual_taxIV < actual_taxIII:
    print("Переплата за IV квартал составила:", actual_taxIII - actual_taxIV, "руб.")
else:
    print("Задолженности по налогу за IV квартал нет.")
