# Function to find list of students who play both cricket and badminton
def both_cricket_badminton(cricket_players, badminton_players):
    both_play = []
    for student in cricket_players:
        if student in badminton_players:
            both_play.append(student)
    return both_play

# Function to find list of students who play either cricket or badminton but not both
def either_cricket_or_badminton(cricket_players, badminton_players):
    either_play = []
    for student in cricket_players:
        if student not in badminton_players:
            either_play.append(student)
    for student in badminton_players:
        if student not in cricket_players:
            either_play.append(student)
    return either_play

# Function to find number of students who play neither cricket nor badminton
def neither_cricket_nor_badminton(total_students, cricket_players, badminton_players):
    neither_play = []
    for student in total_students:
        if student not in cricket_players and student not in badminton_players:
            neither_play.append(student)
    return len(neither_play)

# Function to find number of students who play cricket and football but not badminton
def cricket_and_football_not_badminton(cricket_players, football_players, badminton_players):
    cricket_football_not_badminton = []
    for student in cricket_players:
        if student in football_players and student not in badminton_players:
            cricket_football_not_badminton.append(student)
    return len(cricket_football_not_badminton)

# Function to find number of students who do not play any game
def not_play_any_game(total_students, cricket_players, badminton_players, football_players):
    not_play_any = []
    for student in total_students:
        if student not in cricket_players and student not in badminton_players and student not in football_players:
            not_play_any.append(student)
    return len(not_play_any)

# Function to find list of students who play at least one game
def play_at_least_one_game(cricket_players, badminton_players, football_players):
    at_least_one_game = []
    for student in cricket_players:
        if student not in at_least_one_game:
            at_least_one_game.append(student)
    for student in badminton_players:
        if student not in at_least_one_game:
            at_least_one_game.append(student)
    for student in football_players:
        if student not in at_least_one_game:
            at_least_one_game.append(student)
    return at_least_one_game

# Function to find list of students who play all three games
def play_all_three_games(cricket_players, badminton_players, football_players):
    all_three_games = []
    for student in cricket_players:
        if student in badminton_players and student in football_players:
            all_three_games.append(student)
    return all_three_games

# Sample data
cricket_players = ['A', 'B', 'C', 'D']
badminton_players = ['B', 'C', 'E', 'F']
football_players = ['C', 'D', 'E', 'G']
total_students = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# Test the functions
print("a) Students who play both cricket and badminton:", both_cricket_badminton(cricket_players, badminton_players))
print("b) Students who play either cricket or badminton but not both:", either_cricket_or_badminton(cricket_players, badminton_players))
print("c) Number of students who play neither cricket nor badminton:", neither_cricket_nor_badminton(total_students, cricket_players, badminton_players))
print("d) Number of students who play cricket and football but not badminton:", cricket_and_football_not_badminton(cricket_players, football_players, badminton_players))
print("e) Number of students who do not play any game:", not_play_any_game(total_students, cricket_players, badminton_players, football_players))
print("f) List of students who play at least one game:", play_at_least_one_game(cricket_players, badminton_players, football_players))
print("g) List of students who play all three games:", play_all_three_games(cricket_players, badminton_players, football_players))