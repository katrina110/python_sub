def remove_duplicates(input_str):
    # Ito yung lalagyan ng final na result, yung string na tanggal na
    # yung duplicates
    result = ""

    # Yung seen lalagyan ng letters na hindi duplicate, tapos yung
    # duplicate lalagyan ng mga duplicate malamang
    seen = set()
    duplicate = set()

    # Dito bal yung for na loop inaanalyze nya yung mga laman nung string
    #or yung word
    for char in input_str:
        # Pag yung letter bal or number wala pa sa seen pati hindi sya space
        # malalagay sya dun sa seen
        if char not in seen and char != ' ':
            seen.add(char)
        # Pag nasa seen na sya malalagay sya sa duplicate
        elif char in seen:
            duplicate.add(char)

    # Dito bal ifi filter na ng final yung sagot. Pag yung letter or number
    # sa seen walang katulad sa duplicate, malalagay na sya sa result
    for char in seen:
        if char not in duplicate:
            result += char


    return result

# Ito bal pag nirun mo ibig sabihin mag type ka muna ng number kung ilang
# string yung ilalagay mo
N = int(input())

# Ito bal para i input mo yung mga string base kung ilan yung nilagay mi dun
# sa N
strings = []
for _ in range(N):
    string = input()
    strings.append(string.lower())

# Ito bal para ma print yung final answer
for string in strings:
    modified_string = remove_duplicates(string)
    print(modified_string)
