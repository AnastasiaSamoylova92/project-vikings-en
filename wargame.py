# With a correction already implemented: dont forget to initialize an instance of Class "War"

#! Commenting as not in use, see vikingsClasses.py

# from vikingsClasses import Soldier, Viking, Saxon, War
# import random

# soldier_names = ["albert","andres","archie","dani", "david","gerard","german","graham","imanol","laura"]
# great_war = War()

# #Create 5 Vikings
# for i in range(0,5):
#     if i:
#         great_war.addViking(Viking(soldier_names[random.randint(0,9)],100,random.randint(0,100)))

# #Create 5 Saxons
# for i in range(0,5):
#     if i:
#         great_war.addSaxon(Saxon(100,random.randint(0,100)))
    
# round = 0
# revived_count = 0
# while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
#     print( great_war.vikingAttack() )
#     print( great_war.saxonAttack() )
#     print( great_war.saxonHeal() )
#     print(f"round: {round} // Viking army: {len(great_war.vikingArmy)} warriors",f"and Saxon army: {len(great_war.saxonArmy)} warriors")
#     print(great_war.showStatus())
#     round += 1

# print("\n=== BATTLE SUMMARY ===")
# print(f"Total rounds fought: {round}")
# print(f"Remaining Vikings: {len(great_war.vikingArmy)}")
# print(f"Remaining Saxons: {len(great_war.saxonArmy)}")
# print(f"Count of Viking revived: {revived_count}")