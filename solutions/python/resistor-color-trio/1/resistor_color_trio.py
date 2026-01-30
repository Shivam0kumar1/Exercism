import string
COLOR_CODE = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
    }
def label(colors):
    ohms = "".join(str(COLOR_CODE[colors[i]]) for i in range(0,2))
    # str(COLOR_CODE[colors[0]]) if colors[0] != "0" + str(COLOR_CODE[colors[1]]) if colors[1]!="0"
    if colors[2]=="black" and ohms.count("0")==2:
        return "0 ohms"
    elif colors[2]=="black":
        ohms = ohms.replace("0","")
        return f"{ohms} ohms"
    for i in range(1,COLOR_CODE[colors[2]]+1):
        ohms+="0"
    ohms+= " ohms"
    if ohms.count("0")>6:
        ohms = ohms.replace("000000000","").replace("ohms","gigaohms")
    elif ohms.count("0")==6:
        ohms = ohms.replace("000000","").replace("ohms","megaohms")
    elif "000" in ohms:
        ohms = ohms.replace("000","").replace("ohms","kiloohms")
    return ohms
    
        
