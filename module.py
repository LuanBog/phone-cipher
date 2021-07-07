layout = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

def encode(text, delimiter=' '):
    decoded_text = []

    text = text.lower()

    for letter in text:
        for key, value in layout.items():
            for index, let in enumerate(value):
                if let == letter:
                    amount_to_be_repeated = index + 1
                    result = key * amount_to_be_repeated    

                    decoded_text.append(result)

                    continue
                        
    return delimiter.join(decoded_text)

# "text" should always be seperated with a space and a string
def decode(text, delimiter=' '):
    decoded_text = ''
    splitted = text.split(delimiter)

    for number in splitted:
        single_number = number[0]
        times_repeated = len(number) - 1
        layout_group = layout[single_number] 

        letter = layout_group[times_repeated]
        decoded_text = decoded_text + letter

    return decoded_text
