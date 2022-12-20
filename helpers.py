"""A few helpful fanctions that feel out of place in other files."""


def hex_to_rgb(code):
    """Simple function to convert Hex RGB to numeric RGB.

    Args:
        code (str): hex RGB code

    Raises:
        ValueError: if the code is invalid

    Returns:
        List: numeric RGB code
    """
    try:
        code = str(code).strip('#')
        r = code[0:2]
        g = code[2:4]
        b = code[4:6]
        r = int(r, base=16)
        g = int(g, base=16)
        b = int(b, base=16)
    except ValueError as err:
        raise ValueError(f"Invalid hex code: {err}")
    else:
        return [r, g, b]
