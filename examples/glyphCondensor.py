# robothon 2009
# Get started with a condensed if you have a regular and a bold:
#	seperate x, y interpolation to make stems fatter
#	then scaling to reduce width
#	stems will get their original thickness

from robofab.world import CurrentFont
f = CurrentFont()

# these are measurements you have to take
# from your font. The width of a stem.
lightStem = 106
fatStem = 200

for i in range(0, 10):
	factor = (i*.1, 0)
	print factor
	name = "result_%f"%factor[0]
	scale = float(41)/(41 + factor[0]*(116-41))
	print scale
	f[name].interpolate(factor, f["A"], f["B"])
	f[name].scale((scale, 1))
	f[name].leftMargin = f["A"].leftMargin
	f[name].rightMargin = f["A"].rightMargin
		
f.update() 