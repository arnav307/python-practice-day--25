def determine(ss_num):
    for digit in ss_num:
        if digit.isdigit():
            print(f"Yes it contain digit {digit}")
            return 
    print("No it does not contain")
determine('que0')
