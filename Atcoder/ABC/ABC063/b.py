def main():
    S = input()
    if len(list(S)) == len(list(set(list(S)))):
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()