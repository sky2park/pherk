import sys

ofile = open(sys.argv[1], "r")
lines = ofile.readlines()
ofile.close()

ifile = open("Editted-" + sys.argv[1], "w")

for line in lines:
    newline = line
    if "SW_SPST" in line or "SW_Push" in line:
        items = line.split(",")

        # JLCPCB origin is at bottom-left with axes growing up and right.

        # rotate 180
        items[5] = "180.0"

        # move up by 150mil
        y = float(items[4]) + 2.54 + 1.27
        ytxt = "{:.4f}".format(y)
        items[4] = ytxt

        # move right by 25mil
        x = float(items[3]) - 1.27/2
        xtxt = "{:.4f}".format(x)
        items[3] = xtxt

        # Edit layer from top to bottom
        items[6] = "bottom\n"

        newline = ",".join(items)

    elif "R_Pack" in line:
        items = line.split(",")

        # Remove rotation from 0603x4 resistor array
        items[5] = "0.0"

        newline = ",".join(items)

    elif "74HC165" in line:
        items = line.split(",")

        # Rotate by 90 from what it is by default
        items[5] = "90.0"

        newline = ",".join(items)

    ifile.write(newline)

ifile.close()
