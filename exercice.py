#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dataclasses import replace


def majuscule(mots):
    # TODO completer la fonction ici
    maj=""
    for lettres in mots:
        maj+=chr(ord(lettres)-32)
    return


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
