import re

def convert_to_number(s):
    """
    Convert a string representation of a number with 'k' or 'm' suffix to its numeric value.

    Args:
        s (str or float): The input value to convert. Can be a string with 'k' (thousands)
                          or 'm' (millions) suffix, or a numeric value.

    Returns:
        float: The numeric value of the input.

    Examples:
        >>> convert_to_number('5.3k')
        5300.0
        >>> convert_to_number('2m')
        2000000.0
        >>> convert_to_number('100')
        100.0
        >>> convert_to_number(50)
        50.0
    """
     # Checking if the input is a string
    if isinstance(s, str):
        s = s.lower()
        # Using regex to match the number and optional suffix
        match = re.match(r"([0-9\.]+)([km]?)", s)
        if match:
            # Extracting the numeric part and convert to float
            number = float(match.group(1))
            # Extracting the suffix (if any)
            suffix = match.group(2)
            # Converting based on the suffix
            if suffix == "k":
                return number * 1_000
            elif suffix == "m":
                return number * 1_000_000
            else:
                return number # No suffix, return as is
        else:
            # If input is not a string, convert it to float
            return float(s)