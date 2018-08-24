def quota(valid_votes, seats_available):
    """
    Working with the Quota, that function calculates the number of votes a candidate needs to be elected.
    
    :param valid_votes: Number of valid votes
    :param seats_available: number of available seats
    :return: 
    """
    result = (valid_votes / (seats_available + 1)) + 1
    return round(result)
