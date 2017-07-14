##############################################################
# Random walk diffusion simulation with particle memory.  

# walker class stores entire history of x,y coordinates.


##############################################################
from matplotlib import pyplot as plt
import time
import random
import math
##############################################################

#start timer 
st = time.time()

##############################################################
class walker:

    # walker class - individual particle taking random walk
    
    # required packages: math, random
    
    # class variables
    step_sz=0.01

    # Instantiation
    def __init__(self):

        # Particle location 
        self.x = [0]
        self.y = [0]
        
    def step(self):
    
        # Generate random angle
        theta = random.random()*2*math.pi
        
        # Append x,y lists with new location
        self.x.append(self.x[-1] + math.cos(theta)*self.step_sz)
        self.y.append(self.y[-1] + math.sin(theta)*self.step_sz)



# Make list of walkers
w = [walker() for i in range(100)]

# Loop through list of walkers
for k in range(len(w)):

    # Progress report
    if k%10 == 0 and k != 0:
       print(k,' walkers have completed the journey!')
       
    # Loop through number of steps for current walker   
    for i in range(10000):
        w[k].step()

# Make the figure
f, (ax1,ax2) = plt.subplots(1,2, figsize = (12,6))

# Plot final coordinate for all walkers
for p in range(len(w)):
    ax1.scatter(w[p].x[-1],w[p].y[-1])

# Format subplot    
ax1.set_xlim(left = -3,right = 3)
ax1.set_ylim(bottom = -3,top = 3)
ax1.set_title('Final Position')

# Plot complete paths for a few particles
num_traces = 3
for i in range(num_traces):
    ax2.plot(w[i].x,w[i].y)


# Format subplot 
ax2.set_xlim(left = -3,right = 3)
ax2.set_ylim(bottom = -3,top = 3)
title_str = 'Full Trace For ' + str(num_traces) + ' Particles'
ax2.set_title(title_str)


print('Runtime: ',time.time() - st)
plt.show()

























