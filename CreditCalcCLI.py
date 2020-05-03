import argparse
import math

ap = argparse.ArgumentParser()
ap.add_argument('--type', help='Enter annuity or diff')
ap.add_argument('--payment', type=float)
ap.add_argument('--principal', type=int)
ap.add_argument('--periods', type=int)
ap.add_argument('--interest', type=float)
args = vars(ap.parse_args())
payments, principal, periods, interest = 0, 0, 0, 0
incorrect_parameter = 0
count = 0


def invalid_input():
    global incorrect_parameter
    count_none = 0
    for key, value in args.items():
        if value is None:
            count_none += 1
    if args.get('type') != 'diff' and args.get('type') != 'annuity':
        print('Incorrect parameters')
        incorrect_parameter += 1
    elif 'diff' in args.values() and args.get('payment') is not None:
        print('Incorrect parameters')
        incorrect_parameter += 1
    elif interest in args.values() == 'None':
        print('Incorrect parameters')
        incorrect_parameter += 1
    elif count_none >= 2:
        print('Incorrect parameters')
        incorrect_parameter += 1
    elif '-' in str(args.values()):
        print('Incorrect parameters')
        incorrect_parameter += 1


def cli_mapping():
    global payments, principal, periods, interest
    for key, value in args.items():
        if key == 'payment':
            payments = args[key]
        if key == 'principal':
            principal = args[key]
        if key == 'periods':
            periods = args[key]
        if key == 'interest':
            interest = args[key]


def diff():
    global payments, principal, periods, interest
    if incorrect_parameter == 0:
        all_payments = []
        current_period = 0
        for _ in range(periods):
            nom_interest = (interest / 100) / (12 * 1)
            current_period += 1
            differentiated_payment = math.ceil((principal / periods + nom_interest *
                                                (principal - ((principal * (current_period - 1)) / periods))))
            print(f'Month {current_period}: paid out {differentiated_payment}')
            all_payments.append(differentiated_payment)
        overpayment = sum(all_payments) - principal
        print('\nOverpayment =', overpayment)


def annuity():
    if incorrect_parameter == 0:
        global payments, principal, periods, interest
        nom_interest = (interest / 100) / (12 * 1)
        if args.get('principal') is not None and args.get('payment') is not None:
            periods = math.ceil(math.log((payments / (payments - nom_interest * principal)), 1 +
                                         nom_interest))
            years = periods // 12
            months = periods % 12
            if years == 0 and months == 1:
                print('You need', months, 'month to repay this credit!')
            elif years == 0 and months > 1:
                print('You need', months, 'months to repay this credit!')
            elif years == 1 and months == 0:
                print('You need', years, 'year to repay this credit!')
            elif years > 1 and months == 0:
                print('You need', years, 'years to repay this credit!')
            elif years > 1 and months == 1:
                print('You need', years, 'years and', months, 'month to repay this credit!')
            else:
                print('You need', years, 'years and', months, 'months to repay this credit!')
            print('\nOverpayment =', (payments * periods) - principal)
        elif args.get('principal') is not None and args.get('periods') is not None:
            annuity_ = math.ceil(principal * ((nom_interest * (1 + nom_interest) ** periods) /
                                                    ((1 + nom_interest) ** periods - 1)))
            print(f'Your annuity payment = {annuity_}!')
            print('\nOverpayment =', (annuity_ * periods) - principal)
        elif args.get('periods') is not None and args.get('payment') is not None:
            principal = math.floor(payments / ((nom_interest * (1 + nom_interest) ** periods) /
                                                              ((1 + nom_interest) ** periods - 1)))
            print(f'Your credit principal = {principal}!')
            print('\nOverpayment =', (payments * periods) - principal)


while count == 0:
    cli_mapping()
    if invalid_input():
        count += 1
        break
    else:
        if 'diff' in args.values():
            diff()
        elif 'annuity' in args.values():
            annuity()
        count += 1
