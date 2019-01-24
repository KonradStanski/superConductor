from matplotlib import pyplot as plt  # for plotting
from matplotlib import animation
import numpy as np  # for some mathematical functions
import random  # for random number generator

plt.close('all')  # close previous figure windows

Lx = 32
Ly = 32
N = Lx*Ly

kT = 0.09
NSteps = 10000  # Number of Monte Carlo Steps
random.seed(23)  # Ofir found a cool pattern for kT=0.1, L=16
# random.seed(1345) #cool


def getEnergy():
    # Loop over the n.n. pairs to calculate the energy:
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
    for j in range(N):  # Do more steps for bigger lattices
        # Step 2:
        s = random.randint(0, N-1)  # random integer between 0 and N-1
        p_old = theta_array[s]  # store the original value of the phase
        # p_new = 2*np.pi*random.random() #choose a random new phase

        # More efficient p_new for low T:
        d_theta = 1.0*(random.random() - 0.5)
        p_new = p_old + d_theta

        # Faster way to calculate E_diff:
        E_diff = 0
        # Loop over the 4 neighbours:
        for j in range(4):
            nn_site = nn_array[s][j]  # Neighbour j of site s
            cos_old = np.cos(p_old - theta_array[nn_site])
            cos_new = np.cos(p_new - theta_array[nn_site])
            E_diff = E_diff - (cos_new - cos_old)

        # Step 4: Accept the move with probability prob if E_diff > 0
        if (E_diff <= 0) or (random.random() < np.exp(-E_diff/kT)):
            theta_array[s] = p_new


# Loop to calculate x and y for each site number i:
x_array = np.zeros(N)
y_array = np.zeros(N)
for i in range(N):
    x = i % Lx
    y = (i-x)/Lx
    x_array[i] = x
    y_array[i] = y

theta_array = np.zeros(N)
# Step 1: initially give each rotor a random phase:
for i in range(N):
    r = random.random()
    theta_array[i] = 2*np.pi*r

# Calculate the locations of all the nearest neighbours:
nn_array = np.zeros((N, 4), dtype='int')
for i in range(N):
    # Neighbour to the right:
    if x_array[i] != Lx-1:  # if not on the right edge
        nn_array[i][0] = i+1
    else:  # correct the right edge
        nn_array[i][0] = i+1-Lx

    # Neighbour in the upward direction:
    if y_array[i] != Ly-1:  # if not on the upper edge
        nn_array[i][1] = i+Lx
    else:  # correct the upper edge
        nn_array[i][1] = i+Lx-N

    # Neighbour to the left:
    if x_array[i] != 0:  # if not on the left edge
        nn_array[i][2] = i-1
    else:  # correct the left edge
        nn_array[i][2] = i-1+Lx

    # Neighbour in the downward direction:
    if y_array[i] != 0:  # if not on the bottom edge
        nn_array[i][3] = i-Lx
    else:  # correct the bottom edge
        nn_array[i][3] = i-Lx+N


# function that the animator will call NStep times:
def animate(i):
    # if i % 10 == 0:
        # print("Step %d".format(i))
    MCStep()

    u_array = np.cos(theta_array)     # length along u for each rotor
    v_array = np.sin(theta_array)     # length along v for each rotor
    qu.set_UVC(u_array, v_array)


u_array = np.cos(theta_array)     # length along u for each rotor
v_array = np.sin(theta_array)     # length along v for each rotor

fig = plt.figure()
arrow_colour = (64/255.0, 196/255.0, 180/255.0)
# Format: plt.quiver( x_array, y_array, u_array, v_array)
qu = plt.quiver(x_array, y_array, np.cos(theta_array), np.sin(theta_array),
                units='xy', scale=1.2, pivot='middle', color=arrow_colour)

plt.xlim(-1, Lx)
plt.ylim(-1, Ly)

# Call the animator function many times (i.e. do many MC steps):
anim = animation.FuncAnimation(fig, animate, frames=NSteps, interval=500,
                               repeat=False)

plt.show()
