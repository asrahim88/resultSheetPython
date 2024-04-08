email = input("Enter your email for validation: ")
i,k, d = 0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if "@" in email and email.count("@") == 1 and "." in email and email.count(".") == 1:
            if (email[-3]==".") or (email[-4] == "."):
                for i in email:
                    if i.isspace():
                        j = 1
                    elif i.isalpha():
                        if i == i.upper():
                            k = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i== "@":
                        continue
                    else:
                        d= 1
                if i == 1 or k == 1 or d == 1:
                    print("Invalid Email-5")
                else:
                    print("Valid Email")
            else:
                print("Invalid Email-4")
        else:
            print("Invalid Email-3")
    else:
        print("Invalid Email-2")
else:
    print("Invalid Email-1")