#! /usr/bin/python3

from collections import Counter as count 

def split_cipher(cipher, key_length):
    pos = 0
    krypt_list = ['']*key_length
    for letter in cipher:
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

def build_idx_list(cipher):
    candidates = {}
    for i in range( len(cipher) - 2 ):
        # Loop through the cipher for all conescutive three letter combinations
        candidate = cipher[i:i+3]  # candidate is a three letter string
        if candidate not in candidates:
                f_idx = i   # Set index of where this candidate is first found
                candidates[candidate] = [f_idx]
                while True:
                    f_idx = cipher.find(candidate, f_idx + 1, len(cipher) - 2)
                    if (f_idx != -1):  # If we find another occurence of this candidate later in the text
                        candidates[candidate].append(f_idx - candidates[candidate][0])
                    else:
                        del candidates[candidate][0]
                        break
    return candidates

def get_key_count(candidates):
    
    # Count how many indexes that is dividable by key length among all candidates
    key_count = {}
    for key_len in range(2, 20): # exclude key length 0 and 1
        key_count[key_len] = 0
        for key in candidates:
            for idx in candidates[key]: # skip the first index (0)
                if (idx % key_len == 0):
                    key_count[key_len] += 1
    print("Number of least common denominator for different key length: \n{0}".format( "\n".join(["Key length: {0}, count: {1}".format(k, key_count[k]) for k in key_count]) ) )
    return key_count 

def find_key_len(cipher):
    candidates = build_idx_list(cipher)    
    key_count = get_key_count(candidates)
    
    # Find the key length with highest count
    max_hit_val = 1
    n_keys = len(key_count.values())
    max_hit_idx = n_keys
    print("Searching for key length...")
    for i,v in enumerate( reversed( key_count.values() ) ):
        # Count has to be 20% higher if key length has a common denominator with the current max count key length
        if ( v/max_hit_val > 1.2 or (max_hit_idx % (n_keys - i + 1) != 0 and v/max_hit_val > 1.0) ):
            max_hit_val = v
            max_hit_idx = n_keys - i + 1
            print("Possible key length found: {0}, count: {1}".format(n_keys - i + 1, v))
    print("Key length found: {0}".format(max_hit_idx))
    return max_hit_idx


if __name__ == "__main__":
   
    # Frequency in english lanuage
    # eng_freq = "etaoinsrhldcumfpgwybvkxjqz"
    
    # Path to cipher file
    found1 = "./found1"
    krypton6 = "./krypton6"

    # Read cipher file
    with open(found1) as f:
        found = f.readline()
        found = found.replace(" ", "") # remove spaces

    with open(krypton6) as k6:
        k6_cipher = k6.readline()
        k6_cipher = k6_cipher.replace(" ", "")

    # Find key length
    key_len = find_key_len(found)

    # Split cipher text into n (key_length) different mono alphapbetic ciphers
    split_list = split_cipher(found, key_len)
    for cipher in split_list:
        print(count(cipher))

    split_k6 = split_cipher(k6_cipher, key_len)

    # Manual rotation on each mono cipher based on frequency

    #                5    10   15   20   25
    #alphabet = "abcdefghijklmnopqrstuvwxyz"
    print("Frequency plain text:")
    rot = []
    rot.append(rotate(split_list[0], 'K'))   # X
    rot.append(rotate(split_list[1], 'E'))
    rot.append(rotate(split_list[2], 'Y'))
    rot.append(rotate(split_list[3], 'L'))
    rot.append(rotate(split_list[4], 'E'))
    rot.append(rotate(split_list[5], 'N'))
    rot.append(rotate(split_list[6], 'G'))   # C
    rot.append(rotate(split_list[7], 'T'))
    rot.append(rotate(split_list[8], 'H'))

    join_rot = join_cipher(rot, key_len)
    print(join_rot)

    rotB = []
    rotB.append(rotate(split_k6[0], 'K'))
    rotB.append(rotate(split_k6[1], 'E'))
    rotB.append(rotate(split_k6[2], 'Y'))
    rotB.append(rotate(split_k6[3], 'L'))
    rotB.append(rotate(split_k6[4], 'E'))
    rotB.append(rotate(split_k6[5], 'N'))
    rotB.append(rotate(split_k6[6], 'G'))
    rotB.append(rotate(split_k6[7], 'T'))
    rotB.append(rotate(split_k6[8], 'H'))

    join_rotB = join_cipher(rotB, key_len)
    print("The solution is \"{0}\"".format(join_rotB))


