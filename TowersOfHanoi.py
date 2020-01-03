def TowersOfHanoi(no_of_disc, from_peg, to_peg, aux_peg):
    if no_of_disc == 1:
        print("Move disk 1 from peg", from_peg, "to peg", to_peg)
        return
    else:
        '''move n-1 discs from A To B Using C'''
        TowersOfHanoi(no_of_disc - 1, from_peg, aux_peg, to_peg)
        print("Move disk", no_of_disc, "from peg", from_peg, "to peg", to_peg)
        '''move n-1 discs from B to C using A'''
        TowersOfHanoi(no_of_disc - 1, aux_peg, to_peg, from_peg)


n = 3
TowersOfHanoi(n, 'A', 'B', 'C')
