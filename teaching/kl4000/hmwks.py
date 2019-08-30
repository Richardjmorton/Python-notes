import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')

path='/Users/richardmorton/Desktop/teaching/KL4000/assessment/19_20/'

def hmwk2_q1(a,b):
    
    global path

    x=np.arange(-5,5,1)
    plt.plot(x,a*x+b)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(path+'hmwks/hmwk2_q1.png')

def intersect_graph_plot(a,b,c,d):
    global path

    x=np.arange(0,10,1)
    plt.plot(x,a*x+b)
    plt.plot(x,c*x+d)
    plt.xlabel('Days')
    plt.ylabel('Cost (£)')
    plt.savefig(path+'exam/intersect_plot.png')