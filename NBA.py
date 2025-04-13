import requests
from bs4 import BeautifulSoup

win = 0
lose = 1
teams = []
wins = []
loses = []
wins_and_losses = []
url = 'https://tw.sports.yahoo.com/nba/standings/?selectedTab=CONFERENCE'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
for team in soup.find_all('span', {'class': "Va(m) Px(cell-padding-x)"}):
    if team.get_text() != '':
        get = team.get_text()
        if get.find('-') != -1:
            if len(get) == 4:
                teams.append(get[:get.find(' ')])
            else:
                teams.append("{0:{1}^4}".format(get[:get.find(' ')], chr(12288)))
        else:
            if len(get) == 4:
                teams.append(get)
            else:
                teams.append("{0:{1}^4}".format(get, chr(12288)))

for all_result in soup.find_all('td'):
    wins_and_losses.append(all_result.get_text())
for i in range(0, int(len(wins_and_losses) / 13)):
    wins.append(wins_and_losses[win])
    win += 13
    loses.append(wins_and_losses[lose])
    lose += 13
print("戰績:")
print("{:^6}{:^5}{:^5}".format("球隊", "勝場數", "敗場數"))
for e in range(0, 30):
    if e == 15:
        print("")
    if teams[e] == "76人　":  # 排版美觀
        print("  ", end="")
    print("{:6}{:^5}{:^8}".format(teams[e], wins[e], loses[e]))

play_teams = []
scores = []
for play in soup.find_all("span", {"data-tst": "last-name"}):
    play_teams.append(play.get_text())
for score in soup.find_all("span", {"class": "YahooSans Fw(700)! Va(m) Fz(24px)!"}):
    scores.append(score.get_text())
print("\n今日賽事:")
q = 0
for p in range(0, int(len(play_teams) / 2)):
    for s in range(1, 3):
        print("{}  {}".format(play_teams[q], scores[q]))
        q += 1
    print()

