from math import sqrt

def calc_distance( grid ):
    
    # Calculate shortest distance between buildings
    distance = []
    dist_table = []
    for e in range(0,ah.total):
        distance = []
        for h in range(0,ah.total):
            dx = (grid[e][0] - grid[h][0])
            dy = (grid[e][1] - grid[h][1])
            dz = abs((dx * dx) - (dy * dy))
            d = round(sqrt(dz), 2)
            distance.append (d)
        dist_table.append(distance)
    print("")    

    dx = ah.length
    dy = ah.width
    dz = abs((dx * dx) - (dy * dy))

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
    for e in range(0,ah.total):
        print("Distance: ",  min_distance[e])