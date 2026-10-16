def main():
    hi = loop()
    while hi != 30:
        print(next(hi))



def loop():
    x = 10
    x = yield x
    if x != 20:
        loop()

main()