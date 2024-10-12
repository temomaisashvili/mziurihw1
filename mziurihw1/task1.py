def capitalize(word):
    vowels = 'aeiou'
    result = ''
    for i in word:
        if i in vowels:
            result += i.upper()
        else:
            result += i
    return result


print(capitalize('hello'))
