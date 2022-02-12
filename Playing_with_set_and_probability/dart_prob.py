from math import pi

def dart_prob(r, t):
    area = pi * r ** 2
    probs =  []
    for i in range(t):
        prob = area / (2 * r) ** 2
        probs.append(prob)
    p = sum(probs)/t
    return area, p

if __name__ == "__main__":
    r = int(input('Radius: '))
    t = int(input("Throws: "))
    area, p = dart_prob(r, t)
    print("Area: ", area, "Estimated (", t, " darts): ", p)