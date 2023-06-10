user_wage = 20
user_over = 30
hours = int(input())
if hours <= 40:
    total = (hours * user_wage)
else:
    over_t = (hours % 40)
    reg_t=(hours-over_t)
    total=(reg_t*20) + (over_t*30)

print(total)