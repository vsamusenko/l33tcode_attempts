def longcompref(strs):
    if len(strs) < 1: return ''
    if len(strs) == 1: return strs[0]

    short_str = min(strs)
    print(short_str)
    if len(short_str) == 0:
        return ''

    common_pref = ''


    for i in range(len(short_str)):
        print(range(len(short_str)))
        print('index', i)
        for str in strs:
            print('checking str:', str)
            if str[i] == short_str[i]:
                common_pref = short_str[:i]
                print(common_pref)
            else:
                print('else clause')
                return common_pref

        common_pref = short_str[:i+1]



    return common_pref





x = ["a","b"]
print('------------------')
print(longcompref(x))
