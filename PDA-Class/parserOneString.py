def HTMLToString(file_path):
    result = ""
    inTag = False
    spasi = False

    with open(file_path, 'r') as file:
        content = file.read()

        for char in content:
            if char == '<':
                inTag = True
            elif char == '>':
                inTag = False
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

            result += char

    return result

print(HTMLToString('a.html'))