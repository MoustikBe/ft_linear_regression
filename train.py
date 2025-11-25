import matplotlib.pyplot as plt
import json
import re
import random 
import numpy as np

w_real, b_real = 0, 0
y, x, losses = [], [], []

def init_var():
    ############### Collecting data from dataset ###############
    global x, y
    with open("data.csv") as f:
        newcontent = f.read().strip().split('\n')
    
    for line in newcontent[1:]:
        k, p = line.split(',')
        x.append(int(k))
        y.append(int(p))
        print(line)
    ############### Collecting data from dataset ###############

def train_model():
    global losses, w_real, b_real

    ############### Variable declaration ###############
    # -- Normlisation of the data to avoid UDGE numbers -- # 
    x_min, x_max = min(x), max(x)
    y_min, y_max = min(y), max(y)
    x_norm = [(xi - x_min) / (x_max - x_min) for xi in x]
    y_norm = [(yi - y_min) / (y_max - y_min) for yi in y]
    # ------------------------------------------------------#
    m = len(x)
    w = 0
    b = 0
    lr = 0.1    
    best_loss = float('inf')
    patience_count = 0
    delta = 0.0001
    ############### Variable declaration ###############
    ############### Training the model ###############
    iteration = 3000
    for epoch in range(iteration):
        dw = 0
        db = 0
        loss = 0

        for i in range(m):
            y_i = w*x_norm[i]+b
            dw = dw + (y_i - y_norm[i]) * x_norm[i]
            db = db + (y_i - y_norm[i])
            loss = loss + (y_i - y_norm[i]) ** 2
        
        dw = 2*dw/m
        db = 2*db/m
        loss = loss/m 

        # -- Early stoping implementation to avoid overfeeding -- #  
        if(best_loss - loss > delta):
            best_loss = loss
            patience_count = 0
        else:
            patience_count += 1
        if(patience_count >= 25):
            print("Breaking to avoid overfeeding at ", epoch, " iteration")
            break
        # -- Early stoping implementation to avoid overfeeding -- # 

        losses.append(loss)
        w = w - lr*dw
        b = b - lr*db
    ############### Training the model ###############

    # -- Re adapting the data for the true value -- #
    w_real = w * (y_max - y_min) / (x_max - x_min)
    b_real = b * (y_max - y_min) + y_min - w_real * x_min

    # -- Writing in the json the thetas value -- # 
    data = {"theta0" : b_real, "theta1" : w_real}
    with open(".prog_data.json", "w") as f:
        json.dump(data, f)

def display():
    # -- Display -- #
    # Error line #
    plt.plot(losses)
    plt.figure(figsize=(12, 8))
    plt.scatter(x, y, s=40)
    plt.title("Real_Value") 
    plt.xlabel("Milage")
    plt.ylabel("Price")
    plt.tight_layout()
    # Data line #
    X = np.linspace(min(x), max(x), 100)
    Y = w_real*X+b_real
    plt.plot(X, Y, color="red")
    plt.show()
    plt.close()
    # -- Display -- #

def main():
    init_var()    
    train_model()
    display()

if (__name__ == "__main__"):
    main()