from commands.request import MarvelRequest
import sys


if __name__ == "__main__":
    """
    :input: limit for request
    :return: void
    
    Creates a csv with the requested dataframe.
    """

    if 1 < len(sys.argv) <= 2:
        try:
            limit = int(sys.argv[1])
            if not 0 > limit > 100:
                print("Outside possible range input")
                limit = 100
        except Exception as e:
            print("Not expected input, using default limit")
            limit = 100
        print(f'Chosen limit: {limit}')
    else:
        limit = 100
        print(f'Default limit: {limit}')
        
    command = MarvelRequest(limit=limit)
    command.get_all_heroes()
    import pdb
    pdb.set_trace()


