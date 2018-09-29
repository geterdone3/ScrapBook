#!/usr/bin/env python2

import random
HASH = sys.argv[1]
HASH = '_' + HASH
flag = sys.argv[2]

def genData():
    eng2jib = {'0': 'octocat', '1': 'Octocat', '2': 'oCtocat', '3': 'OCtocat', '4': 'ocTocat', '5': 'OcTocat', '6': 'oCTocat', '7': 'OCTocat', '8': 'octOcat', '9': 'OctOcat', 'a': 'oCtOcat', 'b': 'OCtOcat', 'c': 'ocTOcat', 'd': 'OcTOcat', 'e': 'oCTOcat', 'f': 'OCTOcat', 'g': 'octoCat', 'h': 'OctoCat', 'i': 'oCtoCat', 'j': 'OCtoCat', 'k': 'ocToCat', 'l': 'OcToCat', 'm': 'oCToCat', 'n': 'OCToCat', 'o': 'octOCat', 'p': 'OctOCat', 'q': 'oCtOCat', 'r': 'OCtOCat', 's': 'ocTOCat', 't': 'OcTOCat', 'u': 'oCTOCat', 'v': 'OCTOCat', 'w': 'octocAt', 'x': 'OctocAt', 'y': 'oCtocAt', 'z': 'OCtocAt', 'A': 'ocTocAt', 'B': 'OcTocAt', 'C': 'oCTocAt', 'D': 'OCTocAt', 'E': 'octOcAt', 'F': 'OctOcAt', 'G': 'oCtOcAt', 'H': 'OCtOcAt', 'I': 'ocTOcAt', 'J': 'OcTOcAt', 'K': 'oCTOcAt', 'L': 'OCTOcAt', 'M': 'octoCAt', 'N': 'OctoCAt', 'O': 'oCtoCAt', 'P': 'OCtoCAt', 'Q': 'ocToCAt', 'R': 'OcToCAt', 'S': 'oCToCAt', 'T': 'OCToCAt', 'U': 'octOCAt', 'V': 'OctOCAt', 'W': 'oCtOCAt', 'X': 'OCtOCAt', 'Y': 'ocTOCAt', 'Z': 'OcTOCAt', '!': 'oCTOCAt', '"': 'OCTOCAt', '#': 'octocaT', '$': 'OctocaT', '%': 'oCtocaT', '&': 'OCtocaT', "'": 'ocTocaT', '(': 'OcTocaT', ')': 'oCTocaT', '*': 'OCTocaT', '+': 'octOcaT', ',': 'OctOcaT', '-': 'oCtOcaT', '.': 'OCtOcaT', '/': 'ocTOcaT', ':': 'OcTOcaT', ';': 'oCTOcaT', '<': 'OCTOcaT', '=': 'octoCaT', '>': 'OctoCaT', '?': 'oCtoCaT', '@': 'OCtoCaT', '[': 'ocToCaT', '\\': 'OcToCaT', ']': 'oCToCaT', '^': 'OCToCaT', '_': 'octOCaT', '`': 'OctOCaT', '{': 'oCtOCaT', '|': 'OCtOCaT', '}': 'ocTOCaT', '~': 'OcTOCaT', ' ': 'oCTOCaT', '\t': 'OCTOCaT', '\n': 'octocAT', '\r': 'OctocAT', '\x0b': 'oCtocAT', '\x0c': 'OCtocAT'}

    text = open("junglebook.txt", 'r').readlines()

    intt = random.randint(100, len(text)-100)
    text = text[:intt] + ["flag{" + flag + HASH + "}"] + text[intt:]

    final = ""
    for char in text:
        final = final + eng2jib[char] + ' '
    final = final[:-1]

    f = open("Enter/importantData", 'w')
    f.write(final)
    f.close()

genData()
