from state import State


state = State()

def log_in(instance):
    try:
        state.change_state(instance,1)
        print(f'{instance} logging in')
    except Exception as ex:
        print(ex)

def list_items(instance):
    try:
        state.change_state(instance,2)
        print(f'{instance} list items')
    except Exception as ex:
        print(ex)
        
def edit_items(instance):
    try:
        state.change_state(instance,3)
        print(f'{instance} edit items')
    except Exception as ex:
        print(ex)

def log_out(instance):
    try:
        state.change_state(instance,4)
        print(f'{instance} log out')
    except Exception as ex:
        print(ex)

methods = {
    1: log_in,
    2: list_items,
    3: edit_items,
    4: log_out
}

def main():
    with open('test.log', 'r') as log:
        for line in log:
            l = line.split(':')
            func = methods[int(l[3])]
            func(int(l[2]))

if __name__ == "__main__":
    main()