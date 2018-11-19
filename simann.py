
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import style
style.use('Solarize_Light2')
from math import sqrt
import random
import copy
import math
import time

# Project source files
import plotah
import calc
import hage

GRID_X = 18
GRID_Y = 16

GRID_X_POINTS = 10
GRID_Y_POINTS = 10


def simulated_annealling(ah, buildings, iterations):

   heartbeat = ah.heartbeat

   scores = []
   best_yield = []
   top_yield = 0
   top_buildings = {}
   top_free_distance = {}

   temp_begin = 100
   temp_end = 0

   cooling = 0
   shortening = 0
   cooling_length = iterations * ah.cooling_factor
   
   
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

   # Keep track of time
   start_time = time.process_time()
   
   # Hill climber eploration
   for iteration in range(0, iterations):
       
       ah_total_yield = 0   
       
       # Save current grid in case 2-opt swap is not succesful
       prev_grid = grid
       
       # Swap two building with free grid points
       calc.random_swap(buildings, grid, grid_list, spot_list)
       calc.random_swap(buildings, grid, grid_list, spot_list)
       
       # Calculate distances between all buildings
       dist_table = calc.calc_distance_table( ah, grid )
       
       # Find neighbours
       min_distance = calc.calc_min_distance( ah, dist_table) 
       
       # Calculate surplus distance between neighbours
       free_distance = calc.calc_s2n( ah, buildings, min_distance)
       
       # Calculate added value of each building in Amstelhaege
       score_total = calc.calc_score(ah, buildings, free_distance ) 
       
       # Calculate yield for this map
       for spot in range(0, ah.total):
           ah_total_yield += score_total[spot]['pyp']
       
       # Keep the best result so far
       if ah_total_yield > top_yield:
           # Result improved, keep this grid
           top_yield = ah_total_yield
           top_buildings = copy.deepcopy(buildings)
           top_free_distance = free_distance.copy()
           #print("  Run: ", "Iteration: ", iteration,  "Current top yield: ", '{:8.2f}'.format(top_yield))
       else:  
           shortening = (ah_total_yield - top_yield ) * ah.sfactor
           # Accept as solution or not
           if iteration < cooling_length:
               temp_actual = temp_begin - (temp_begin - temp_end) * (iteration / cooling_length)
               if temp_actual > 0.01:
                   cooling = shortening / temp_actual

               acceptance = math.exp(cooling)
            
               dice = random.random()
               if dice < acceptance:
                   # Result accepted
                   top_yield = ah_total_yield
                  
                   #print("  Run: ", "Iteration: ", iteration,  "Yes accepted:      ", '{:04.2f}'.format(dice), '{:04.2f}'.format(acceptance), '{:06.2f}'.format(shortening), '{:8.2f}'.format(ah_total_yield))
               else:
                   # Result not accepted, restore previous grid
                   grid = prev_grid
                   
                   # Restore xy coordinates                  
                   for spot in range(0, ah.total):  
                       buildings[spot]['x']  = grid[spot][0] * GRID_X
                       buildings[spot]['y']  = grid[spot][1] * GRID_Y
                   
                   #print("  Run: ", "Iteration: ", iteration,  "Not accepted:      ", '{:04.2f}'.format(dice), '{:04.2f}'.format(acceptance), '{:06.2f}'.format(shortening), '{:8.2f}'.format(ah_total_yield))
       
       # Archive the results
       scores.append(ah_total_yield)
       best_yield.append(top_yield)
       
       if iteration % (heartbeat) == 0:
          time_elapsed =  time.process_time() - start_time
          print(" alive at: ", '{:6d}'.format(iteration), "Time elapsed: ", '{:6.2f}'.format(time_elapsed))
   
   # Iterations per second
   its = (iterations - 1) / time_elapsed 
   print("Iterations per second: ",  '{:6f}'.format(its)  )
   
   # Keep top yield
   ah.top_yield = top_yield
       
   # Plot the histogram of all scores   
   plotah.plot_scores(best_yield, "Simulated annealling - Best yield: ")    
   
   # Plot the histogram of all scores   
   plotah.plot_histogram(scores)
   
   # Plot the layout of Amstelheage
   plotah.ah_plot( ah, top_buildings, top_free_distance)
   