market_2nd_signals = {
    "north_west" : "green",
    "south-west" : "red" 
}

def switch_lights(dict):
    if dict["north_west"] == "green":
        dict["north_west"] = "yellow"
    if dict['south-west'] == "red":
            dict['south-west' ] = "green"
    assert 'red' in dict.values(), 'Neighter light is red'        
            
print(market_2nd_signals)
switch_lights(market_2nd_signals)
print(market_2nd_signals)            