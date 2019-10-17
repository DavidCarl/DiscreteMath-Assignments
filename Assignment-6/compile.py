import variable as var


variables = {}

def main():
    with open('test.vssl', 'r') as vsslCode:
        line = vsslCode.readline()
        cnt = 1
        while line:
            if(line[:3] == 'DEF'):
                try:
                    variable(line, cnt)                    
                except Exception as ex:
                    print(ex)
                    return
            elif(line[:5] == 'WHILE'):
                try:
                    loop(line, cnt)
                except Exception as ex:
                    print(ex)
                    return
            elif(line[:2] == 'if' or line[:4] == 'else'):
                try:
                    ifstatement(line, cnt)
                except Exception as ex:
                    print(ex)
                    return
            line = vsslCode.readline()
            cnt += 1
    pass

# This should work now!
# Or it kinda is missing variable value, not sure where to implement yet!
def variable(line, cnt):
    variableInfo = line[4:].split(':')
    varType = variableInfo[1].replace(' ','')
    varName = variableInfo[0]
    if ';' in varType:
        varType = varType.split(';')[0]
    else:
        raise Exception('Missing ; on line', cnt)
    if varType == 'INTEGER' or varType == 'BOOLEAN':
        if varType == 'INTEGER':
            testVar = var.INTEGER(varName, None)
            variables[varName] = testVar
        else:
            testVar = var.BOOLEAN(varName, None)
            variables[varName] = testVar
    else:
        raise Exception('Unknown variable type', varType, 'on line', cnt)

def loop(line, cnt):
    print('This is a loop!')
    pass

def ifstatement(line, cnt):
    print('this is a if statement!')
    pass


if __name__ == "__main__":
    main()