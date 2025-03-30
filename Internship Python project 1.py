import argparse
import math

def mortgage_calculator(principal, annual_rate, years):
    monthly_rate = annual_rate / 100 / 12
    total_payments = years * 12
    
    if monthly_rate == 0:
        monthly_payment = principal / total_payments
    else:
        monthly_payment = principal * (monthly_rate * (1 + monthly_rate)**total_payments) / ((1 + monthly_rate)**total_payments - 1)
    
    total_payment = monthly_payment * total_payments
    
    print(f"Monthly Payment: ${monthly_payment:,.2f}")
    print(f"Total Payment: ${total_payment:,.2f}")

def investment_calculator(initial, annual_rate, years):
    rate = annual_rate / 100
    future_value = initial * (1 + rate)**years
    
    print(f"Future Value: ${future_value:,.2f}")
    print(f"Total Profit: ${future_value - initial:,.2f}")

def savings_goal_calculator(goal, years, annual_rate):
    months = years * 12
    monthly_rate = annual_rate / 100 / 12
    
    if monthly_rate == 0:
        monthly_savings = goal / months
    else:
        monthly_savings = goal * monthly_rate / ((1 + monthly_rate)**months - 1)
    
    total_contributions = monthly_savings * months
    
    print(f"Required Monthly Savings: ${monthly_savings:,.2f}")
    print(f"Total Contributions: ${total_contributions:,.2f}")

def income_tax_calculator(income, deductions):
    tax_brackets = [
        (9950, 0.10),
        (40525, 0.12),
        (86375, 0.22),
        (164925, 0.24),
        (209425, 0.32),
        (523600, 0.35),
        (float('inf'), 0.37)
    ]
    
    taxable_income = max(0, income - deductions)
    tax = 0
    previous_bracket = 0
    
    for bracket, rate in tax_brackets:
        if taxable_income > previous_bracket:
            taxable_in_bracket = min(taxable_income, bracket) - previous_bracket
            tax += taxable_in_bracket * rate
            previous_bracket = bracket
        else:
            break
    
    print(f"Taxable Income: ${taxable_income:,.2f}")
    print(f"Estimated Tax Liability: ${tax:,.2f}")

def main():
    parser = argparse.ArgumentParser(description="Financial Planning CLI Tool")
    subparsers = parser.add_subparsers(dest="command")
    
    mortgage_parser = subparsers.add_parser("mortgage", help="Calculate mortgage payments")
    mortgage_parser.add_argument("principal", type=float, help="Loan amount in dollars")
    mortgage_parser.add_argument("annual_rate", type=float, help="Annual interest rate in percent")
    mortgage_parser.add_argument("years", type=int, help="Loan term in years")
    
    investment_parser = subparsers.add_parser("investment", help="Calculate future investment value")
    investment_parser.add_argument("initial", type=float, help="Initial investment amount in dollars")
    investment_parser.add_argument("annual_rate", type=float, help="Expected annual return in percent")
    investment_parser.add_argument("years", type=float, help="Investment time horizon in years")
    
    savings_parser = subparsers.add_parser("savings", help="Calculate monthly savings to reach a goal")
    savings_parser.add_argument("goal", type=float, help="Savings goal in dollars")
    savings_parser.add_argument("years", type=float, help="Time frame in years")
    savings_parser.add_argument("annual_rate", type=float, help="Expected annual return in percent")
    
    tax_parser = subparsers.add_parser("tax", help="Calculate estimated tax liability")
    tax_parser.add_argument("income", type=float, help="Annual income in dollars")
    tax_parser.add_argument("deductions", type=float, help="Total deductions in dollars")
    
    args = parser.parse_args()
    
    if args.command == "mortgage":
        mortgage_calculator(args.principal, args.annual_rate, args.years)
    elif args.command == "investment":
        investment_calculator(args.initial, args.annual_rate, args.years)
    elif args.command == "savings":
        savings_goal_calculator(args.goal, args.years, args.annual_rate)
    elif args.command == "tax":
        income_tax_calculator(args.income, args.deductions)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

