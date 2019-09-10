import re


def main():
    f = open("1.txt")
    f2 = open("2.txt", "a+")
    while True:
        data = ""
        for i in f:
            if i != "\n":
                data += i
            else:
                break
        print(data)
        if not data:
            break
        one_word = re.match(r"\S+", data).group()
        print(one_word)
        pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\S{1,6}"
        pattern1 = r"\w{4}\.\w{4}\.\w{4}"
        addr = re.findall(pattern, data)
        addr1 = re.findall(pattern1, data)
        print(addr)
        print(addr1)
        if addr == [] or addr1 == []:
            f2.write("%s : '' \n" % one_word)
        else:
            f2.write("%s : %s :%s\n" % (one_word, addr[0], addr1[0]))

if __name__=="__main__":
    main()