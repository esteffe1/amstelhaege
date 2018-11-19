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

def random_walk(ah, buildings, random_walks):

	bad_yield = 50000
	scores = []
	top_scores = []
	bad_scores = []
	top_yield = 0
	top_buildings = {}
	top_free_distance = {}
   
	# Random statespace eploration
	for run in range(0, random_walks):
			ah_total_yield = 0
		 
			# Generate random grid posistion
			grid = []
			for y in range(0, 10):
					for x in range (0,10):
							grid.append([x,y])
			random.shuffle(grid)    

			# Calculate distances between all buildings
			dist_table = calc.calc_distance_table( ah, grid )
			# Find neighbours
			min_distance = calc.calc_min_distance( ah, dist_table)

			# Assign each building a grid posisttion  
			for spot in range(0, ah.total):  
					buildings[spot]['x']  = grid[spot][0] * GRID_X
					buildings[spot]['y']  = grid[spot][1] * GRID_Y

			# Calculate extra free distance
			free_distance = calc.calc_s2n( ah, buildings, min_distance)
			
			# Calculate value of Amstelhaege
			score_total = calc.calc_score(ah, buildings, free_distance ) 
			
			for spot in range(0, ah.total):
					ah_total_yield += score_total[spot]['pyp']
			
			if ah_total_yield > top_yield:
					top_yield = ah_total_yield
					top_buildings = copy.deepcopy(buildings)
					top_free_distance = free_distance.copy()
					#print("  Run: ", run,  "Cuurent top yield: ", top_yield)
			if ah_total_yield < bad_yield:
					bad_yield = ah_total_yield
					bad_buildings = copy.deepcopy(buildings)
					bad_free_distance = free_distance.copy()
					#print("  Run: ", run,  "Cuurent top yield: ", top_yield)   
			
			scores.append(ah_total_yield)
			top_scores.append(top_yield)
			bad_scores.append(bad_yield)
			
	# Plot the histogram of all scores   
	plotah.plot_scores2(scores, top_scores, bad_scores, "Random top vs worst yield")

	# Plot the layout of Amstelheage
	ah.top_yield = top_yield
	plotah.ah_plot( ah, top_buildings, top_free_distance)
   
	# Plot the layout of Amstelheage
	ah.top_yield = bad_yield
	plotah.ah_plot( ah, bad_buildings, bad_free_distance )

