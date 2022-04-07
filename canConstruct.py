def canConstruct(target, wordbank):
    if target == '':
        return [[]]
    if target == None:
        return [[]]

    result = []

    for word in wordbank:
        print(word)
        if target.startswith(word):
            print('yes it starts with -->', word)
            suffix = target[len(word):]
            print('sufx -->', suffix)
            suffixWays = canConstruct(suffix, wordbank)
            print('suffixways -->', suffixWays)
            list(map((lambda x: x.insert(0, word)), suffixWays))
            print('suffixways -->', suffixWays)
            result.extend(suffixWays)

    return result

print(canConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
