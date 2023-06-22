palindrom = "frdbrf"
ne_palindrom = "crab"


def test_palindrom(word: str) -> bool: 
    """
    Проверка слова (str) на палиндром
    """

    symbols = []

    for symbol in word:
        symbols.append(symbol)

    if len(symbols) % 2 == 1:

        start_i = 0
        end_i = len(symbols) - 1

        for i in symbols:

            q = symbols[end_i]

            if start_i != end_i:
                print(i, q)
                if i != q:
                    print(i)
                    return False
                else:
                    start_i += 1
                    end_i -= 1

            else:
                return True
            
    elif len(symbols) % 2 == 0:

        start_i = 0
        end_i = len(symbols) - 1

        for i in symbols:

            q = symbols[end_i]

            if end_i - start_i != 1:
                if i != q:
                    return False
                else:
                    start_i += 1
                    end_i -= 1
            else:
                return True
            
print(test_palindrom(palindrom))

# Сложнее чем показалось на самом деле.