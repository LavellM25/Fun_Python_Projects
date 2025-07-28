def caesar_decode(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            # Shift character backwards
            base = ord('A')
            shifted = (ord(char) - base - shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

message = "HTSLWFYZQFYNTSX DJW QJFWSNSL UDYMTS"
decoded = caesar_decode(message, 5)
print(decoded)
