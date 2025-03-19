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
    def receiveDamage(self, damage):
        self.health -= damage
        global total_damage_done_by_vikings #* to update global variable for data tracking. Done here in case there is an ability that reduces damage
        total_damage_done_by_vikings += damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
    def heal(self):
        healed_amount = random.randint(5, 40) # random amount to be healed
        self.health += healed_amount
        global total_healed_amount #* to update the global variable for data tracking
        total_healed_amount += healed_amount
        return f"Pray thy gods! a Saxon has healed {healed_amount} points of damage!"

# WAAAAAAAAAGH

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

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
            return  #! We addded the condition to avoid that saxons attack when the list is empty
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        result = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result
    
    def saxonHeal(self):
        if self.saxonArmy == []:
            return  #! We addded the condition to avoid that saxons heal when the list is empty
        saxon = random.choice(self.saxonArmy)
        result = saxon.heal()
        return result
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    
# With a correction already implemented: dont forget to initialize an instance of Class "War"

#global var
soldier_names = ["albert","andres","archie","dani", "david","gerard","german","graham","imanol","laura"]
great_war = War()
round = 0
revived_count = 0
blocked_count = 0
total_healed_amount = 0
total_damage_done_by_saxons = 0
total_damage_done_by_vikings = 0

#Create 5 Vikings
for i in range(0,5):
    if i:
        great_war.addViking(Viking(soldier_names[random.randint(0,9)],100,random.randint(0,100)))

#Create 5 Saxons
for i in range(0,5):
    if i:
        great_war.addSaxon(Saxon(100,random.randint(0,100)))
    

while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    print( great_war.vikingAttack() )
    print( great_war.saxonAttack() )
    print( great_war.saxonHeal() )
    print(f"round: {round} // Viking army: {len(great_war.vikingArmy)} warriors",f"and Saxon army: {len(great_war.saxonArmy)} warriors")
    print(great_war.showStatus())
    round += 1

print("\n=== BATTLE SUMMARY ===")
print(f"Total rounds fought: {round}")
print(f"Remaining Vikings: {len(great_war.vikingArmy)}")
print(f"Remaining Saxons: {len(great_war.saxonArmy)}")
print(f"Total Count of Viking revived: {revived_count}")
print(f"Total Count of Viking blocks: {blocked_count}")
print(f"Total Amount Healed by Saxons: {total_healed_amount}")
print(f"Total Damage Done by Saxons: {total_damage_done_by_saxons}") # reduced by abilities (block)
print(f"Total Damage Done by Vikings: {total_damage_done_by_vikings}") 
