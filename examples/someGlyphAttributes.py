# robothon 2009
# set basic attributes in a glyph

from robofab.world import CurrentFont

font = CurrentFont()
glyph = font['A']

glyph.width = 200
print glyph.width
print glyph.box

glyph.unicode = 666
print glyph.unicode

glyph.update()