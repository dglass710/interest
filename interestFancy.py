from commaNumber import commaNumber
cn = commaNumber

def interest(initial, rate, years, contribution, contInc):
    if years == 0:
        return initial + contribution
    return (1 + rate/100) * interest(initial, rate, years - 1, contribution, contInc) + (contribution * (1 + contInc/100.0)**years)
def removeCommas(myStr):
    retStr = ''
    for char in myStr:
        if char != ',':
            retStr += char
    return retStr
def printSavings(age, rate, iAmnt, endAge, contribution = 0, contInc = 0, div = 0):
    for year in range(endAge - age + 1):
        amnt = int(interest(iAmnt, rate, year, contribution, contInc))
        wDiv = int(interest(iAmnt, rate + div, year, contribution, contInc))
        print('{} years old: \n\ndivs removed:\ntotal: ${}\ndividend: ${}\n\ndivs reinvested:\ntotal: ${}\ndividend: ${}\n\n*************\n'.format(year + age, cn(amnt), cn(int(amnt * .02)), cn(wDiv), cn(int(wDiv * .02))))
def UI():
    'A very simple user interface for using this calculator on the command line'
    params = ('Current Age:\t\t\t', 'Initial Amount:\t\t\t$', 'Interest (%):\t\t\t', 'Expected Dividends (%):\t\t','Final Age:\t\t\t', 'Initial Contribution ($):\t', 'Increase In Contribution (%):\t')
    usrInput = []
    tmpUsrInput = ''
    for i in range(7):
        while True and tmpUsrInput.lower() != 'exit':
            tmp = False
            tmpUsrInput = input(params[i])
            try:
                usrInput.append(eval(removeCommas(tmpUsrInput)))
                tmp = True
            except:
                print('Your input is non-numeric')
            if tmp:
                break
    if tmpUsrInput.lower() != 'exit':
        printSavings(usrInput[0], usrInput[2], usrInput[1], usrInput[4], usrInput[5], usrInput[6], usrInput[3])

UI()


