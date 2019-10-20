import re
from queue import Queue


p = [] # Preconditions
q = [] # Postconditions
variables = {}
domains  = {}

def pre_post_conditions():
    '''
    Load the precondition and postconditions for a conditions.txt file
    '''
    with open('conditions.txt', 'r') as f:
        lines = [line.strip() for line in f]
        for line in lines:
            print(line)
            statements = line.split('[', 1)[1].split(']')[0].split(',')
            if line.upper().startswith('P'):
                insert_statements_in_conditions(p, statements)
            elif line.upper().startswith('Q'):
                insert_statements_in_conditions(q, statements)

def insert_statements_in_conditions(condition, statements):
    for statement in statements:
        statement = statement.replace(' ', '') # clean statements for spaces
        statement = statement.split('∈') # split name and value
        condition.append(statement[0])

def load_vssl():
    '''
    Loads all the commands from vssl.txt and returns a queue of the commands 
    '''
    with open('VSSL.txt', 'r') as f:
        lines = [line.strip() for line in f]
        commands = Queue(len(lines)) 
        for line in lines:
            commands.put(line)
        return commands

def define_var(command):
    tmp = command.split(' ',1)[1].split(': ',1)
    variables[tmp[0]] = {'type': tmp[1]}


block_count = 0
def if_block(command):
    global block_count
    block_count += 1
    command = command.replace(' ','')
    command = command[1:-1]
    if '==' in command:
        command = command.split('==',1)
    
    elif '<=' in command:
        command = command.split('<=',1)
    
    elif '>=' in command:
        command = command.split('>=',1)
    
    elif '<' in command:
        command = command.split('<',1)
    
    elif '>' in command:
        command = command.split('>',1)
    
    print(command)
    # print('block entered')


def end_block(command):
    global block_count
    block_count -= 1
    # print('block exited')


switcher = {
    "DEF": define_var,
    "IF": if_block,
    "}": end_block
}

def run_commands(commands):
    while not commands.empty():
        command = commands.get()
        tp = command.split(' ',1)[0]
        func = switcher.get(tp)
        if func: 
            func(command)
        print(f'{command:20}', get_s({'Y':\
                                        {'type':'INTEGER',\
                                         'lower': 4,
                                         'upper': 9
                                        },
                                        'X':{'value':100}
                                    }))




def get_p(domain):
    tmp = ''
    for i, p_val in enumerate(p):
        tmp = tmp + p_val + ' ∈ {'
        if p_val in domain:
            if 'value' in domain[p_val]:
                tmp = tmp + str(domain[p_val]['value']) + '}'
            else:
                tmp = tmp \
                    + str(domain[p_val].get('lower', '')) \
                    + '...' \
                    + str(domain[p_val].get('upper','')) \
                    + '}'
        if i + 1 is not len(p):
            tmp = tmp + ','
    return tmp

def get_q(domain):
    tmp = ''
    for i, q_val in enumerate(q):
        tmp = tmp + q_val + ' ∈ {'
        if q_val not in domain:
            tmp = tmp + '?}'
        else:
            if 'value' in domain[q_val]:
                tmp = tmp + str(domain[q_val]['value']) + '}'
            else:
                tmp = tmp \
                    + str(domain[q_val].get('lower', '')) \
                    + '...' \
                    + str(domain[q_val].get('upper','')) \
                    + '}'
        if i + 1 is not len(p):
            tmp = tmp + ','
    return tmp

def get_s(domain):
    s = 's = '
    s = s + '[' + get_p(domain) + ', '
    s = s + get_q(domain) + ']'
    return s
    return ''

def main():
    pre_post_conditions() 
    commands = load_vssl()
    run_commands(commands)

if __name__ == "__main__":
    main()