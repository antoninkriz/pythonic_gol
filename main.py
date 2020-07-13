# GAME OF LIFE
# An attempt at a very "pythonic" Game Of Life implementation
# ---
# Variables: 1 LOC
# Step logic: 3 LOC
# Iteration: 2 LOC
# ---

import os
import platform
import time
import numpy as np


def step(cells):
    tmp = np.array([[cells[y - 1:y + 1 + 1, x - 1:x + 1 + 1].sum() - cells[y, x] for x in range(1, cells.shape[1] - 1)] for y in range(1, cells.shape[0] - 1)])
    return np.pad(np.array([[0 if cells[y + 1, x + 1] == 1 and tmp[y, x] > 3 or tmp[y, x] < 2 else 1 if cells[y + 1, x + 1] == 0 and tmp[y, x] == 3 else cells[y + 1, x + 1] for x in range(cells.shape[1] - 2)] for y in range(cells.shape[0] - 2)]), 1, mode='constant')


cells = np.pad(np.random.randint(2, size=(10, 10), dtype=int), 1, mode='constant')

while True:
    cells = os.system('cls' if platform.system() == 'Windows' else 'clear') or print('\n'.join(''.join(str('X' if c else ' ') for c in r) for r in cells[1:11, 1:11])) or time.sleep(0.5) or step(cells)
