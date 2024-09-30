import numpy as np
import matplotlib.pyplot as plt
x_train = ([1.5, 2.5])  #Area 1000s sqft X-axis INDPND VAR
y_train = ([350.0, 550.0]) #Price $1000s Y-axis DPND VAR
#print(f"x_train: {x_train}")
#print(f"y_train: {y_train}")


def compute_model_output(NewX, NewW, NewB):
    m = len(NewX)
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = NewX[i]*NewW + NewB
    return f_wb 

def main():
    w = 200
    b = 50
    print(f"compute_model_output(x_train, w, b): {compute_model_output(x_train, w, b)}")
    tmp_f_wb = compute_model_output(x_train, w, b)
    plt.plot(x_train, tmp_f_wb, c='b', label='Predictions')
    plt.scatter(x_train, y_train, marker='X',c='r')
    plt.title("Housing Prices")
    plt.xlabel('Area (1000) sqft')
    plt.ylabel('Price $(1000)')
    plt.show()
    print("Enter Area of House to predict Price in thousands of Dollars")
    Area = int(input("Area: "))
    w = 200
    b = 50 
    price = w*Area + b
    print(f"price: {price}")







main()




