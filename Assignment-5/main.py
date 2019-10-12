import setHandler


handler = setHandler.setHandler()

def main():
    print(handler.membership(3, set([1,2,3,4,5])))
    print(handler.intersection(set([1,2,3]), set([2,3,4])))

if __name__ == "__main__":
    main()