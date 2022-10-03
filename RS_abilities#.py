abilities_bar = [Omnipower, Asphyxiate, GConc, DBreath, Wrack, Impact, Auto]

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
ability_list = [Omnipower, Asphyxiate, GConc, DBreath, Wrack, Impact, Auto]

    
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
    print("ability chosen:", ability_used.name)
    
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
    
##########
def CurrentOutput():
    tick: 0
    adren: 0 damage 0
    cd's: [0, 0, 0, 0, 0]
    ability chosen: GConc

    tick: 4
    adren: 8 damage 107.0
    cd's: [5, 0, 0, 0, 0]
    ability chosen: DBreath

    tick: 6
    adren: 16 damage 182.5
    cd's: [3, 15, 0, 0, 0]
    ability chosen: Wrack

    tick: 8
    adren: 24 damage 220.5
    cd's: [1, 13, 3, 0, 0]
    ability chosen: Impact

    tick: 10
    adren: 32 damage 260.5
    cd's: [0, 11, 1, 23, 0]
    ability chosen: GConc

    tick: 14
    adren: 40 damage 367.5
    cd's: [5, 7, 0, 19, 0]
    ability chosen: Wrack

    tick: 16
    adren: 48 damage 405.5
    cd's: [3, 5, 3, 17, 0]
    ability chosen: Auto

    tick: 18
    adren: 56 damage 405.5
    cd's: [0, 1, 3, 1, 15, 0]
    ability chosen: Asphyxiate

    tick: 26
    adren: 41 damage 706.5
    cd's: [0, 0, 0, 7, 0]
    ability chosen: GConc

    tick: 30
    adren: 49 damage 813.5
    cd's: [5, 0, 0, 3, 0]
    ability chosen: DBreath

    tick: 32
    adren: 57 damage 889.0
    cd's: [20, 3, 15, 0, 1, 0]
    ability chosen: Wrack

    tick: 34
    adren: 65 damage 927.0
    cd's: [18, 1, 13, 3, 0, 0]
    ability chosen: Impact

    tick: 36
    adren: 73 damage 967.0
    cd's: [16, 0, 11, 1, 23, 0]
    ability chosen: GConc

    tick: 40
    adren: 81 damage 1074.0
    cd's: [12, 5, 7, 0, 19, 0]
    ability chosen: Wrack

    tick: 42
    adren: 89 damage 1112.0
    cd's: [10, 3, 5, 3, 17, 0]
    ability chosen: Auto

    tick: 44
    adren: 97 damage 1112.0
    cd's: [8, 1, 3, 1, 15, 0]
    ability chosen: Auto

    tick: 46
    adren: 100 damage 1112.0
    cd's: [0, 6, 0, 1, 0, 13, 0]
    ability chosen: Omnipower

    tick: 51
    adren: 0 damage 1212.0
    cd's: [0, 0, 0, 8, 0]
    ability chosen: GConc

    tick: 55
    adren: 8 damage 1319.0
    cd's: [5, 0, 0, 4, 0]
    ability chosen: DBreath

    tick: 57
    adren: 16 damage 1394.5
    cd's: [3, 15, 0, 2, 0]
    ability chosen: Wrack

    tick: 59
    adren: 24 damage 1432.5
    cd's: [1, 13, 3, 0, 0]
    ability chosen: Impact

    tick: 61
    adren: 32 damage 1472.5
    cd's: [0, 11, 1, 23, 0]
    ability chosen: GConc

    tick: 65
    adren: 40 damage 1579.5
    cd's: [5, 7, 0, 19, 0]
    ability chosen: Wrack

    tick: 67
    adren: 48 damage 1617.5
    cd's: [3, 5, 3, 17, 0]
    ability chosen: Auto

    tick: 69
    adren: 56 damage 1617.5
    cd's: [0, 1, 3, 1, 15, 0]
    ability chosen: Asphyxiate

    tick: 77
    adren: 41 damage 1918.5
    cd's: [0, 0, 0, 7, 0]
    ability chosen: GConc

    tick: 81
    adren: 49 damage 2025.5
    cd's: [5, 0, 0, 3, 0]
    ability chosen: DBreath

    tick: 83
    adren: 57 damage 2101.0
    cd's: [20, 3, 15, 0, 1, 0]
    ability chosen: Wrack

    tick: 85
    adren: 65 damage 2139.0
    cd's: [18, 1, 13, 3, 0, 0]
    ability chosen: Impact

    tick: 87
    adren: 73 damage 2179.0
    cd's: [16, 0, 11, 1, 23, 0]
    ability chosen: GConc

    tick: 91
    adren: 81 damage 2286.0
    cd's: [12, 5, 7, 0, 19, 0]
    ability chosen: Wrack

    tick: 93
    adren: 89 damage 2324.0
    cd's: [10, 3, 5, 3, 17, 0]
    ability chosen: Auto

    tick: 95
    adren: 97 damage 2324.0
    cd's: [8, 1, 3, 1, 15, 0]
    ability chosen: Auto

    tick: 97
    adren: 100 damage 2324.0
    cd's: [0, 6, 0, 1, 0, 13, 0]
    ability chosen: Omnipower
