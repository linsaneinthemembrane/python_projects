morse_dict: dict[str: str] = {"A": ". -", "B": "- . . .", "C": "- . - .", "D": "- . .", "E": ".", "F": ". . - .", "G": "- - .", "H": ". . . .", "I": ". .", "J": ". - - -", "K": "- . -", "L": ". - . .", "M": "- -", "N": "- .", "O": "- - -", "P": ". - - .", "Q": "- - . -",
                              "R": ". - .", "S": ". . .", "T": "-", "U": ". . -", "V": ". . . -", "W": ". - -", "X": "- . . -", "Y": "- . - -", "Z": "- - . .", "1": ". - - - -", "2": ". . - -", "3": ". . . - -", "4": ". . . . -", "5": ". . . . .", "6": "- . . . .", "7": "- - . . .", "8": "- - - . .", "9": "- - - - .", "0": "- - - - -", " " : " "}

go = True
sentence = input("Enter a sentence: ")

while go == True:
    upper_sentence = sentence.upper()
    for i in range(len(upper_sentence)):
        trans_letter = morse_dict[upper_sentence[i]]
        print(trans_letter, end = "")
    print("")
    blehbleh = input("Would you like to enter another sentence? ")
    if blehbleh == "no":
        go = False