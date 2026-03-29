goals_dict = dict()
# Process data for a player name and the list of goals for that player.
def process_data(name, goals_string):
    goals_list = goals_string.split(',')
    goals_set = set(goals_list)

    if goals_dict.get(name):
        goals_dict[name].update(goals_set)
    else:
        goals_dict[name] = goals_set

# Main code - process the file and populate goals_dict with all the info.
with open('data.txt') as fh:
    for name in fh:
        name = name.rstrip('\r\n')
        goals_string = fh.readline().rstrip('\r\n')
        process_data(name, goals_string)

# Display the goal-scoring pattern for each player.
for k,v in goals_dict.items():
    print("%s\t%s" % (k, v))