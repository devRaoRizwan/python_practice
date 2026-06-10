# Calculate income tax for a given income based on these rules:
# First $10,000: 0% tax
# Next $10,000: 10% tax
# Remaining income: 20% tax
# Given Input: income = 45000
# Expected Output: Total income tax to pay is 6000


def income_tax_calculator(salary):
    tax_amount = 0
    if salary <= 10000 :
        return tax_amount
    elif salary <= 20000:
        tax_amount = (salary - 10000) * 0.10
         
    else :
        tax_amount = 0 + (10000 * 0.10)
        tax_amount += (salary - 20000) * 0.20
    return tax_amount
        

if __name__ == "__main__" :
    income = 45000
    print(f"Total income tax to pay is {income_tax_calculator(income)}")
    
        
        
        
        