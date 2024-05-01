import periodictable

def get_element_info(symbol):
    if not periodictable.elements.symbol(symbol):
        print("Invalid element symbol")
        return
    element = periodictable.elements.symbol(symbol)

    print(f"Element: {element.name}")
    print(f"Symbol: {element.symbol}")
    print(f"Atomic number: {element.number}")
    print(f"Atomic mass: {element.mass}")
    print(f"Density: {element.density}")

element_symbol = input("Enter the symbol of the element: ")
get_element_info(element_symbol)
