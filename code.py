#Step02

import pandas as pd
import numpy as np

df=pd.read_csv("day02_usage.csv")

chat = df["Chat"].to_numpy()
video = df["Video"].to_numpy()
study = df["Study"].to_numpy()
games = df["Games"].to_numpy()

#length - no.of rows in each col
print("Chat len:",len(chat))
print("Video len:",len(video))
print("Study len:",len(study))
print("Games len:",len(games))

#sum of each col
print("Chat sum:",chat.sum())
print("Video sum:",video.sum())
print("Study sum:",study.sum())
print("Games sum:",games.sum())

#print("Total mins over 30 days:",chat_narr.sum() ,video_narr.sum() ,study_narr.sum() ,games_narr.sum())

#AVERAGE
print("Chat sum:",round(chat.mean(),1))
print("Video sum:",round(video.mean(),1))
print("Study sum:",round(study.mean(),1))
print("Games sum:",round(games.mean(),1))

# Study mins - Game mins
study_games = study - games
print("Study - Games :",study_games)

# best day and worst day
print("Best day: Day",int(study_games.argmax())+1) 
print("Worst day: Day",int(study_games.argmin())+1)
# to_numpy() - returns int64, but 1 is int -> so we can't directly use study_games.argmax()+1

#Part D- max app of each day
apps = ['Chat','Video','Study','Games']

for i in range(len(df)):
    list = np.array([chat[i],video[i],study[i],games[i]])
    idx = int(list.argmax())
    print(f"Day{i+1} App:{apps[idx]}")


#2nd way
'''
winners=[]
for i in range(len(df)):
    list =[chat[i],video[i],study[i],games[i]]

    #finding max index
    best=0
    for j in range(1,4):
        if list[j] > list[best]:
            best=j
    winners.append(apps[best])

'''

#Part - D2
total_sum = chat+video+study+games

chat_share = (chat/total_sum)*100       # chat[1]/total_sum[1] - like this runs 30 times
                                        #chat_share contains 30 values - 30 days each
video_share = (video/total_sum)*100
study_share = (study/total_sum)*100
games_share = (games/total_sum)*100
#chatgpt_share = (gpt_share/total_sum)*100

#If new app is included - how many lines will change
'''line 65 is changed - add the new app to total_sum.
    if we directly write line 72 without adding gpt array to total_sums - biggest mistake.
    It won't give error, it executes but only 4 apps data is considered for total sum.

    Hence if new app is added - we should manually add 2 changes
'''

#Printing the shares of each day
print("\nDay 1 Shares:",round(chat_share[0],1),round(video_share[0],1),
      round(study_share[0],1),round(games_share[0],1))

'''If we want to print for 30 days - 30 lines
    Even tho we write it in for loop - still.... (...)'''