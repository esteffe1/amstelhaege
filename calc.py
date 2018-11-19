from math import sqrt
import random

GRID_X = 18
GRID_Y = 16

def calc_distance_table(ah, grid ):
    
    # Calculate shortest distance between buildings
    distance = []
    dist_table = []
    for e in range(0,ah.total):
        distance = []
        for h in range(0,ah.total):
            dx = (grid[e][0] - grid[h][0])
            dy = (grid[e][1] - grid[h][1])
            dz = abs((dx * dx) + (dy * dy))
            d = round(sqrt(dz), 2)
            distance.append (d)
        
        dist_table.append(distance)
        
    return dist_table   
    

def calc_min_distance (ah, dist_table):

    dx = ah.length
    dy = ah.width
    dz = (dx * dx) + (dy * dy)

    max_distance = round(sqrt(dz), 2)
    min_distance = []
    for e in range(0,ah.total):
        min_distance.append( [0 ,0, max_distance] )

    for e in range(0,ah.total):  
        n = 0
        d = 0
        for h in range(0,ah.total):
            if e != h:
                if  dist_table[e][h] < min_distance[e][2]:
                    d = dist_table[e][h]
                    n = h
                    min_distance[e] = [e,n,d]   
        
    return min_distance
    
   
def calc_score (ah, buildings, free_distance):

    score = 0
    score_total = {}
    free_length = []
    
    for spot in range(0,ah.total):  
        
        xs = free_distance[spot]['xs']
        ys = free_distance[spot]['ys']
       
        xn = free_distance[spot]['xn']
        yn = free_distance[spot]['yn']
  
        # Calculate extra free space
        free_length.append( sqrt( pow( ( xs - xn), 2) + pow( (ys - yn), 2) ) )
        
        
    for spot in range(0,ah.total):     
        
        # Bonus for each building
        bonus = 1 + (free_length[spot] * buildings[spot]['bonus'])
        
        # Property yield performance
        pyp = bonus * buildings[spot]['value']
        
        score_total[spot] = {'bonus' : bonus, 'pyp' : pyp}
        
        #print(" Score: ", free, score_total, x, x1, y, y1)
        
    return score_total
    
    
    
def calc_s2n(ah, buildings, min_distance):
   
   free_distance = {}
   
   # Plot the buildings
   for spot in range(0, ah.total):
    
       neighbour = min_distance[spot][1]
       
       # Current building
       x = buildings[spot]['x']
       y = buildings[spot]['y']
       
       # Neighbour of current bulding
       xn = buildings[neighbour]['x']
       yn = buildings[neighbour]['y']
       
       # Dimensions of current building
       extra  = buildings[spot]['extra']
       width  = buildings[spot]['width']
       length = buildings[spot]['length']
       
       # Dimensions of neighbour building
       n_extra  = buildings[neighbour]['extra']
       n_width  = buildings[neighbour]['width']
       n_length = buildings[neighbour]['length']
       
       xs = x
       ys = y
       
       # Neighbour top right
       if yn > y  and xn > x:
           ys += length + buildings[spot]['extra'] 
           xs += width  + buildings[spot]['extra']           
           
       # Neighbour bottom left    
       if yn < y  and xn < x:
           yn += n_length + buildings[neighbour]['extra']         
           xn += n_width +  buildings[neighbour]['extra']             
           
       # Neighbour bottom right    
       if yn < y  and xn > x:
           yn += n_length + buildings[neighbour]['extra']         
           xs  += width + buildings[spot]['extra']              
           
       # Neighbour top left    
       if yn > y  and xn < x:
           ys += length + buildings[spot]['extra']         
           xn += n_width + buildings[neighbour]['extra']                 
           
       # Neighbour same y level    
       if yn == y and xn < x:        
          xn += n_width + buildings[neighbour]['extra']            
       elif yn == y and xn > x:        
          xs += width + buildings[spot]['extra']
                   
       # Neighbour same x level    
       if xn == x and yn < y:        
          yn += n_length + buildings[neighbour]['extra']   
          
       elif xn == x and yn > y:        
          ys += length + buildings[spot]['extra']           
        
       free_distance[spot] = {'xs' : xs, 'ys' : ys, 'xn' : xn, 'yn' : yn}
       
   return free_distance
      
    
def random_swap(buildings, grid, grid_list, spot_list):    
    
    # Swap tow buildings with outside grid points
    random_grid = random.randint(20,len(grid_list)-1) 
    #print ("  grid: ", grid_list[random_grid], random_grid, end="")
    random_spot = random.randint(0,len(spot_list)-1) 
    #print ("  spot: ", spot_list[random_spot], random_spot)
    
    # Swap the spot and index
    temp_x = grid[random_spot][0]
    temp_y = grid[random_spot][1]
    
    grid[random_spot][0] = grid[random_grid][0]
    grid[random_spot][1] = grid[random_grid][1] 
     
    grid[random_grid][0] = temp_x
    grid[random_grid][1] = temp_y  
    
    buildings[random_spot]['x']  = grid[random_spot][0] * GRID_X
    buildings[random_spot]['y']  = grid[random_spot][1] * GRID_Y

    
    
    