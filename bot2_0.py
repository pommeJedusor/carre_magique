def get_moves(pos):
    for i in range(0,512):
        #case 0
        #0 1 3
        if (((pos & 2**0) >> 0) ^ ((i & 2**0)) ^ ((i & 2**1) >> 1) ^ ((i & 2**3) >> 3)):
            continue
        #case 1
        #0 1 2 4
        if (((pos & 2**1) >> 1) ^ ((i & 2**0)) ^ ((i & 2**1) >> 1) ^ ((i & 2**2) >> 2) ^ ((i & 2**4) >> 4)):
            continue
        #case 2
        #1 2 5
        if (((pos & 2**2) >> 2) ^ ((i & 2**1) >> 1) ^ ((i & 2**2) >> 2) ^ ((i & 2**5) >> 5)):
            continue
        #case 3
        #0 3 4 6
        if (((pos & 2**3) >> 3) ^ ((i & 2**0)) ^ ((i & 2**3) >> 3) ^ ((i & 2**4) >> 4) ^ ((i & 2**6) >> 6)):
            continue
        #case 4
        #0 2 4 6 8
        if (((pos & 2**4) >> 4) ^ ((i & 2**0)) ^ ((i & 2**2) >> 2) ^ ((i & 2**4) >> 4) ^ ((i & 2**6) >> 6) ^ ((i & 2**8) >> 8) == 0):
            #print(i)
            continue
        #case 5
        #2 4 5 8
        if (((pos & 2**5) >> 5) ^ ((i & 2**2) >> 2) ^ ((i & 2**4) >> 4) ^ ((i & 2**5) >> 5) ^ ((i & 2**8) >> 8)):
            continue
        #case 6
        #3 6 7
        if (((pos & 2**6) >> 6) ^ ((i & 2**3) >> 3) ^ ((i & 2**6) >> 6) ^ ((i & 2**7) >> 7)):
            continue
        #case 7
        #4 6 7 8
        if (((pos & 2**7) >> 7) ^ ((i & 2**4) >> 4) ^ ((i & 2**6) >> 6) ^ ((i & 2**7) >> 7) ^ ((i & 2**8) >> 8)):
            continue
        #case 8
        #5 7 8
        if (((pos & 2**8) >> 8) ^ ((i & 2**5) >> 5) ^ ((i & 2**7) >> 7) ^ ((i & 2**8) >> 8)):
            continue
        
        return i

def get_binpos(pos):
    bin_pos = 0
    for i in range(9):
        if pos[i]:
            bin_pos += 2**i
    return bin_pos

def get_nun_bin_moves(moves):
    final_moves = []
    for i in range(9):
        if 2**i & moves:
            final_moves.append(i)
    return final_moves

def bot(pos):
    binpos = get_binpos(pos)
    moves = get_moves(binpos)
    return get_nun_bin_moves(moves)
