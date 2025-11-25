import sys


def main():
    if (len(sys.argv) > 3):
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = sys.argv[3]
        if(c == "-"):
            print(a - b)
        elif(c == "+"):
            print(a + b)
        elif(c == '*'):
            print(a * b)
        elif(c == "/"):
            print(a / b)
        print("P'tite calculette oslm")  

#    x = 15
#    i = 0
#
#    def alternative_fun():
#        print(i)
#        i = 25
#
#    while i < x:
#        i += 1
#        if i == 12:
#            alternative_fun()
#    print(i)


if __name__ == "__main__":
    main()
