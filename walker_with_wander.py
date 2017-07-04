##############################################################
# Random walk diffusion simulation with particle memory and wander feature

# wander method takes a specified number of steps



##############################################################
import math
import random
from matplotlib import pyplot as plt
import time
##############################################################
#start timer 
st = time.time()

random.seed()

##############################################################
class walker:
    
    # walker class - individual particle taking random walk
    
    # required packages: math, random
    
    # class variables
    step_sz=0.01

    def __init__(self):

        # Particle location 
        self.x = [0]
        self.y = [0]
    
   
    def step(self):
        # Take a step     
        
        # Generate random angle
        theta = random.random()*2*math.pi
        
        # Append x,y lists with new location
        self.x.append(self.x[-1] + math.cos(theta)*self.step_sz)
        self.y.append(self.y[-1] + math.sin(theta)*self.step_sz)


    def wander(self,num_steps):
        # Take many steps
        
        for i in range(num_steps):
            self.step()
##############################################################

##############################################################
def main():

# Instantiate walker
    w = [walker() for i in range(100)]
    num_steps = 10000

    for k in range(len(w)):
        if k%10 == 0 and k != 0:
           print(k,' walkers have completed the journey!')
        w[k].wander(num_steps)

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


    Runtime = (time.time() - st)
    print('Finished in ',Runtime,' seconds.')

    plt.show()
##############################################################


main()





















