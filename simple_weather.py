import requests


def rabin_karp_search(text, pattern):
    pattern_hash = hash(pattern)
    window_hash = hash(text[:len(pattern)])

    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == window_hash and text[i:i + len(pattern)] == pattern:
            return i
        window_hash = hash(text[i + 1:i + len(pattern) + 1])
    return None


graduse = '°'
patternTemp = "AppFactTemperature_value"
patternPlusMinus = "AppFactTemperature_sign__1MeN4 AppFactTemperature_attr__8pcxc"

while True:
    location = input("location: ").lower()
    r = requests.get(f"https://yandex.ru/pogoda/ru/{location}")
    data = r.text

    temperature_idx = rabin_karp_search(data, patternTemp)
    sign_idx = rabin_karp_search(data, patternPlusMinus)
    
    if temperature_idx:
        temperature = data[temperature_idx+33:temperature_idx+35:1]
        if not temperature[-1].isdigit():
            temperature = data[temperature_idx+33:temperature_idx+34:1]

        if temperature != '0':
            sign = data[sign_idx+63:sign_idx+64:1]
        else:
            sign = ''

        print(f"It's {sign}{temperature}{graduse} in {location.capitalize()} now")

    else:
        print("Местоположение не найденно :(")