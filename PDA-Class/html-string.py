def HTMLToString(file_path):
    result = ""
    tagStack = []
    text = False

    with open(file_path, 'r') as file:
        content = file.read()

        for char in content:
            if char == '<':
                tagStack.append(char)
            elif char == '>':
                tagStack.pop()
                text = False
            elif len(tagStack) == 0 and char in [' ', '\t', '\n']:
                continue
            else:
                if char == ' ':
                    if spasi:
                        continue
                    else:
                        spasi = True
                else:
                    spasi = False
            
            if text and len(tagStack) == 0 and (char not in ["<", ">"]):
                continue

            if len(tagStack) == 0 and (char not in ["<", ">"]):
                text= True

            result += char

    return result