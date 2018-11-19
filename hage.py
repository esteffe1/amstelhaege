import json
from building import Building
from building import Requirement

class amstel:

    # class attribute
    species = "Heuistieken"

    # instance attribute
    def __init__(self, name):
        self.buildings = self.load_buildings(f"data/{name}")
        self.requirements = self.load_requirements(f"data/{name}")
        
        
        self.top_yield = 0
        
        # Simulated annealling parameters
        self.sfactor = 1
        self.cooling_factor = 1
        self.heartbeat = 10000
    
    def load_buildings(self, filename):
        """"  Load building parameters """
        
        buildings = []
        with open(filename) as json_file:  
            data = json.load(json_file)
           
            for s in data['buildings']: 
                k = s.keys()
                for i in k:
                    t = s[i]            
                     
                    name    = t['name'  ]                   
                    value   = t['value' ]              
                    width   = t['width' ]               
                    length  = t['length']                                  
                    extra   = t['extra' ]                     
                    bonus   = t['bonus' ]  
                  
                    buildings.append( Building(name, value, width, length, extra, bonus) )
                  
        return buildings
    pass

    def load_requirements(self, filename):
        """"  Load building parameters """
        
        requirements = []
        with open(filename) as json_file:  
            data = json.load(json_file)         
            for t in data['area']: 
                    self.name    = t['name'  ]                                       
                    self.width   = t['width' ]               
                    self.length  = t['length']                                  
                    self.pond    = t['pond'  ]                     
                    self.water   = t['water' ]  
                  
            for t in data['composition']: 
                    self.total   = t['total' ]                                       
                    self.ewg     = t['ewg'   ]                
                    self.bgl     = t['bgl'   ]                                  
                    self.msn     = t['msn'   ]                                       
    pass
    
    def __str__(self):
        return f"   {len(self.buildings)}  different types of buildings in the neighbourhood "
    
              
    def load_json(self, filename):
        """
        Load rooms from filename.
        Returns a collection of Room objects.
        """
        with open(filename) as json_file:  
          data = json.load(json_file)
          #print(data) 
          #print("")

          for p in data['area']:
             # print("p is ", p.keys(), p.values(), p['name'] )
              k = p.keys()
              print(" ", k)
              for i in k:
                  t = p[i] 
                  print('area: looks like ' + i + " " + t)
              print("")
              
          for p in data['composition']:
              k = p.keys()
              print(" ", k)
              for i in k:
                  t = p[i] 
                  print('composition: number of ' + i + " " + t)
              print("")
          
          for s in data['buildings']: 
              k = s.keys()
              print(" ", k)
              for i in k:
                  t = s[i]            
                  print('buildings: value of ' + i + " " + t['value'])             
              print("")
      #json.dumps(data, indent=3)