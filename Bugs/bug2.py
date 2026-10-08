# DAY 2 - BUG FILE 2 of 6
import numpy as np
import pandas as pd

df = pd.read_csv("day02_usage.csv")
chat = df["Chat"].to_numpy()
#video = df["video"].to_numpy()
video = df["Video"].to_numpy()
study = df["Study"].to_numpy()
games = df["Games"].to_numpy()

print("Total minutes over 30 days")
print("  Chat :", chat.sum())
print("  Video:", video.sum())
print("  Study:", study.sum())
print("  Games:", games.sum())


'''Error at line 7: KeyError
    It is not 'video', it is 'Video'
'''