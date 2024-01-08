#!/user/bin/python3
"""Module that inverts != and =="""


class MyInt(int):
    """MyInt Class"""

    def __eq__(self, other):
        """Returns !="""
        return super().__ne__(other)

    def __ne__(self, other):
        """Returns =="""
        return super().__eq__(other)
