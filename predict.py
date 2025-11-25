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

    x_min, x_max = 0, 20000
    y_min, y_max = 0, 20000
    plt.figure(figsize=(8, 6))
    plt.xlabel("Milage")
    plt.ylabel("Price")
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(range(x_min, x_max + 1, 2000))
    plt.yticks(range(y_min, y_max + 1, 2000))
    plt.scatter(x, y, s=30)
    plt.show()
    plt.close()

if (__name__ == "__main__"):
    main()