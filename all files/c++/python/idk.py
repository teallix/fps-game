def check_valid_note(note):
    if not note:
        return True

    if note.endswith("."):
        return check_valid_note(note[:-1])

    if note[0] in [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'p', 'a#', 'b#', 'c#', 'd#', 'e#', 'f#', 'g#'
    ]:
        return check_valid_note(note[1:])

    if note[0].isdigit():
        length = note[0]
        while len(note) > 1 and note[1].isdigit():
            length += note[1]
            note = note[1:]
        if int(length) in [1, 2, 4, 8, 16, 32]:
            if len(note) > 1 and note[1].isdigit() and int(note[1]) in [1, 2, 3, 4, 5, 6, 7, 8]:
                return check_valid_note(note[2:])
            elif len(note) >1 and note[1] == '#':
                return check_valid_note(note[2:])
            else:
                return check_valid_note(note[1:])
    
    return False

#used for manual testing purpose
if __name__ == "__main__":
    print(check_valid_note('4a8'))
    print(check_valid_note('16b5'))# 
    print(check_valid_note('32c4'))
    print(check_valid_note('e7'))# 
    print(check_valid_note('f2')) 
    print(check_valid_note('d#'))#  
    print(check_valid_note('16p'))  
    print(check_valid_note('p'))    
    print(check_valid_note('f.'))   
    print(check_valid_note('32a#8.'))#