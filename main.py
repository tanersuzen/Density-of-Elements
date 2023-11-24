import periodictable
from periodictable import elements, formula, chemicals

for el in periodictable.elements:
    print(el.name,el.symbol,el.number)
while True:
    symbol_element = formula(input ("enter symbol for detail info: "))

    print (f"{symbol_element},Density: {symbol_element.density} g/cm3")