COLOR_CODE = {
    "black": 0, "brown": 1, "red": 2, "orange": 3,
    "yellow": 4, "green": 5, "blue": 6, "violet": 7,
    "grey": 8, "white": 9
}

MULTIPLIER = {
    "black": 1, "brown": 10, "red": 100, "orange": 1_000,
    "yellow": 10_000, "green": 100_000, "blue": 1_000_000,
    "violet": 10_000_000, "grey": 100_000_000, "white": 1_000_000_000,
    "gold": 0.1, "silver": 0.01
}

TOLERANCE = {
    "grey": "±0.05%", "violet": "±0.1%", "blue": "±0.25%",
    "green": "±0.5%", "brown": "±1%", "red": "±2%",
    "gold": "±5%", "silver": "±10%"
}

def format_value(value):
    """Format resistance into ohms, kiloohms, or megaohms with clean decimals."""
    if value >= 1_000_000:
        val = value / 1_000_000
        unit = "megaohms"
    elif value >= 1_000:
        val = value / 1_000
        unit = "kiloohms"
    else:
        val = value
        unit = "ohms"

    # Ensure val is float for consistency
    val = float(val)

    # Format: no trailing zeros, no unnecessary decimals
    if val.is_integer():
        return f"{int(val)} {unit}"
    else:
        return f"{val:.2f}".rstrip("0").rstrip(".") + f" {unit}"

def resistor_label(colors):
    n = len(colors)

    # One-band resistor
    if n == 1 and colors[0] == "black":
        return "0 ohms"

    # Four-band resistor
    if n == 4:
        d1 = COLOR_CODE[colors[0]]
        d2 = COLOR_CODE[colors[1]]
        multiplier = MULTIPLIER[colors[2]]
        tolerance = TOLERANCE[colors[3]]
        value = (d1 * 10 + d2) * multiplier
        return f"{format_value(value)} {tolerance}"

    # Five-band resistor
    if n == 5:
        d1 = COLOR_CODE[colors[0]]
        d2 = COLOR_CODE[colors[1]]
        d3 = COLOR_CODE[colors[2]]
        multiplier = MULTIPLIER[colors[3]]
        tolerance = TOLERANCE[colors[4]]
        value = (d1 * 100 + d2 * 10 + d3) * multiplier
        return f"{format_value(value)} {tolerance}"

    raise ValueError("Invalid resistor band configuration")