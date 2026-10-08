# DAY 2 - BUG FILE 1 of 6
# Release first. Students fix it before file 2 appears.
import pandas as pd
import numpy as np

df = pd.read_csv("day02_usage.csv")
chat = df["Chat"].to_numpy()
video = df["Video"].to_numpy()
study = df["Study"].to_numpy()
games = df["Games"].to_numpy()

print("Average minutes per day")
print("  Chat :", np.round(chat.mean(), 1))
print("  Video:", np.round(video.mean(), 1))
print("  Study:", np.round(study.mean(), 1))
print("  Games:", np.round(games.mean(), 1))


'''Error: numpy not imported'''