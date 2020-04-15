
#Student name: Alisha Augustin
#Lab section: ENGR 132-002

import matplotlib.pyplot as plt
import math
import numpy as np

    
if __name__ == "__main__":
    v1 = (0,0)
    v2 = (0.5, math.sin (math.radians (60)))
    v3 = (1,0)
   
    x_b = 0 
    y_b = 0                                     
    a = 1                                       
    x_a = x_b + a/2                             
    y_a = y_b + a * math.sin (math.radians (60)) 
    x_c = x_b + a                               
    y_c = y_b
    

    plt.plot ([x_a, x_b, x_c, x_a], [y_a, y_b, y_c, y_a], 'b-') 
    plt.axis ([-0.1, 1.1, -0.1, 1.1]) 
    
    plt.text (x_b, y_b - 0.05, "B")              
    plt.text (x_a, y_a + 0.05, "A")             
    plt.text (x_c, y_c - 0.05, "C")              
    plt.title ("Sierpinski Triangle")
    
    w = np.random.rand (1, 3)
    x_o = (w[0][0]*x_a + w[0][1]*x_b + w[0][2]*x_c)/sum(w[0])
    y_o = (w[0][0]*y_a + w[0][1]*y_b + w[0][2]*y_c)/sum(w[0])
    plt.plot(x_o, y_o, "r.");
   
    max_iter = 10000
    num_iter = 0
    while (num_iter < max_iter):
        dice_val = np.random.randint(6)
        if dice_val == 1 or dice_val == 2:
            x_o = (x_a + x_o)/2
            y_o = (y_a + y_o)/2
            plt.plot(x_o, y_o, "r.");
        elif dice_val == 3 or dice_val == 4:
            x_o =(x_b + x_o)/2
            y_o = (y_b + y_o)/2
            plt.plot(x_o, y_o, "r.");
        elif dice_val == 5 or dice_val == 6:
            x_o =(x_c + x_o)/2
            y_o = (y_c + y_o)/2
            plt.plot(x_o, y_o, "r.");
        num_iter = num_iter + 1 
        
    plt.savefig("sierpinski_triangle.pdf")
    plt.show()
    