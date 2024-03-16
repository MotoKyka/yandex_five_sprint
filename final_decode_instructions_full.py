def decode_string(string: str) -> str:
    stack = []
    current_num: int = 0
    current_string: str = ''

    for letter in string:
        if letter.isdigit():
            current_num = int(str(current_num) + letter)
        elif letter == '[':
            stack.append((current_num, current_string))
            current_num = 0
            current_string = ''
        elif letter == ']':
            num, prev_str = stack.pop()
            current_string = prev_str + num * current_string
        else:
            current_string += letter

    return current_string


if __name__ == '__main__':
    input_instructions = input(f'Введите инструкции: ')
    # Примеры использования
    # print(decode_string("2[с]3[в]ш"))
    # print(decode_string("3[a2[c]]"))
    # print(decode_string("2[abc]3[cd]ef"))
    # print(decode_string("3[a]2[bc]"))
    # print(decode_string("0[abc]3[3[d]cd]ef"))
    # print(decode_string("1[dcd]ef"))
    print(decode_string(input_instructions))
