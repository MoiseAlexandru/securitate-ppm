
import hashlib

hash_file = open("hashes.txt", "r")

hashlist = hash_file.read().split("\n")
print(hashlist)


def gethash(x, y):
    text = "P6 " + str(x) + " " + str(y) + " 255"
    corresponding_sha256 = hashlib.sha256(text.encode('UTF-8'))
    return corresponding_sha256.hexdigest()


# print(gethash(360, 537))

hash_with_xy = {}
for current_hash in hashlist:
    for X in range(1, 1000):
        for Y in range(1, 1000):
            corresponding_sha256 = gethash(X, Y)
            if corresponding_sha256 == current_hash:
                hash_with_xy[current_hash] = (X, Y)
                break

for elem in hash_with_xy:
    print(elem, hash_with_xy[elem])

matched_hashes = {
    "bd0fd461d87fba0d5e61bed6a399acdfc92b12769f9b3178f9752e30f1aeb81d": 2,
    "602a4a8fff652291fdc0e049e3900dae608af64e5e4d2c5d4332603c9938171d": 5,
    "372df01b994c2b14969592fd2e78d27e7ee472a07c7ac3dfdf41d345b2f8e305": 7,
    "77a39d581d3d469084686c90ba08a5fb6ce621a552155730019f6c02cb4c0cb6": 3,
    "456ae6a020aa2d54c0c00a71d63033f6c7ca6cbc1424507668cf54b80325dc01": 6,
    "70f87d0b880efcdbe159011126db397a1231966991ae9252b278623aeb9c0450": 4,
    "aa105295e25e11c8c42e4393c008428d965d42c6cb1b906e30be99f94f473bb5": 1,
    "f40e838809ddaa770428a4b2adc1fff0c38a84abe496940d534af1232c2467d5": 8
}

