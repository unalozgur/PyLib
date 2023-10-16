def convtoBin(input : int, bitWidth : int):
    return bin(input & 2**bitWidth-1)[2:]