import pandas as pd
import numpy as np

df=pd.read_csv("day02_usage.csv")

chat_narr = df["Chat"].to_numpy()
video_narr = df["Video"].to_numpy()
study_narr = df["Study"].to_numpy()
games_narr = df["Games"].to_numpy()

#length - no.of rows in each col
print("Chat len:",len(chat_narr))
print("Video len:",len(video_narr))
print("Study len:",len(study_narr))
print("Games len:",len(games_narr))

#sum of each col
print("Chat sum:",chat_narr.sum())
print("Video sum:",video_narr.sum())
print("Study sum:",study_narr.sum())
print("Games sum:",games_narr.sum())

#print("Total mins over 30 days:",chat_narr.sum() ,video_narr.sum() ,study_narr.sum() ,games_narr.sum())

#AVERAGE
print("Chat sum:",round(chat_narr.mean(),1))
print("Video sum:",round(video_narr.mean(),1))
print("Study sum:",round(study_narr.mean(),1))
print("Games sum:",round(games_narr.mean(),1))

# Study mins - Game mins
study_games = study_narr - games_narr
print("Study - Games :",study_games)

# best day and worst day
print("Best day: Day",int(study_games.argmax())+1) 
print("Worst day: Day",int(study_games.argmin())+1)
# to_numpy() - returns int64, but 1 is int -> so we can't directly use study_games.argmax()+1

# max app of each day
#for i in range(len(df)):
#    new_list = []
