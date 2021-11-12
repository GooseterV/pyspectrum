import pyspectrum_ as ps
import colorsys
c = ps.Colors()
red = c.RGB(255, 0, 0)
green = c.RGB(0, 255, 0)
blue = c.RGB(0, 0, 255)
yellow = c.RGB(255, 255, 0)
print(green.to_hsv().to_tuple())
g = c.combine_colors([blue, yellow])
print(g.to_tuple())
print(g.to_rgb())
gg = colorsys.hsv_to_rgb(0/255, 100/255, 100/255)
print([round(255*cc) for cc in gg])








