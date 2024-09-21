def calculate_finance(
        monthly_income: float,
        tax_rate: float, 
        currency: str,  
        food_expense: float, 
        health_insurance: float,
        monthly_rent: float,
        other_expenses: float) -> None:
    

    monthly_tax: float = monthly_income * (tax_rate / 100)
    monthly_net_income: float = monthly_income - monthly_tax - monthly_rent - food_expense - health_insurance - other_expenses
    yearly_salary: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_salary - yearly_tax

    print('-' * 20)
    print(f"Monthly Income : {currency}{monthly_income:,.3f}")
    print(f"Tax Rate : {tax_rate:,.2f}%")
    print(f"Monthly Tax : {currency}{monthly_tax:,.3f}")
    print(f"Monthly Net Income : {currency}{monthly_net_income:,.3f}")
    print(f"Yearly Salary : {currency}{yearly_salary:,.3f}")
    print(f"Yearly Tax Paid : {currency}{yearly_tax:,.3f}")
    print(f"Yearly Net Income : {currency}{yearly_net_income:,.3f}")
    print('-' * 20)
 
def main() -> None:
    try:
        monthly_income: float = float(input("Enter your monthly salary: "))
        tax_rate: float = float(input("Enter your tax rate (%): "))
        monthly_rent: float = float(input("Enter your monthly rent: "))
        food_expenses: float = float(input("Enter your food expenses: "))
        health_insurance: float = float(input("Enter your monthly health insurance contribution: "))
        other_expenses: float = float(input("Enter your other monthly expenses: "))
        calculate_finance(monthly_income, tax_rate, "$", monthly_rent, food_expenses, health_insurance, other_expenses)
    
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
