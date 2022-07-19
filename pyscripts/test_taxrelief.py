genderbonus = {0, 500}
age = 0
variable = 0
salary = 0
taxpaid = 0

if age >= 18:
    variable == 1

elif age >= 35:
    variable == 0.8

elif age >= 50:
    variable == 0.5

elif age >= 75:
    variable == 0.367

elif age >= 76:
    variable == 0.05

taxrelief = ((salary - taxpaid) * variable +genderbonus)

#comparing of expected taxrelief to taxrelief shown in UI
