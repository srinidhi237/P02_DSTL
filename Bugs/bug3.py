# DAY 2 - BUG FILE 3 of 6
# First SILENT bug. Stop the room here.
import numpy as np
import pandas as pd

df = pd.read_csv("day02_usage.csv")
chat = df["Chat"].to_numpy()
video = df["Video"].to_numpy()
study = df["Study"].to_numpy()
games = df["Games"].to_numpy()

DAYS = 30
print("Average minutes per day over", DAYS, "days")
print("  Chat :", chat.sum() // DAYS)
print("  Video:", video.sum() // DAYS)
print("  Study:", study.sum() // DAYS)
print("  Games:", games.sum() // DAYS)

print("\nTotal screen time per day, on average:",
      (chat.sum() // DAYS) + (video.sum() // DAYS)
      + (study.sum() // DAYS) + (games.sum() // DAYS))