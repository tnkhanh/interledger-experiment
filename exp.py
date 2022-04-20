#!/usr/bin/python3

import os
import subprocess
import resource
import time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from threading import Thread

alice_cli = "docker run --rm --network local-ilp interledgerrs/ilp-cli --node http://alice-node:7770"

def amount_experiment():

    N = 200 
    times = np.zeros(N) 
    sums = np.zeros(N)
    amt = 0
    for i in range(N):
        command = alice_cli + " pay alice --auth alice_password --amount " + str(amt) + " --to http://charlie-node:7770/accounts/charlie/spsp"
        start_time = time.time()
        subprocess.call(command, shell=True, stdout=subprocess.DEVNULL)
        end_time = time.time()
        elapsed = end_time - start_time
        print("Amount: " + str(amt) + ', elapsed: ' + str(elapsed))
        times[i] = elapsed
        if i==0:
            sums[i] = times[i]
        else:
            sums[i] = sums[i-1] + times[i]
        amt += 10000

    x = np.linspace(0, 2000 * N, N)
#    fig, ax = plt.subplots()
#    ax.plot(x, sums)
#    ax.plot(x, times)

    plt.subplot(1, 2, 1)
    plt.plot(x, times)
    plt.title("Amount-time chart")
    plt.xlabel("Amount(gwei)")
    plt.ylabel("Time(s)")

    plt.subplot(1, 2, 2)
    plt.plot(x, sums)
    plt.title("Total time chart")
    plt.xlabel("Amount(gwei)")
    plt.ylabel("Total time(s)")
    plt.show()


command = alice_cli + " pay alice --auth alice_password --amount 200000 --to http://charlie-node:7770/accounts/charlie/spsp"

def th():
    subprocess.call(command, shell=True)#, stdout=subprocess.DEVNULL)

def latency_experiment():
    N = 5
    times = np.zeros(N)

    f = open("threads_report.txt", "w")
    for i in range(N):
        threads = []
        for j in range(N):
            threads.append(Thread(target=th))

        start_time = time.time()
        for t in threads:
            t.start()

        for t in threads:
            t.join()

        end_time = time.time()
        elapsed = end_time - start_time
        times[i] = elapsed

        print("Threads: " + str(i+1) + ', elapsed: ' + str(elapsed))
        f.write(str(i+1) + ", " + str(elapsed))
        f.write("\n")

        times[i] = elapsed

    f.close()

    x = np.linspace(0, N, N)

    fig, ax = plt.subplots()
    ax.plot(x, times)
    plt.xlabel("Threads")
    plt.ylabel("Time(s)")
    plt.title("ETC-XRP trading in Interledger")
    plt.show()

if __name__ == "__main__":
    amount_experiment()

#    info = resource.getrusage(resource.RUSAGE_CHILDREN)
#    print("real " + str(elapsed))
#    print("user " + str(info.ru_utime))
#    print("system " + str(info.ru_stime))
