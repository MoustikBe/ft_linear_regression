import matplotlib.pyplot as plt
import re

def main():
    print("Init")
    f = open("data.csv")
    content = f.read()
    print(content)
    newcontent = content.split('\n')
    print("\n", newcontent)

    y = []
    x = []
    for i in range(len(newcontent)):
       if(i > 0):
            NewStr = newcontent[i][:newcontent[i].find(',')]
            NewStr2 = newcontent[i][newcontent[i].find(',') + 1:]
            x.append(NewStr)
            y.append(NewStr2)


    plt.xlabel("Milage")
    plt.ylabel("Price")
    plt.axis([0, 20, 0, 20])
    plt.scatter(x, y, color='blue', s=50, marker='o')
    plt.show()
    plt.close()

if (__name__ == "__main__"):
    main()