import pyspectrum_ as ps
c = ps.Colors()
red = c.RGB(255, 0, 0)
green = c.RGB(0, 255, 0)
blue = c.RGB(0, 0, 255)
yellow = c.RGB(255, 255, 0)
gr = c.combine_colors([blue, yellow])
print(gr.to_rgb().to_tuple())











