import variable as var


variables = {}
statementTrue = False

def main():
    inIfStatement = False
    inWhileLoop = False
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
            elif(line[:5] == 'WHILE' or inWhileLoop):
                if line[:5] == 'WHILE':
                    inWhileLoop = True
                elif '}' in line:
                    inWhileLoop = False
                try:
                    loop(line, cnt)
                except Exception as ex:
                    print(ex)
                    return
            elif(line[:2] == 'if' or line[:4] == 'else' or inIfStatement):
                if line[:2] == 'if' or line[:4] == 'else':
                    inIfStatement = True
                elif '}' in line:
                    # print('Ending if statement!')
                    inIfStatement = False
                    statementTrue = False
                elif line.strip().split(':')[0] in variables:
                    try:
                        setVariable(line, cnt)
                    except Exception as ex:
                        print(ex)
                try:
                    ifstatement(line, cnt)
                except Exception as ex:
                    print(ex)
                    return
            elif line.strip().split(':')[0] in variables:
                try:
                    setVariable(line, cnt)
                except Exception as ex:
                    print(ex)
            # print(line.strip().split(':')[0], len(line.strip().split(':')[0]))
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
            testVar = var.BOOLEAN(varName, True)
            variables[varName] = testVar
    else:
        raise Exception('Unknown variable type', varType, 'on line', cnt)

def setVariable(line, cnt):
    res = line.strip().split(':')[1].strip().split(';')[0]
    if variables[line.strip().split(':')[0]].getType() == 'BOOLEAN':
        if res == 'TRUE':
            variables[line.strip().split(':')[0]].setValue(True)
        elif res == 'FALSE':
            variables[line.strip().split(':')[0]].setValue(False)
        print(variables[line.strip().split(':')[0]].getValue())
    elif variables[line.strip().split(':')[0]].getType() == 'INTEGER':
         variables[line.strip().split(':')[0]].setValue(int(res))

        

def loop(line, cnt):
    print('This is a loop!')
    pass

def ifstatement(line, cnt):
    if 'if(' in line or 'if (' in line:
        statement = line.split('(')[1].split(')')[0]
        if '>' in statement:
            pass
        elif '<' in statement:
            pass
        elif ' ' not in statement:
            if variables[statement].getValue():
                statementTrue = True
                # print('TRUE')
            else:
                print('FALSE')
        else:
            raise Exception('Unknown if statement', statement)
    pass


if __name__ == "__main__":
    main()