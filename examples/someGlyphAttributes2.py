# robothon 2009
# set basic attributes in a glyph

from robofab.world import CurrentFont

font = CurrentFont()
glyph = font['A']

glyph.leftMargin = 50
print glyph.leftMargin
glyph.rightMargin = 50
print glyph.rightMargin

glyph.update()

