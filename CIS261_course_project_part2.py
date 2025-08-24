#Carl Shaffer CIS 261 Course Project part2 week 5
from datetime import datetime


def get_employee_name():
    while True:
        employee_name = input('Enter employee name: ')
        if employee_name.strip():
            return employee_name
        else:
            print('Employee name cannot be empty. Please enter a name. ')

def get_total_hours():
    while True:
        try:
           hours = float(input('Enter total hours worked: '))
           if hours >=0:
               return hours
           else:
               print('Hours cannot be negative. Please enter a valid number.')
        except ValueError:
            print('Invalid input. Please enter a numerical value.')

def get_hourly_rate():
    while True:
        try:
            rate = float(input('Enter hourly rate: '))
            if rate >= 0:
                return rate
            else:
                print('Hourly rate cannot be negative number. Please enter a valid number.')
        except ValueError:
            print('Invalid input')

def get_income_tax_rate():
    while True:
        try:
           tax_rate = float(input('Enter income tax rate(as a decimal): '))
           if 0 <= tax_rate <=1:
               return tax_rate
           else:
               print('Income tax rate must be between 0 and 1.')
        except ValueError:
           print('Invalid Input.')

def calculate_pay(total_hours, hourly_rate, tax_rate):
    gross_pay = total_hours * hourly_rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, net_pay, income_tax

def get_pay_period_dates():
    while True:
        from_date_str = input('Enter pay period "from" date (mm/dd/yyyy): ')
        to_date_str = input('Enter pay period "to" date (mm/dd/yyyy): ')
        try:
            from_date = datetime.strptime(from_date_str, "%m/%d/%Y")
            to_date = datetime.strptime(to_date_str, "%m/%d/%Y")
            if from_date <= to_date:
                return from_date_str, to_date_str
            else:
                print("The 'from' date cannot be after the 'to' date. Please try again.")
        except ValueError:
            print('Invalid date format. Please use mm/dd/yyyy.')
 
            
def process_and_display_employee_data(employee_list):
    totals = {
        'num_employees': 0,
        'total_hours_sum': 0.0,
        'total_gross_pay_sum': 0.0,
        'total_tax_sum': 0.0,
        'total_net_pay_sum': 0.0
    }
        
    print('\n--- Processing All Employee Records ---')
    for record in employee_list:
        from_date, to_date, employee_name, total_hours, hourly_rate, income_tax_rate = record

        gross_pay, net_pay, income_tax_amount = calculate_pay(total_hours, hourly_rate, income_tax_rate)

        display_employee_details(employee_name, total_hours, hourly_rate, gross_pay, income_tax_rate, income_tax_amount, net_pay)
    
        totals['num_employees'] += 1
        totals['total_hours_sum'] += total_hours
        totals['total_gross_pay_sum'] += gross_pay
        totals['total_tax_sum'] += income_tax_amount
        totals['total_net_pay_sum'] += net_pay
    
    return totals


def display_employee_details(name, hours, rate, gross, tax_rate, income_tax_amount, net):
    print('\n--- Employee PayRoll Details ---')
    print(f'Employee Name:{name}')
    print(f'Total Hours:{hours:.2f}')
    print(f'Hourly Rate:${rate:.2f}')
    print(f'Gross Pay:${gross:.2f}')
    print(f'Income Tax Rate:{tax_rate:.2%}')
    print(f'Income Tax Amount:${income_tax_amount:.2f}')
    print(f'Net Pay:${net:.2f}')
    print('----------------------------------------------------------')

def display_totals(num_employees, total_hours_sum, total_gross_pay_sum, total_tax_sum, total_net_pay_sum):
    print('\n--- Overall Company Payroll Summary ---')
    print(f'Total number of Employees Processed:{num_employees}')
    print(f'Total hours worked for all Employees:{total_hours_sum:.2f}')
    print(f'Total gross pay for all Employees:${total_gross_pay_sum:.2f}')
    print(f'Total Income Tax collected:${total_tax_sum:.2f}')
    print(f'Total net pay distributed:${total_net_pay_sum:.2f}')
    print('-----------------------------------------------------------')

def main():
    employee_records = []
     
    from_date, to_date = get_pay_period_dates()

    print('Welcome To The Payroll Calculator!')
    print('Type "end" for Employee name to terminate the program.')
   
    while True:
        employee_name = get_employee_name()
        if employee_name.lower() == 'end':
            break
                                         
        total_hours = get_total_hours()
        hourly_rate = get_hourly_rate()
        income_tax_rate = get_income_tax_rate()

        employee_records.append([from_date, to_date, employee_name, total_hours, hourly_rate, income_tax_rate])

        while True:
            add_another = input('\nAdd Another Employee?(y/n):').strip().lower()
            if add_another in ['y', 'n']:
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        if add_another == 'n':
            break

    if employee_records:
        payroll_totals = process_and_display_employee_data(employee_records)
        display_totals(
            payroll_totals['num_employees'],
            payroll_totals['total_hours_sum'],
            payroll_totals['total_gross_pay_sum'],
            payroll_totals['total_tax_sum'],
            payroll_totals['total_net_pay_sum']
        )
    else:
        print('No employee data was entered')
                

if __name__ == '__main__':
   main()