import random

# Soldier

class Soldier():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        self.blocked_chance = 0.3 #! 30% chance of blocking
        self.blocked_reduction = 0.5 #! 50% damage reduction when blocked

    def battleCry(self):
        return "Odin Owns You All!"
    
    def block_successfully(self):
        return random.random() < self.blocked_chance
  
    def receiveDamage(self, damage):

        global blocked_count #!to capture the variable outside the function
        if self.block_successfully():
            damage = damage * self.blocked_reduction
            blocked_count += 1 #! we add the global variable to count the blocks
            blocking_message = f"{self.name} has blocked the attack. Damage reduced to {damage}"
        else:
            blocking_message = f"{self.name} has received {damage} points of damage"
        self.health -= damage

        global total_damage_done_by_saxons #* to update global variable for data tracking. Done here in case there is an ability that reduces damage
        total_damage_done_by_saxons += damage

        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            random_chance_revive = random.randint(0, 4) #20% possibility of revival
            if random_chance_revive == 1:
                self.health = 50
                global revived_count #!by defining the global variable the classes can access them 
                revived_count +=1
                return f"The viking {self.name} has revived. He is now back to arms."
            else:
                return f"{self.name} has died in act of combat"
                    

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        self.range_threshold = self.health * 0.3 #Range when below 30% of health


    def receiveDamage(self, damage):
        self.health -= damage
        global total_damage_done_by_vikings #* to update global variable for data tracking. Done here in case there is an ability that reduces damage
        total_damage_done_by_vikings += damage
        if self.health > 0:
            self.checkIncreaseAttack()
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
        
    def heal(self):
        healed_amount = random.randint(5, 40) #* random amount to be healed
        self.health += healed_amount
        global total_healed_amount #* to update the global variable for data tracking
        total_healed_amount += healed_amount
        return f"Pray thy gods! a Saxon has healed {healed_amount} points of damage!"

    def is_range(self):
        return self.health <= self.range_threshold

    def checkIncreaseAttack(self):
        if self.is_range():
            global rage_count
            rage_count += 1
            #print("The Saxon is enter in RAGE MODE!")
            self.strength += 5 # Plus 5 to damage 

# WAAAAAAAAAGH

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        self.revived_count = 0 #added

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        if self.vikingArmy == []:
            return  #! We addded the condition to avoid that vikings attack when the list is empty
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        result = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result
    
    def saxonAttack(self):
        if self.saxonArmy == []:
            return  #! We added the condition to avoid that saxons attack when the list is empty
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        result = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result
    
    def saxonHeal(self):
        if self.saxonArmy == []:
            return  #! We added the condition to avoid that saxons heal when the list is empty
        saxon = random.choice(self.saxonArmy)
        result = saxon.heal()
        return result
    
    def checkVikingBattleCry(self):
        if self.vikingArmy == []:
            return  #! We added the condition to avoid that vikings ability when the list is empty
        battle_cry_chance = random.randint(1, 5)
        if battle_cry_chance == 1: # 20% chance of happening
            for viking in self.vikingArmy:
                viking.strength += 10 # Increase the strengh of all vikings by 10
            global battlecry_count #* to update the global variable for data tracking
            battlecry_count += 1
            return self.vikingArmy[0].battleCry() # just for the shout!
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

#* Global Variables

viking_names = [
"Ragnar", "Bjorn", "Erik", "Thorvald", "Harald", "Sigurd", "Ivar", "Leif", "Ulf", "Gunnar",
"Eirik", "Sven", "Hakon", "Rolf", "Sten", "Vidar", "Orm", "Viggo", "Torstein", "Halvar",
"Arne", "Trygve", "Odin", "Frode", "Ketil", "Runar", "Magnus", "Asmund", "Steinar", "Thorkell"
]
great_war = War()
round_count = 0
total_damage_done_by_saxons = 0
total_damage_done_by_vikings = 0
total_healed_amount = 0
revived_count = 0
blocked_count = 0
battlecry_count = 0
rage_count = 0

#* Creating the Vikings for the War. 
# quantity = 5
# name = random from list
# health = 100
# strength = random from 0 to 100
for i in range(0,5):
    if i:
        great_war.addViking(Viking(viking_names[random.randint(0,29)],100,random.randint(0,100)))

#* Creating the Saxons for the War.
# quantity = 5
# health = 100
# strength = random from 0 to 100
for i in range(0,5):
    if i:
        great_war.addSaxon(Saxon(100,random.randint(0,100)))

#* Main War Loop
while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    great_war.vikingAttack() 
    great_war.saxonAttack() 
    great_war.saxonHeal() 
    great_war.checkVikingBattleCry()
    round_count += 1
    # determine the winner based on game's outcome   


#* Battle Summary
print("\n=== BATTLE SUMMARY ===")
print(great_war.showStatus())
print(f"Total rounds fought: {round_count}")
print(f"Remaining Vikings: {len(great_war.vikingArmy)}")
print(f"Remaining Saxons: {len(great_war.saxonArmy)}")
print(f"Total Damage Done by Saxons: {int(total_damage_done_by_saxons)}") # Total Damage reduced by abilities (block)
print(f"Total Damage Done by Vikings: {total_damage_done_by_vikings}") # Total Damage reduced by abilities
print(f"Total Amount Healed by Saxons: {total_healed_amount}") # chance of one Saxon heal every round
print(f"Total Count of Viking revived: {revived_count}") # chance of revival after hit and dead
print(f"Total Count of Viking blocks: {blocked_count}") # chance of block before hit
print(f"Total Count of Viking Battle Cry activations: {battlecry_count}") # increase strength of all Vikings for the rest of the war
print(f"Total Count of Saxon rage mode: {rage_count}") # increase strength of all Saxon when they are equal or lower than 30% of health 
