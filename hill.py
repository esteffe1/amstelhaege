
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import style
style.use('Solarize_Light2')
from math import sqrt
import random
import copy

# Project source files
import plotah
import calc
import hage

GRID_X = 18
GRID_Y = 16

GRID_X_POINTS = 10
GRID_Y_POINTS = 10


def hillclimber(ah, buildings, iterations):

   heartbeat = 10000

   scores = []
   best_yield = []
   top_yield = 0
   top_buildings = {}
   top_free_distance = {}

   # Generate random grid posistion
   grid = []
   prev_grid = grid
   for y in range(0, GRID_Y_POINTS):
       for x in range (0, GRID_X_POINTS):
            grid.append([x,y])
   random.shuffle(grid)  

   grid_list = []
   for spot in range(0, GRID_X_POINTS * GRID_Y_POINTS):
        grid_list.append(spot)

   spot_list = []
   for spot in range(0, ah.total):
        spot_list.append(spot)   
           
   # Assign each building a grid posisttion  
   for spot in range(0, ah.total):  
       buildings[spot]['x']  = grid[spot][0] * GRID_X
       buildings[spot]['y']  = grid[spot][1] * GRID_Y

   # Hill climber eploration
   for iteration in range(0, iterations):
       
       ah_total_yield = 0   
       # Save current grid if swap is not succesful
       prev_grid = grid
       # Swap two building with free grid poits
       calc.random_swap(buildings, grid, grid_list, spot_list)
       calc.random_swap(buildings, grid, grid_list, spot_list)
       
       # Calculate distances between all buildings
       dist_table = calc.calc_distance_table( ah, grid )
       # Find neighbours
       min_distance = calc.calc_min_distance( ah, dist_table) 
       # Calculate extra free distance
       free_distance = calc.calc_s2n( ah, buildings, min_distance)
       # Calculate value of Amstelhaege
       score_total = calc.calc_score(ah, buildings, free_distance ) 
       
       # Calculate yield for this map
       for spot in range(0, ah.total):
           ah_total_yield += score_total[spot]['pyp']
       
       # Keep the best result sofar
       if ah_total_yield > top_yield:
           # Result improved, keep this grid
           top_yield = ah_total_yield
           top_buildings = copy.deepcopy(buildings)
           top_free_distance = free_distance.copy()
           print("  Run: ", "Iteration: ", iteration,  "Cuurent top yield: ", top_yield)
       else: 
           # Result not improved, restore previous grid
           grid = prev_grid
           #print("  Run: ", run,  "No improvement: ", ah_total_yield)
       
       # Archive the results
       scores.append(ah_total_yield)
       best_yield.append(top_yield)
       
       if iteration % (heartbeat) == 0:
          print(" alive at: ", iteration)
       
   ah.top_yield = top_yield
       
   # Plot the histogram of all scores   
   plotah.plot_scores(best_yield, "Hillclimber best yield")    
   # Plot the histogram of all scores   
   plotah.plot_histogram(scores)
   # Plot the layout of Amstelheage
   plotah.ah_plot( ah, top_buildings, top_free_distance)
   # Plot the layout of Amstelheage
   plotah.ah_plot( ah, buildings, free_distance )
