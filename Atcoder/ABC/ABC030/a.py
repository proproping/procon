def main():
    A,B,C,D = map(int,input().split())
    if B/A == D/C:
        print("DRAW")
    elif B/A > D/C:
        print("TAKAHASHI")
    else:
        print("AOKI")

if __name__ == '__main__':
    main()