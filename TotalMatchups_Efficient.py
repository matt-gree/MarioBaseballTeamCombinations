import math
char_name_dup_list = {
    "Mario",
    "Luigi",
    "DK",
    "Diddy",
    "Peach",
    "Daisy",
    "Yoshi",
    "Baby Mario",
    "Baby Luigi",
    "Bowser",
    "Wario",
    "Waluigi",
    "Koopa",
    "Toad",
    "Boo",
    "Toadette",
    "Shy Guy",
    "Birdo",
    "Monty",
    "Bowser Jr",
    "Paratroopa",
    "Pianta",
    "Noki",
    "Bro",
    "Toadsworth",
    "Magikoopa",
    "King Boo",
    "Petey",
    "Dixie",
    "Goomba",
    "Paragoomba",
    "Dry Bones",
}

captain_list = {
    "Mario",
    "Luigi",
    "Peach",
    "Daisy",
    "Yoshi",
    "Birdo",
    "Wario",
    "Waluigi",
    "DK",
    "Diddy",
    "Bowser",
    "Bowser Jr"
}

char_name_dup_dict = {
    "Koopa": 2,
    "Toad": 5,
    "Shy Guy": 5,
    "Paratroopa": 2,
    "Pianta": 3,
    "Noki": 3,
    "Bro": 3,
    "Magikoopa": 4,
    "Dry Bones": 4
}

num_matchups_from_captain_num = {
    2: 25740,
    3: 77220,
    4: 154440,
    5: 257400,
    6: 386100,
    7: 540540,
    8: 720720,
    9: 926640,
    10: 1158300,
    11: 1415700,
    12: 1698840
}
import time

start = time.perf_counter()
def combination(n, n_list):
    if n <= 0:
        yield set()
        return

    n_list = list(n_list)  # Convert to list
    for i in range(len(n_list)):
        c_num = n_list[i]
        for a_num in combination(n - 1, n_list[i + 1:]):
            yield {c_num} | a_num


def count_valid_teams():
    running_total = 0
    team_count = 0
    for team in combination(18, char_name_dup_list):

        # Check if the team has at least one captain character
        num_captains = len(captain_list.intersection(team))
        if num_captains < 2:
            continue

        duplicates_appended = 1
        for key, value in char_name_dup_dict.items():
            if key in team:
                duplicates_appended *= value

        running_total += duplicates_appended*num_matchups_from_captain_num[num_captains]
    
        team_count += 1
        if team_count%1000000==0:
            print(team_count)
        #print(running_total)
        #running_total += len(base_teams)*math.factorial(num_captains)

    return running_total

total_teams = count_valid_teams()
end = time.perf_counter()
runtime = (end - start) / 60
print(f"Runtime: {runtime} minutes")
print(f"Total Valid Team Combinations: {total_teams}")