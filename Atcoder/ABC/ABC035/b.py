def main():
    S = list(input())
    T = int(input())
    tmp = [0,0]
    wild = 0
    for i in range(len(S)):
        if S[i] == "L":
            tmp[0] += -1
        if S[i] == "R":
            tmp[0] += 1
        if S[i] == "U":
            tmp[1] += 1
        if S[i] == "D":
            tmp[1] += -1
        if S[i] == "?":
            wild += 1
    tmp = [abs(tmp[0]),abs(tmp[1])]
    if T == 1:
        print(sum(tmp) + wild)
    elif T == 2:
        if sum(tmp) - wild >= 0:
            print(sum(tmp) - wild)
        else:
            if abs(sum(tmp) - wild)%2 == 0:
                print(0)
            else:
                print(1)

if __name__ == '__main__':
    main()