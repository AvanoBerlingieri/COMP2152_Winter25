import random

from character import Character

class Hero(Character):
    def __init__(self):
        combat_strength = random.randint(1, 6)
        health_points = random.randint(1, 6)
        super().__init__(combat_strength, health_points)

    # Hero's Attack Function
    def hero_attacks(self, combat_strength, monster_health_points):
        ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  

  """
        print(ascii_image)
        print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(monster_health_points) + ")")
        if combat_strength >= monster_health_points:
            # Player was strong enough to kill monster in one blow
            monster_health_points = 0
            print("    |    You have killed the monster")
        else:
            # Player only damaged the monster
            monster_health_points -= combat_strength

            print("    |    You have reduced the monster's health to: " + str(monster_health_points))
        return monster_health_points

    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector")