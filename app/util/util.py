from datetime import datetime

"""
0:  Success
1:  Item doesn't exist
2:  Item was created
3:  Category doesn't exist
4:  Category was created
5:  Price can't less than 0
6:  The child category can't be parent
"""


def get_current_timestamp() -> int:
    return int(datetime.timestamp(datetime.now()) * 1000)
