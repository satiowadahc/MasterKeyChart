#
# Master Key Template
#
# Plan
#  Take in Number of Keys
#  Take in Number of Doors
#  Take in Number of Pins
#  Take in MACS
#

import numpy as np
import random as rand
#TODO true random?
rand.seed()


class Door:

    def __init__(self, idl, pinCount):
        self.pins = [[0], [0], [0]]
        self.id = idl
        for i in range(pinCount):
            self.pins.append([0])

    def __str__(self):
        return str(self.id)

    def display(self):
        print("Door")
        for i in self.pins:
            print('Pin Chamber ', i)


class Key:
    def __init__(self, idl, cut=3):
        self.cuts = []
        self.id = idl
        for k in range(cut):
            self.cuts.append(0)

    def __str__(self):
        return str(self.id)

    def display(self):
        print("Key" + str(self.id))
        print(self.cuts)


def assigner(keys, doors):

    accessList = np.ones((len(keys), len(doors)))
    print(accessList)
    for k in keys:
        if input('Is key ' + str(k) + ' a master key?') in [1, '1', 'y', 'Y']:
            for d in doors:
                accessList[k.id, d.id] = 1
        else:
            for d in doors:
                test = True
                while test:
                    parse = input("Should key " + str(k) + " open door " + str(d) + "?")
                    if parse in [1, '1', 'y', 'Y']:
                        accessList[k.id, d.id] = 1
                        test = False
                    elif parse in [0, '0', 'n', 'N']:
                        accessList[k.id, d.id] = 0
                        test = False
                    else:
                        print('Please makes sense')
    print(accessList)
    return accessList


def keyCutter(pinCount, MACS, keys, accesslist):
    # Check pins
    if pinCount != len(keys[0].cuts):
        print('Keys do not match pins')
        return 1

    (x, y) = accesslist.shape

    check = 5
    test = True
    for k in keys:
        for c in range(pinCount):
            while test:
                k.cuts[c] = rand.randint(1, 9)
                if abs(c-check) < MACS:
                    test = False


# Testing ------------------

# Create Doors
numDoors = 3
dtl = []
for i in range(numDoors):
    dtl.append(Door(i, 5))

# Create Keys
ktl = []
numKeys = 3
for i in range(numKeys):
    ktl.append(Key(i, 5))

acl = assigner(ktl, dtl)
keyCutter(5, 6, ktl, acl)

for i in ktl:
    print(i.display())
