import random

from character import Character

class Monster(Character):
    def __init__(self):
        combat_strength = random.randint(1, 6)
        health_points = random.randint(1, 6)
        super().__init__(combat_strength, health_points)

    # Monster's Attack Function
    def monster_attacks(self, combat_strength, hero_health_points):
        ascii_image2 = """                                                                 
           @@@@ @                           
      (     @*&@  ,                         
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                
               @       /                    
                %         @                 
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
        print(ascii_image2)
        print("    |    Monster's Claw (" + str(combat_strength) + ") ---> Player (" + str(hero_health_points) + ")")
        if combat_strength >= hero_health_points:
            # Monster was strong enough to kill player in one blow
            hero_health_points = 0
            print("    |    Player is dead")
        else:
            # Monster only damaged the player
            hero_health_points -= combat_strength
            print("    |    The monster has reduced Player's health to: " + str(hero_health_points))
        return hero_health_points

    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector")