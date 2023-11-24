def HTMLToString(file_path):
    result = ""
    inTag = False

    with open(file_path, 'r') as file:
        content = file.read()

        for char in content:
            if char == '<':
                result += char
                inTag = True
            elif char == '>':
                result += char
                inTag = False
            elif not inTag and char in [' ', '\t', '\n']:
                continue
            else:
                result += char

    return result