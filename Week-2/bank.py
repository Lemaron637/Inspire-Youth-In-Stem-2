goss_income = int(input("what is your goss income "))
tax_group_a = (goss_income * 0.05)
tax_group_b = (goss_income * 0.16)
tax_group_c = (goss_income * 0.19)
tax_group_d = (goss_income * 0.30)

if goss_income <= 100000:
    print("Goss income:", goss_income)
    print("Net income:", goss_income - tax_group_a)

if goss_income >= 100001:
    print("Goss_income:", goss_income)
    print("Net income:", goss_income - tax_group_b)


if (goss_income >=150001) &(goss_income<=300000):
    print("Goss income:",goss_income)
    print("Net income:", goss_income - tax_group_c)
     
elif (goss_income >=300001) &(goss_income<=500000):
    print("Goss income:",goss_income)
    print("Net income:", goss_income - tax_group_d)




