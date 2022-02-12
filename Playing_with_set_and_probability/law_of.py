from random import randint

def expectation(num_events):
    e = []
    for i in range(num_events):
        e.append(randint(1,6))
    return sum(e)/num_events

if __name__ == "__main__":
    print(expectation(1000))
