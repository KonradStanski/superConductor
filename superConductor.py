from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random

# Initialize Variables
plt.close('all')

Lx = 32
Ly = 32
N = Lx*Ly

kT = 0.09
NSteps = 10000
random.seed(23)


def getEnergy():
    cosineSum = 0
    for i in range(N):
        nn_i_right = nn_array[i][0]
        cos1 = np.cos(theta_array[i] - theta_array[nn_i_right])
        nn_i_up = nn_array[i][1]
        cos2 = np.cos(theta_array[i] - theta_array[nn_i_up])
        cosineSum = cosineSum + cos1 + cos2
    energyOverJ = -1*cosineSum
    return energyOverJ


def MCStep():
    for j in range(N):
        # Step 2:
        s = random.randint(0, N-1)
        p_old = theta_array[s] 

        d_theta = 1.0*(random.random() - 0.5)
        p_new = p_old + d_theta

        E_diff = 0
        # Loop over the 4 neighbours:
        for j in range(4):
            nn_site = nn_array[s][j]  # Neighbour j of site s
            cos_old = np.cos(p_old - theta_array[nn_site])
            cos_new = np.cos(p_new - theta_array[nn_site])
            E_diff = E_diff - (cos_new - cos_old)

       
        if (E_diff <= 0) or (random.random() < np.exp(-E_diff/kT)):
            theta_array[s] = p_new


def animate(i):
    # if i % 10 == 0:
        # print("Step %d".format(i))
    MCStep()

    u_array = np.cos(theta_array)
    v_array = np.sin(theta_array)     
    qu.set_UVC(u_array, v_array)


# Main Running Code
x_array = np.zeros(N)
y_array = np.zeros(N)
for i in range(N):
    x = i % Lx
    y = (i-x)/Lx
    x_array[i] = x
    y_array[i] = y

theta_array = np.zeros(N)

for i in range(N):
    r = random.random()
    theta_array[i] = 2*np.pi*r

nn_array = np.zeros((N, 4), dtype='int')
for i in range(N):
    # Neighbour to the right:
    if x_array[i] != Lx-1: 
        nn_array[i][0] = i+1
    else:  
        nn_array[i][0] = i+1-Lx

    # Neighbour in the upward direction:
    if y_array[i] != Ly-1:  
        nn_array[i][1] = i+Lx
    else:  # correct the upper edge
        nn_array[i][1] = i+Lx-N

    # Neighbour to the left:
    if x_array[i] != 0: 
        nn_array[i][2] = i-1
    else: 
        nn_array[i][2] = i-1+Lx

    # Neighbour in the downward direction:
    if y_array[i] != 0:  
        nn_array[i][3] = i-Lx
    else:  
        nn_array[i][3] = i-Lx+N


u_array = np.cos(theta_array)    
v_array = np.sin(theta_array)    

fig = plt.figure()
arrow_colour = (64/255.0, 196/255.0, 180/255.0)
qu = plt.quiver(x_array, y_array, np.cos(theta_array), np.sin(theta_array),
                units='xy', scale=1.2, pivot='middle', color=arrow_colour)

plt.xlim(-1, Lx)
plt.ylim(-1, Ly)

# Call the animator function many times
anim = animation.FuncAnimation(fig, animate, frames=NSteps, interval=500, repeat=False)

plt.show()
