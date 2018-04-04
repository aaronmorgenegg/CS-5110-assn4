# Aaron Morgenegg

def vickreyClarkGrove(slots, bidders):
    # Given descendingly sorted lists of slots and bidders, compute VCG

    # Figure out the winners of the auction
    VCG = getVickreySlots(slots, bidders)

    # Figure out the cost for the slots
    return getVickreyCosts(slots, bidders, VCG)

def getVickreySlots(slots, bidders):
    VCG = []

    # Assign slots to highest bidders
    for i in range(len(bidders)):
        slot = i
        if slot >= len(slots):
            slot = None
        VCG.append({'slot': slot})

    VCG = getVickreyCosts(slots, bidders, VCG)
    return VCG

def getVickreyCosts(slots, bidders, VCG):
    for i in range(len(bidders)):
        VCG[i]['cost'] = getVickreyCost(slots, bidders, VCG, i)
    return VCG

def getVickreyCost(slots, bidders, VCG, i):
    try:
        cost = slots[VCG[i]['slot']]
    except TypeError:
        return 0
    bidders_copy = list(bidders)
    bidders_copy.remove(bidders[i])
    VCG2 = getVickreySlots(slots, bidders_copy)
    VCG_copy = list(VCG)
    print(VCG2)
    print(VCG)

    return 0

if __name__ == '__main__':
    slots = [500, 300, 100]
    bidders = [.5, .4, .3, .2, .1]
    VCG = vickreyClarkGrove(slots, bidders)
    print(VCG)
