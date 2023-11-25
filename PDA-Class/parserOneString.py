def HTMLToString(file_path):
    result = ""
    inTag = False
    spasi = False
    text = False

    with open(file_path, 'r') as file:
        content = file.read()

        for char in content:
            if char == '<':
                inTag = True
            elif char == '>':
                inTag = False
                text = False
            elif not inTag and char in [' ', '\t', '\n']:
                continue
            else:
                if char == ' ':
                    if spasi:
                        continue
                    else:
                        spasi = True
                else:
                    spasi = False
            
            if text and not inTag and (char not in ["<", ">"]):
                continue

            if not inTag and (char not in ["<", ">"]):
                text= True

            result += char

    return result
