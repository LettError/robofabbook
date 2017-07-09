# robothon 2009
# get the parent object for a glyph

from robofab.world import CurrentFont

font = CurrentFont()

glyph = font["A"]
print glyph.getParent()

