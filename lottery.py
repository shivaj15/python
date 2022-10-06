#!/usr/bin/python

numbers = 6
max  = 49
file = open("output.txt", "a" )

a, b, c, d, e, f  = 0, 1, 2, 3, 4, 5

while a < 45:
    while b < 46:
        while c < 47:
            while d < 48:
                while e < 49:
                    while f < 50:
                        file.write(str(a) + "\t" + str(b) + "\t"  + str(c) + "\t" + str(d) + "\t" + str(e) + "\t" + str(f) + "\n")
                        #x = a, b, c, d, e, f
                        #file.write(str(x) + "\n")
                        f += 1

                    e += 1
                    f = e + 1

                d += 1
                e = d + 1

            c += 1
            d = c + 1

        b += 1
        c = b + 1

    a += 1
    b = a + 1

file.close()