def vowelsToUpper(string_to_convert):
    vowels = {"a", "e", "i", "o", "u"}
    newString = ""

    for letters in string_to_convert:
        if letters in vowels:
            capitalString = letters.upper()
            newString += capitalString
        else:
            newString += letters

    return newString


string = "vowels to upper"
capitalizedString = vowelsToUpper(string)
print("Initial string", string)
print("With vowelsToUpper:", capitalizedString)

