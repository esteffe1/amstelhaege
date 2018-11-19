
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import style
#style.use('Solarize_Light2')

def ah_plot(ah, buildings, free_distance):

   # Plot x and y axis
   limsy = (0, ah.length)
   limsx = (0, ah.width)
   
   fig1 = plt.figure(figsize=[10.0, 10.0], edgecolor='w')
   title = "Amstelhaege yield " + str(int(ah.top_yield))
   plt.title(title)

   # Set colors and other properties
   ax1 = fig1.add_subplot(111, aspect='equal')
   ax1.spines['bottom'].set_color('#dddddd')
   ax1.spines['top'].set_color('#dddddd') 
   ax1.spines['right'].set_color('white')
   ax1.spines['left'].set_color('white')
   ax1.tick_params(axis='x', colors='white')
   ax1.tick_params(axis='y', colors='white')
   ax1.yaxis.label.set_color('white')
   ax1.xaxis.label.set_color('white')
   ax1.title.set_color('red')

   # Assign each building type a colour
   plot_color ={'egw' :'pink', 'bgl' : 'darksalmon', 'msn' : 'lightgreen'}
   
   # Plot the buildings
   for spot in range(0, ah.total):
          
       # Current building
       x = buildings[spot]['x']
       y = buildings[spot]['y']
       
       # Dimensions of current building
       extra  = buildings[spot]['extra']
       width  = buildings[spot]['width']
       length = buildings[spot]['length']
            
       kluer  = plot_color [buildings[spot]['type']]
       
       # Plot the buildings rectangles
       ax1.add_patch(patches.Rectangle((x, y), width+extra, length+extra, fill=None))
       ax1.add_patch(patches.Rectangle((x+extra/2, y+extra/2), width, length, color=kluer))
       
       # Plot the building spot text
       x_midlle = width/2 + extra/2
       y_middle = length/2 + extra/2
       ax1.text(x + x_midlle, y + y_middle, spot, horizontalalignment='center',verticalalignment='center')
       
       # Plot the min distance tracks
       xs = free_distance[spot]['xs']
       ys = free_distance[spot]['ys']
       
       xn = free_distance[spot]['xn']
       yn = free_distance[spot]['yn']
       
       # Set the begin and end point
       ax1.plot(xs, ys, 'ro') 
       ax1.plot(xn, yn, 's')     
       
       ax1.plot([xs,xn],[ys,yn],'k-')
           
   plt.ylim(limsy)
   plt.xlim(limsx)
   
   
def plot_histogram(scores):

   # Plot a histogram
   
   # Create the bins
   bins_total = 100
   bin_start = 8000
   bin_end = 15000
   bins = []
   
   # Fill the bins
   for bint in range(bin_start, bin_end, bins_total):
       bins.append(bint)

   # Do the plot   
   plt.hist(scores, bins, histtype='bar', rwidth=0.8)

   plt.xlabel('x')
   plt.ylabel('y')
   plt.title('State space')
   #plt.legend()
   plt.show()

def plot_scores(scores, title):

   # Do the plot  
   fig = plt.figure(figsize=[12.0, 4.0])   
   plt.plot(scores)

   plt.xlabel('Iterations')
   plt.ylabel('Yield')
   plt.title(title)
  # plt.legend()
   plt.show()
   
def plot_scores2(scores, top_scores, bad_scores, title):

   fig = plt.figure(figsize=[12.0, 4.0])
   fig.add_subplot(1,2,1)
   
   # Do the plot   
   plt.plot(top_scores)
   plt.plot(bad_scores)
   
   plt.xlabel('iterafies')
   plt.ylabel('yield')
   plt.title(title)
   
   # Add a second plot figure
   fig.add_subplot(1,2,2)
   
   # Plot a histogram
   
   # Create the bins
   bins_total = 100
   bin_start = 8000
   bin_end = 15000
   bins = []
   
   # Fill the bins
   for bint in range(bin_start, bin_end, bins_total):
       bins.append(bint)

   # Do the plot   
   plt.hist(scores, bins, histtype='bar', rwidth=0.8)

   plt.xlabel('x')
   plt.ylabel('y')
   plt.title('Random state space')
   
   plt.show(block=True) 
