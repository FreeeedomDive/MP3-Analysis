import math


def dec_to_bin(number):
    bin = ""
    while number > 0:
        bin += str(number % 2)
        number = number // 2
    return bin


def bin_to_dec(str):
    number = 0
    for i in range(0, len(str)):
        n = int(str[i])
        number += math.pow(2, i) * n
    return number


def make_length_correct(length):
    bin_str = dec_to_bin(length)
    if len(bin_str) > 24:
        bin_str = bin_str[:23] + bin_str[24:]
    if len(bin_str) == 24:
        bin_str = bin_str[:23]
    if len(bin_str) > 16:
        bin_str = bin_str[:15] + bin_str[16:]
    if len(bin_str) == 16:
        bin_str = bin_str[:15]
    if len(bin_str) > 8:
        bin_str = bin_str[:7] + bin_str[8:]
    if len(bin_str) == 8:
        bin_str = bin_str[:7]
    return int(bin_to_dec(bin_str))
