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

        try:
            cost = slots[i] * bidders[i]['bid']
        except IndexError:
            cost = 0
        if slot >= len(slots):
            slot = None
        VCG.append({'slot': slot, 'cost': cost, 'bidder': bidders[i]})

    return VCG

def getVickreyCosts(slots, bidders, VCG):
    VCG_copy = list(VCG)
    for i in range(len(bidders)):
        getVickreyCost(slots, bidders, VCG_copy, i)
    return VCG_copy

def getVickreyCost(slots, bidders, VCG, i):
    bidders_copy = list(bidders)
    bidders_copy.remove(bidders[i])
    VCG2 = getVickreySlots(slots, bidders_copy)
    VCG_copy = list(VCG)
    VCG[i]['cost'] = getVickreyCostAdjustment(VCG2, VCG_copy, i)

def getVickreyCostAdjustment(VCG2, VCG, i):
    cost_adjustment = 0
    for j in range(len(VCG2)):
        ranking = VCG2[j]
        if ranking['bidder']['bidder'] > i:
            cost_adjustment += (ranking['cost'] - findBidder(ranking['bidder']['bidder'], VCG)['cost'])
    return cost_adjustment

def findBidder(i, VCG):
    for ranking in VCG:
        if ranking['bidder']['bidder'] == i:
            return ranking
    raise Exception

def toString(VCG):
    # get a string representation of VCG for presentation purposes
    vcg_string = ''
    for ranking in VCG:
        vcg_string += '\nBidder: ' + str(ranking['bidder']['bidder'])
        vcg_string += '\nSlot: ' + str(ranking['slot'])
        vcg_string += '\nCost: ' + str(ranking['cost'])
        vcg_string += '\n'
    return vcg_string

if __name__ == '__main__':
    print('\n---- TEST 1 -----\n')
    slots = [500, 300, 100]
    bidders = [{'bid': .5, 'bidder': 0},
               {'bid': .4, 'bidder': 1},
               {'bid': .3, 'bidder': 2},
               {'bid': .2, 'bidder': 3},
               {'bid': .1, 'bidder': 4}]

    VCG = vickreyClarkGrove(slots, bidders)
    print(toString(VCG))

    print('\n---- TEST 2 -----\n')
    slots = [500, 300, 100]
    bidders = [{'bid': .5, 'bidder': 0},
               {'bid': .45, 'bidder': 1},
               {'bid': .4, 'bidder': 2},
               {'bid': .35, 'bidder': 3},
               {'bid': .3, 'bidder': 4}]

    VCG = vickreyClarkGrove(slots, bidders)
    print(toString(VCG))

    print('\n---- TEST 3 -----\n')
    slots = [500, 300, 100]
    bidders = [{'bid': .5, 'bidder': 0},
               {'bid': .2, 'bidder': 1},
               {'bid': .15, 'bidder': 2},
               {'bid': .1, 'bidder': 3},
               {'bid': .05, 'bidder': 4}]

    VCG = vickreyClarkGrove(slots, bidders)
    print(toString(VCG))

    print('\n---- TEST 4 -----\n')
    slots = [500, 300, 100]
    bidders = [{'bid': .5, 'bidder': 0},
               {'bid': .03, 'bidder': 1},
               {'bid': .02, 'bidder': 2},
               {'bid': .01, 'bidder': 3},
               {'bid': .01, 'bidder': 4}]

    VCG = vickreyClarkGrove(slots, bidders)
    print(toString(VCG))

    print('\n---- TEST 5 -----\n')
    slots = [500, 300]
    bidders = [{'bid': .5, 'bidder': 0},
               {'bid': .4, 'bidder': 1},
               {'bid': .3, 'bidder': 2},
               {'bid': .2, 'bidder': 3},
               {'bid': .1, 'bidder': 4}]

    VCG = vickreyClarkGrove(slots, bidders)
    print(toString(VCG))

    print('\n---- TEST 6 -----\n')
    slots = [700, 600, 500, 450, 300, 100, 25]
    bidders = [{'bid': .5, 'bidder': 0},
               {'bid': .4, 'bidder': 1},
               {'bid': .3, 'bidder': 2},
               {'bid': .2, 'bidder': 3},
               {'bid': .1, 'bidder': 4}]

    VCG = vickreyClarkGrove(slots, bidders)
    print(toString(VCG))
