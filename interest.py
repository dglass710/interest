from commaNumber import commaNumber

def main(years, initialAmount, interest):
    'This is the conventional way to think of interest earned, in a recursive way'
    if years < 1:
        if initialAmount == int(initialAmount):
            initialAmount = int(initialAmount)
        return initialAmount
    return main(years - 1, (interest/100 + 1) * initialAmount, intrest)
def alsoWorks(years, initialAmount, interest):
    'Has identical I/O to main but with an iterative process and without the limitation of reaching maximum recursion depth'
    while years > 0:
        years -= 1
        initialAmount *= (1 + interest/100)
    if initialAmount == int(initialAmount):
        initialAmount = int(initialAmount)
    return initialAmount
def simpleVersion(years, initialAmount, interest):
    'Also has the same I/O as alsoWorks and main with an arithmatic expression and without computational intensity'
    return initialAmount*(1+interest/100)**years
def UI():
    'A very simple user interface for using this calculator on the command line'
    params = ('Number of Years:\t', 'Initial Amount:\t\t$', 'Interest (%):\t\t')
    usrInput = []
    b = ''
    for i in range(3):
        while True and b.lower() != 'exit':
            tmp = False
            try:
                usrInput.append(eval(input(params[i])))
                tmp = True
            except:
                print('Your input is non-numeric')
            if tmp:
                break
    print(f'Total:\t\t\t${commaNumber(((simpleVersion(usrInput[0], usrInput[1], usrInput[2])*100+.5)//1)/100)}')

UI()
