# Tax Withheld Calculator

# Write a console program that calculates the total amount of tax withheld from an employee’s weekly salary.
# The total withheld tax amount is calculated by combining the amount of provincial tax withheld and the amount of 
# federal tax withheld, minus a per-dependent deduction from the total tax withheld. The user will enter their pre-tax 
# weekly salary amount and the number of dependents they wish to claim. 
# 
# The program will calculate and output the amount of provincial tax withheld, amount of federal tax withheld, the 
# dependent tax deduction, and the user’s final take-home amount.
# Provincial withholding tax is calculated at 6.0%. Federal withholding tax is calculated at 25.0%. 
# The tax deduction for dependents is calculated at 2.0% of the employee’s salary per dependent.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    PROVINCIAL_TAX_RATE = 0.06
    FEDERAL_TAX_RATE = 0.25
    DEPEDENTS_RATE = 0.02

    preTaxSalary = 0.0
    dependents = 0
    provincialTaxWithheld = 0.0
    federalTaxWithheld = 0.0
    dependentDeduction = 0.0
    totalWitheld = 0.0
    takeHomePay = 0.0

    print("Tax Withholding Calculator\n")

    preTaxSalary = float(input("Please enter the full amount of your weekly salary: "))
    dependents = int(input("How many dependents do you have?: "))
    print("")
    provincialTaxWithheld = PROVINCIAL_TAX_RATE * preTaxSalary
    federalTaxWithheld = FEDERAL_TAX_RATE * preTaxSalary
    dependentDeduction = (DEPEDENTS_RATE * preTaxSalary) * dependents
    totalWitheld = (provincialTaxWithheld + federalTaxWithheld) - dependentDeduction
    takeHomePay = preTaxSalary - totalWitheld

    print(f"Provincial Tax Withheld: ${provincialTaxWithheld:.2f}")
    print(f"Federal Tax Withheld: ${federalTaxWithheld}")
    print(f"Dependent Deduction for {dependents} dependants: ${dependentDeduction:.2f}")
    print(f"Total Withheld: ${totalWitheld:.2f}")
    print(f"Total Take-Home Pay: ${takeHomePay:.2f}")




    # YOUR CODE ENDS HERE

main()
