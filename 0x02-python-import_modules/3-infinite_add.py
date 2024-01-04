#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    
    # Convert arguments to integers and sum them
    result = sum(map(int, args))
    
    print(result)
