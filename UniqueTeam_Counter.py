char_name_dup_list = [
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
]

captain_list = [
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
]

char_name_dup_dict = {
    "Koopa": ["Koopa(G)", "Koopa(R)"],
    "Toad": ["Toad(R)", "Toad(B)", "Toad(Y)", "Toad(G)", "Toad(P)"],
    "Shy Guy": ["Shy Guy(R)", "Shy Guy(B)", "Shy Guy(Y)", "Shy Guy(G)", "Shy Guy(Bk)"],
    "Paratroopa": ["Paratroopa(R)", "Paratroopa(G)",],
    "Pianta": ["Pianta(B)", "Pianta(R)", "Pianta(Y)"],
    "Noki": ["Noki(B)", "Noki(R)", "Noki(G)"],
    "Bro": ["Bro(H)", "Bro(B)", "Bro(F)"],
    "Magikoopa": ["Magikoopa(B)", "Magikoopa(R)", "Magikoopa(G)", "Magikoopa(Y)"],
    "Dry Bones": ["Dry Bones(Gy)", "Dry Bones(G)", "Dry Bones(B)", "Dry Bones(R)",]
}
import time
import csv

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
    for team in combination(9, set(char_name_dup_list)):
        team_with_duplicates = set(team)  # Create a set for the team

        # Check if the team has at least one captain character
        num_captains = sum(captain in team_with_duplicates for captain in captain_list)
        if num_captains == 0:
            continue

        base_teams = [team_with_duplicates]  # List to store base teams
        duplicates_appended = 1
        duplicate_number = 1
        for key, value in char_name_dup_dict.items():
            if key in team:
                duplicate_teams = []  # List to store teams with duplicates
                duplicates_appended *= duplicate_number
                for base_team in base_teams:
                    if key in base_team:
                        base_team.remove(key)  # Remove the base character
                        for duplicate in value:
                            team_with_duplicates = base_team.copy()  # Create a copy of the base team
                            team_with_duplicates.add(duplicate)  # Add the duplicate character
                            duplicate_teams.append(team_with_duplicates)
                        duplicate_number = len(value)

                base_teams.extend(duplicate_teams)  # Extend the list with teams including duplicates
                base_teams = base_teams[duplicates_appended:]

        team_count += 1
        print(team_count)
        running_total += len(base_teams)*num_captains

    return running_total

total_teams = count_valid_teams()
end = time.perf_counter()
runtime = (end - start) / 60
print(f"Runtime: {runtime} minutes")
print(f"Total Valid Team Combinations: {total_teams}")