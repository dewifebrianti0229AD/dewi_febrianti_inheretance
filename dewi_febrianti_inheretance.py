class Hewan(object):
    def __init__(self, a, b, c):
        self.ayam = a
        self.burung = b
        self.cicak = c

    def cetakData(self):
        print("ayam\t: ", self.ayam)
        print("burung\t: ", self.burung)
        print("cicak\t: ", self.cicak)


# kelas turunan (subclass)
class Hewandomba(Hewan):
    def __init__(self, a, b, c, d, ):
        self.ayam = a
        self.burung = b
        self.cicak = c
        self.domba = d

    def cetakData(self):
        print("ayam\t: ", self.ayam)
        print("burung\t: ", self.burung)
        print("cicak\t: ", self.cicak)
        print("domba\t: ", self.domba)


def main():
    # membuat objek Hewandomba
    Hewan1 = Hewan(1, 2, 3)
    Hewandomba1 = Hewandomba(1, 2, 3, "4")

    # menggunakan objek
    print('Hewan')
    Hewan1.cetakData()
    print(' ')
    print('Domba')
    Hewandomba1.cetakData()


if __name__ == "__main__":
    main()

