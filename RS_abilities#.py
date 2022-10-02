class Player:
    t_damage = 0
    adrenaline = 0

class Wrack:
    name = "Wrack"
    damage = (94-18)/2
    cooldown = 5
    cast_time = 1
    adren_gain = 8
    adren_req = 0
    cd = 0
class Impact:
    name = "Impact"
    damage = (100-20)/2
    cooldown = 25
    cast_time = 1
    adren_gain = 8
    adren_req = 0 
    cd = 0
class LConc:
    name = "LConc"
    damage = ((180-36)/2)
    cooldown = 9
    cast_time = 4
    adren_gain = 8
    adren_req = 0
    cd = 0
class LWave:
    name = "LWave"
    damage = ((120-24)/2)
    cooldown = 9
    cast_time = 1
    adren_gain = 8
    adren_req = 0
    cd = 0
class Asphyxiate:
    name = "Asphyxiate"
    damage = ((752-150)/2)
    cooldown = 34
    cast_time = 7
    adren_gain = -15
    adren_req = 50
    cd = 0
class Omnipower:
    name = "Omnipower"
    damage = ((400-200)/2)
    cooldown = 50
    cast_time = 4
    adren_gain = -100
    adren_req = 100
    cd = 0
class DBreath:
    name = "DBreath"
    damage = ((188-37)/2)
    cooldown = 17
    cast_time = 1
    adren_gain = 8
    adren_req = 0
    cd = 0
class GConc:
    name = "GConc"
    damage = ((267-53)/2)
    cooldown = 9
    cast_time = 3
    adren_gain = 8
    adren_req = 0
    cd = 0
class Auto:
    name = "Auto"
    damage = 0
    cooldown = 0
    cast_time = 1
    adren_gain = 8
    adren_req = 0
    cd = 0    

    
#print(Wrack.damage)
#print(Wrack.cd)
#print("T1")

#ability_list = [Wrack, Impact, GConc, Asphyxiate, Omnipower, DBreath, Auto]
ability_list = [Asphyxiate, GConc, DBreath, Wrack, Impact, Auto]

    
def select(c_adren):
    adren_check = []
    cd_list = []
    available = []
    
    for ability in ability_list:
        #print(ability)
        if c_adren >= ability.adren_req:
            #print("AC",ability)
            #print(ability.adren_gain + c_adren)
            adren_check.append(ability)
    
    for ability in adren_check:
        cd_list.append(ability.cd)
        available.append(ability)
    print("cd's:", cd_list)
    #print("available", available)
    first0 = cd_list.index(0)
    first_ab = available[first0]
    
    #print(list1,available,first0)
    #print(first_ab)
    return first_ab


def activate(ability):
    ability.cd = ability.cooldown 
    
    return ability.damage, ability.adren_gain, ability.cast_time

def update():
    for ability in ability_list:
        if ability.cd > 0:
            ability.cd -= 1
    

def cycle():
    adren =  Player.adrenaline
    total_damage = Player.t_damage
    print("adren:", Player.adrenaline, "damage", Player.t_damage)
    
    ability_used = select(adren) #this selects the first ability on the list not on cooldown.
    print("ability chosen", ability_used.name)
    
    dmg_done, adren_gain, cast_time = activate(ability_used) #this activates the selected ability and sets in on cooldown
    
    Player.t_damage += dmg_done
    if Player.adrenaline + adren_gain < 100:
        Player.adrenaline += adren_gain
    else:
        Player.adrenaline = 100
    return cast_time

tick = 0
final_tick = 101
cast_cd = 0

while tick != final_tick:
    
    update()
    if cast_cd == 0:
        print("\ntick:", tick)
        cast_cd = cycle()
    elif cast_cd > 0:
        #print("cast_cd:", cast_cd)
        cast_cd -= 1
    
    tick+=1