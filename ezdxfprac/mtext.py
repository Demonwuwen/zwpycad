import ezdxf

doc = ezdxf.new("R2007", setup=True)
msp = doc.modelspace()

lorem_ipsum = """
{\\C1;Lorem ipsum dolor sit amet, consectetur adipiscing elit,}
{\\C2;sed do eiusmod tempor incididunt ut labore et dolore magna}
{\\C5;aliqua. Ut enim ad minim veniam, quis nostrud exercitation}
{ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia
deserunt mollit anim id est laborum.
"""

# store MTEXT entity for additional manipulations
mtext = msp.add_mtext(lorem_ipsum, dxfattribs={"style": "OpenSans"})


mtext.text += "Append additional text to the MTEXT entity."
# even shorter with __iadd__() support:
mtext += "Append additional text to the MTEXT entity."

doc.saveas("m_text.dxf")