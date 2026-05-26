ex = input("Expression: ").strip()

x,y,z = ex.split()

display_sum = round (int(x) + int(z), 1)
display_sub = round (int(x) - int(z), 1)
display_mul = round (int(x) * int(z), 1)
display_div = round (int(x) / int(z), 1)

if y == "+":
    print (f"{display_sum:.1f}")
elif y == "-":
    print (f"{display_sub:.1f}")
elif y == "*":
    print (f"{display_mul:.1f}")
else:
    print (f"{display_div:.1f}")
