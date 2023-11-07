
prctg = float(input(" percentage: "))

if prctg >= 90 and prctg <= 100:
    print("grade is A+")

elif prctg >= 80 and prctg < 90:
    print("grade is A")

elif prctg >= 70 and prctg < 80:
    print("grade is B")

elif prctg >= 60 and prctg < 70:
    print("grade is C")

elif prctg >= 50 and prctg < 60:
   print("grade is D")

elif prctg >= 0 and prctg < 50:
    print("grade is F, you are fail")
else:
    print("prctg should be between 0 to 100")