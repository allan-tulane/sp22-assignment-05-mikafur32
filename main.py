####### Problem 3 #######

test_cases = [('book', 'back'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA'), ('kookaburra', 'kookybird')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant', '-elephant'), ('AAAGAATTCA', 'AAA---T-CA')]


def MED(S, T):
    if (S == ""):
        return (len(T))
    elif (T == ""):
        return (len(S))
    else:
        if (S[0] == T[0]):
            return (MED(S[1:], T[1:]))
        else:
            return (1 + min(MED(S, T[1:]), MED(S[1:], T), MED(S[1:], T[1:])))


def fast_MED(S, T):
    def pad(x, y):
        # pad with leading 0 if x/y have different number of bits
        # e.g., [1,0] vs [1]
        pad_length = 0
        pad_bool = True
        if len(x) < len(y):
            pad_length = (len(y) - len(x))
            pad_bool = True
            x = x + '0' * pad_length
        elif len(y) < len(x):
            pad_length = (len(x) - len(y))
            pad_bool = False
            y = y + '0' * pad_length
        return x, y, pad_length, pad_bool

    S, T, pad_length, pad_bool = pad(S, T)

    memo_arr = [[0 for n in range(len(S))] for m in range(len(T))]

    for i in range(len(S)):
        for j in range(len(T)):
            if i == 0:
                memo_arr[i][j] = j

            elif j == 0:
                memo_arr[i][j] = i
            else:
                if S[i] == T[j]:
                    memo_arr[i][j] = memo_arr[i - 1][j - 1]
                else:
                    memo_arr[i][j] = 1 + min(memo_arr[i - 1][j - 1], memo_arr[i][j - 1], memo_arr[i - 1][j])
    # format_arr(memo_arr,S,T)

    if pad_bool:
        # print(((len(S) - pad_length - 1), len(T) - 1))
        return memo_arr[len(S) - pad_length - 1][len(T) - 1]  # TODO verify

    else:
        # print(((len(S) - 1), len(T) - pad_length - 1))
        return memo_arr[len(S) - 1][len(T) - pad_length - 1]  # TODO verify


def format_arr(arr, S, T):
    print(list(T))
    for i in range(len(arr)):
        print((S[i]), arr[i])


def fast_MED_arr(S, T):
    def pad(x, y):
        # pad with leading 0 if x/y have different number of bits
        # e.g., [1,0] vs [1]
        pad_length = 0
        pad_bool = True
        if len(x) < len(y):
            pad_length = (len(y) - len(x))
            pad_bool = True
            x = x + '0' * pad_length
        elif len(y) < len(x):
            pad_length = (len(x) - len(y))
            pad_bool = False
            y = y + '0' * pad_length
        return x, y, pad_length, pad_bool

    S, T, pad_length, pad_bool = pad(S, T)

    memo_arr = [[0 for n in range(len(S))] for m in range(len(T))]

    for i in range(len(S)):
        for j in range(len(T)):
            if i == 0:
                memo_arr[i][j] = j

            elif j == 0:
                memo_arr[i][j] = i
            else:
                if S[i] == T[j]:
                    memo_arr[i][j] = memo_arr[i - 1][j - 1]
                else:
                    memo_arr[i][j] = 1 + min(memo_arr[i - 1][j - 1], memo_arr[i][j - 1], memo_arr[i - 1][j])
    # format_arr(memo_arr,S,T)
    return memo_arr


def fast_align_MED(S, T):
    # fast med traveerse back from the memoTable
    # if up, append S original, append - to T
    # if down, append T original, append - to S
    # always choose up if both are equal
    arr = fast_MED_arr(S, T)
    alignS, alignT = '',''

    i = len(S) - 1
    j = len(T) - 1
    while i >= 0:
        while j >= 0:
            x = arr[i][j - 1]  #up
            y = arr[i - 1][j - 1] #diag
            z = arr[i - 1][j] # left
            if z <= x and z <= y:
                alignS = S[i] + alignS
                alignT = "-" + alignT
                #go left
                i -= 1

            elif y <= x and y <= z:
                alignS = S[i] + alignS
                alignT = T[j] + alignT

                # go diagonal
                i -= 1
                j -= 1

            elif x <= y and x <= z:
                # go up
                alignS = '-' + alignS
                alignT = T[j] + alignT
                j -= 1







    return alignS, alignT


def test_MED():
    for S, T in test_cases:
        print(fast_MED(S, T))
        print(MED(S, T))
        assert fast_MED(S, T) == MED(S, T)


def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])


for i in test_cases:
    print(fast_align_MED(i[0], i[1]))

#print(fast_align_MED('kookaburra', 'kookybird'))
