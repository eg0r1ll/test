import requests # python -m pip install requests


def rabin_karp_search(text, pattern): # Robin Karp's algorithm
    pattern_hash = hash(pattern)
    window_hash = hash(text[:len(pattern)])

    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == window_hash and text[i:i + len(pattern)] == pattern:
            return i
        window_hash = hash(text[i + 1:i + len(pattern) + 1])
    return None


# I found this in the HTML code (https://yandex.ru/pogoda)
patternTemp = "AppFactTemperature_value"
patternPlusMinus = "AppFactTemperature_sign__1MeN4 AppFactTemperature_attr__8pcxc"

while True:
    location = input("location: ").lower()
    if location == "exit" or location == "quit": break

    request = requests.get(f"https://yandex.ru/pogoda/ru/{location}") # get the page markup
    data = request.text[70000:75000:1] # cut off the excess
    del request

    # Get the index where the pattern match was found:
    temperature_idx = rabin_karp_search(data, patternTemp)
    sign_idx = rabin_karp_search(data, patternPlusMinus)
    
    if temperature_idx:
        # search for temperature value:
        temperature = data[temperature_idx+33:temperature_idx+35:1] # for a two-digit number
        if not temperature[-1].isdigit():
            temperature = data[temperature_idx+33:temperature_idx+34:1] # for a single digit number

        # get the sign before the temperature (+/- or if zero then nothing):
        if temperature != '0':
            sign = data[sign_idx+63:sign_idx+64:1]
        else:
            sign = ''

        print(f"It's {sign}{temperature}° in {location.capitalize()} now") # output

    else:
        print("Location not found :(")