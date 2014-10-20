"""Roman numerals implementation.

Examples
--------
>>> Roman('I') + 5 == Roman('VI')
True

"""


__author__ = 'Vladimir Keleshev'
__author_email__ = 'vladimir@keleshev.com'
__version__ = '0.1.0'


_numerals = {'I': 1, 'V': 5, 'X': 10}


class Roman(int):

    """Roman numeral.

    >>> Roman('I') == 1
    True

    """

    def __new__(class_, roman):
        """Create integer from a string representing Roman numeral.

        Parameters
        ----------
        roman : string
          A string representing Roman numeral.

        Returns
        -------
        n : Roman
          A number that represents the Roman numeral.

        Raises
        ------
        ValueError
          In case ``roman`` does not represent a valid Roman numeral.

        Example
        -------
        >>> Roman('XVI')
        16

        """
        try:
            return sum(_numerals[digit] for digit in roman)
        except KeyError:
            raise ValueError('Invalid Roman numeral %r' % roman)
