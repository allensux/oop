import threading

sum= 0
loopsum = 1000000

def myAdd():
    global sum, loopsum
    for i  in range(1, loopsum):
        sum += 1
    print("Add{0}".format(sum))

def myMinu():
    global sum, loopsum
    for i in range(1, loopsum):
        sum -= 1
    print("Minu{0}".format(sum))

def main():
    print("Starting...{0}".format(sum))

    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("ALL Done...{0}".format(sum))

if __name__ == '__main__':
    main()

