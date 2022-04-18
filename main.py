#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#


class Node:
    def __init__(self, ch):
        self.ch = ch
        self.is_terminal = False
        self.children = {}


class Trie:
    def __init__(self):
        self.roots = {}

    @staticmethod
    def _add(node, word, i):
        if i >= len(word):
            node.is_terminal = True
            return
        next_ch = word[i]
        if next_ch not in node.children:
            node.children[next_ch] = Node(next_ch)
        Trie._add(node.children[next_ch], word, i + 1)

    def add(self, word, i=0):
        if i >= len(word):
            return
        root_ch = word[i]
        if root_ch not in self.roots:
            self.roots[root_ch] = Node(root_ch)

        self._add(self.roots[root_ch], word, i + 1)

    @staticmethod
    def _has_prefix_relation(node, word, i):
        if node.is_terminal:
            return True
        if i >= len(word):
            return True
        next_ch = word[i]
        if next_ch not in node.children:
            return False

        return Trie._has_prefix_relation(node.children[next_ch], word, i + 1)

    def has_prefix_relation(self, word, i=0):
        if i >= len(word):
            return True
        root_ch = word[i]
        if root_ch not in self.roots:
            return False

        return self._has_prefix_relation(self.roots[root_ch], word, i + 1)


def noPrefix(words):
    trie = Trie()
    for word in words:
        if trie.has_prefix_relation(word.rstrip()):
            print("BAD SET")
            print(word)
            return
        trie.add(word)
    print("GOOD SET")


if __name__ == "__main__":
    with open(os.environ["INPUT_PATH"], "r") as f:
        n = int(f.readline().strip())

        words = []

        for _ in range(n):
            words_item = f.readline()
            words.append(words_item)

        noPrefix(words)
