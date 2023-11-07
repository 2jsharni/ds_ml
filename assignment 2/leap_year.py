yr =  int(input("Enter yr : "))

if yr % 400 == 0 or yr % 4 == 0:
    print("{} is leap yr".format(yr))
elif yr % 100 == 0:
    print("{} is not leap yr".format(yr))
else:
     print("{} is not leap yr".format(yr))