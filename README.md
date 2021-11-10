# pyspectrum
### a small, multi-use color library for python
### supports RGB, Hexadecimal, Decimal, CMYK and most web colors (`red`, `seagreen`, `yellow`)
## Quickstart
### Installation
Using `pip` to install is highly reccomended</br>

`pip install -U pyspectrum`</br>
### Examples
```py
import pyspectrum
# init colors
c = pyspectrum.Colors()
# creating color classes out of values
redRGB = c.RGB(255, 0, 0)
redHex = c.Hexadecimal("#ff0000")
redCMYK = c.CMYK(0, 100, 100, 0)
# converting values
convertedCMYK = redRGB.to_cmyk()
convertedHex = redRGB.to_hex()





