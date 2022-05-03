from string import ascii_lowercase as ALPHABETS


def main():
    """Main Program"""
    while True:
        counters = {}
        text = input("Input sentence to display graph! [q to Quit]: ").lower()
        if text == "q":
            print("Bye-bye!")
            break

        print("Chart:")
        for char in text:
            if char in ALPHABETS:
                counters[char] = counters.get(char, 0) + 1

        for char in ALPHABETS:
            if counters.get(char):
                print(f"{char}: {convert(char, counters)}")


def convert(char, counters):
    """Convert counters to graphical chart"""
    return "".join([char for _ in range(counters.get(char))])


if __name__ == "__main__":
    main()
