def quota(valid_votes, seats_available):
    """
    Working with the Quota, that function calculates the number of votes a candidate needs to be elected.
    
    :param valid_votes: Number of valid votes
    :param seats_available: number of available seats
    :return: 
    """
    result = (valid_votes / (seats_available + 1)) + 1
    return round(result)

def read_data(filepath):
    """"
    Using that function you are able to read STV counting problem data
    and return the number of candidates, the available seats and the voting data.
    """
    compiled = re.compile("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?")
    election_data = []
    with open(filepath) as f:
        for line in f.read().splitlines():
            line_data = [int(x) for x in line.split() if compiled.match(x) and int(x) != 0]
            if line_data:
                election_data.append(line_data)
    num_candidates = election_data[0][0] - len(election_data[1])
    available_seats = election_data[0][1]
    final_election_data = []
    for i in range(len(election_data)):
        l = election_data[i]
        if i == 0 or i == 1:
            continue
        else:
            if len(l) > num_candidates + 1:
                final_election_data.append(l[0:num_candidates + 1])
            else:
                final_election_data.append(l)
    return num_candidates, available_seats, final_election_data

def valid_votes(election_data):
    """
    The following function receives a list of lists (election data)
    and returns the number of valid votes
    :param election_data: election data
    :return:
    """
    valid_votes = 0
    for data in election_data:
        valid_votes += data[0]
    return valid_votes
