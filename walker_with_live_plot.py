##############################################################
# Basic random walk diffusion simulation with a live plot
# utilizing pyqtgraph.

##############################################################
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
##############################################################

##############################################################
class walker:
    
    # walker class - individual particle taking random walk
    
    # required packages:
    # import numpy as np
    
    # class variables
    step_sz=0.01

    # Instantiation
    def __init__(self):
    
        # Two-coordinate position formatted to
        # work with pyqtgraph scatter plot.
        self.pos = np.zeros(2)
    
    # Take a step            
    def step(self):
        
        # Generate random angle
        theta = np.random.random(1)*2*np.pi
        
        # Update position
        self.pos[0] += np.cos(theta)*self.step_sz
        self.pos[1] += np.sin(theta)*self.step_sz



# instantiate walker
w = walker()

# make the pyqtgraph window
app = QtGui.QApplication([])
mw = QtGui.QMainWindow()
mw.resize(800,800)
view = pg.GraphicsLayoutWidget()  ## GraphicsView with GraphicsLayout inserted by default
mw.setCentralWidget(view)
mw.show()

# Format plot
mw.setWindowTitle('Random Walk')
p1 = view.addPlot()
p1.setRange(xRange=[-1,1])
p1.setRange(yRange=[-1,1])

# Initialize the scatter plot
s1 = pg.ScatterPlotItem(size=10, pen=pg.mkPen(None), brush=pg.mkBrush(255, 255, 255, 120))


# Update function for live plot
def update():

    # Take a step
    w.step()
    
    # Update scatter plot
    new_spot = [{'pos': w.pos, 'data': 1}] 
    s1.addPoints(new_spot)
    p1.addItem(s1)

# execute update function with QTimer
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)


### Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
