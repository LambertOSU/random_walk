##############################################################
# Random walk diffusion simulation with
# radial concentration analysis.

# This simulation performs a random walk simulation with a
# predefined number of "walkers." The radial concentration
# at the final step is calculated and plotted along with
# a scatter plot of the final position.

# The annulus resolution for the radial concentration
# calculation is defined in the simulation() function.

# The step size is defined in the walker class.

##############################################################
import math
import random
import time
from matplotlib import pyplot as plt
from collections import Counter
from operator import itemgetter
##############################################################
#start timer
st = time.time()

# seed RNG
random.seed()

##############################################################
def main():

    #SIMULATION VARIABLES

    # number of walkers
    num_walkers = 1000

    # number of steps per walker
    num_steps = 10000

    # radial thickness of annuli for post processing
    ring_res = 0.1

    # generate list of walker instances
    w = [walker() for i in range(num_walkers)]


    #SIMULATION LOOP

    # report
    print('\nStarting simulation...\n')

    # loop through list of walkers
    for k in range(len(w)):

        # progress report
        if (k+1)%math.floor(num_walkers/10) == 0:
           print((k+1),'walkers have completed the journey!')

        # walker takes a wander for defined number of steps
        w[k].wander(num_steps)


    # POST PROCESSING

    print('\nSimulation complete! \n\nPost-processing...\n')

    # initialize figure
    f, (ax1,ax2) = plt.subplots(1,2, figsize = (12,6))

    # use latex for properly formatted units in axis labels and titles
    plt.rc('text', usetex=True)

    # scatter plot of final postion
    for p in range(len(w)):
        ax1.scatter(w[p].x[-1],w[p].y[-1])

    # format subplot
    ax1.set_title('Final Position')
    ax1.set_xlabel('$L$')
    ax1.set_ylabel('$L$')

    # generate list of bin numbers
    ring_nums = [w[i].ring(ring_res) for i in range(len(w))]

    # count number of walkers in each bin
    ring_cnt = Counter(ring_nums)

    # sort the counter
    ring_cnt = sorted(ring_cnt.items(), key=itemgetter(0))

    # initialize concentration list
    concentration =[]

    # loop through counter and calculate concentration in each annulus.
    for i in range(len(ring_cnt)):

        # area of anulus
        area = (((ring_res*(ring_cnt[i][0]+1))**2) - (ring_res*ring_cnt[i][0])**2)

        # concentration of particles in annulus
        concentration.append(ring_cnt[i][1]/area)


    # radial coordinates for plotting
    r = [i*ring_res for i in range(len(ring_cnt))]

    # plot concentration
    ax2.plot(r,concentration)

    # format subplot
    ax2.set_title('Radial Concentration')
    ax2.set_xlabel('$L$')
    ax2.set_ylabel('$Number/L^2$')

    # report runtime
    print('Finished in ','%.2f' % (time.time() - st),' seconds.\n')

    plt.show()
############################################################

##############################################################
class walker:

    # walker class - individual particle taking random walk

    # required packages: math, random

    # class variables
    step_sz=0.01

    def __init__(self):

        # particle location
        self.x = [0]
        self.y = [0]


    def step(self):
        # take a step

        # generate random angle
        theta = random.random()*2*math.pi

        # append x,y lists with new location
        self.x.append(self.x[-1] + math.cos(theta)*self.step_sz)
        self.y.append(self.y[-1] + math.sin(theta)*self.step_sz)


    def wander(self,num_steps):
        # take many steps

        for i in range(num_steps):
            self.step()


    def ring(self,ring_resolution):
        # determine radial bin number of particle
        # based on location and bin size

        r = math.sqrt(self.x[-1]**2 + self.y[-1]**2)
        ring_num = math.floor(r/ring_resolution)
        return ring_num


##############################################################

if __name__ == '__main__':
  main()
