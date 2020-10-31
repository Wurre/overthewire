#! /usr/bin/python3
from collections import Counter as count 

def split_cipher(cipher, key_length):
    pos = 0
    krypt_list = ['']*key_length
    for letter in found:
        if pos > (key_length - 1):
            pos = 0
        krypt_list[pos] += letter
        pos += 1
    return krypt_list

def join_cipher(plain_list, key_length):
    plain_text = ""
    for n_char in range(len(plain_list[0])):
        for plain in plain_list:
            if len(plain) > n_char:
                plain_text += plain[n_char]
    return plain_text

def rotate(cipher, ch):
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    plain = ""
    num = alphabet.find(ch)
    if num:
        for char in cipher:
            idx = alphabet.find(char) - num
            plain += alphabet[idx]
        print(count(plain))
        return plain
    else:
        return False

def print_with_len(plain_text, key_len):
    print(' '.join(plain_text[i:i+key_len] for i in range(0,len(plain_text),key_len)))


# Frequency in english lanuage
eng_freq = "etaoinsrhldcumfpgwybvkxjqz"

# Path to cipher file
file1 = "./found2"

# Set key length
key_len = 6

# Read cipher file
f = open(file1)
found = f.readline()
found = found.replace(" ", "") # remove spaces

# Split cipher text into n (key_length) different mono alphapbetic ciphers
split_list = split_cipher(found, key_len)
for cipher in split_list:
    print(count(cipher))


#                5    10   15   20   25
#alphabet = "abcdefghijklmnopqrstuvwxyz"
print("Frequency plain text:")
rot = []
rot.append(rotate(split_list[0], 'F'))
rot.append(rotate(split_list[1], 'R'))
rot.append(rotate(split_list[2], 'E'))
rot.append(rotate(split_list[3], 'K'))
rot.append(rotate(split_list[4], 'E'))
rot.append(rotate(split_list[5], 'Y'))

join_rot = join_cipher(rot, key_len)

print_with_len(join_rot, key_len)

