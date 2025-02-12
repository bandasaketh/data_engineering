annual_salary = int(input('Enter your annual salary:'))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal:'))
total_cost = int(input('Enter the cost of your dream home:'))
portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary= annual_salary/12
savings = monthly_salary * portion_saved
months= 0
down_payment= total_cost * portion_down_payment
while current_savings < down_payment :
    current_savings += current_savings * r/12
    current_savings += savings 
    months += 1
print('Number of months:', months)    


