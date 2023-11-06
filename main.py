
from drawtool import drawSquare as dt

def main():
    doc, msp = dt.create_document()
    point = [0, 0]
    dt.create_drawing(doc, msp, point)
    doc.saveas("draw_border.dxf")


if __name__ == "__main__":
    main()
