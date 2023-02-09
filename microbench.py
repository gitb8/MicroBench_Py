import time

# set run repetitions
RUNS = 65536

def func1(): pass       # demo function

def func2(): pass       # demo function

# bench setup

a = 0

# /bench setup

start = time.perf_counter_ns()
for run in range(RUNS):
    # 1st run

    a += 1
    # a += 2      # reverse test

    # bench functions
    # func1()
    # func2()     # reverse test

    # /1st run
end = time.perf_counter_ns()
first = float(end - start)

# reset bench

a = 0

# /reset bench

start = time.perf_counter_ns()
for run in range(RUNS):
    # 2nd run

    a += 2
    # a += 1      # reverse test

    # bench functions
    # func2()
    # func1()     # reverse test

    # /2nd run
end = time.perf_counter_ns()
second = float(end - start)

# print result nanoseconds
# print("1st run: ", first / float(RUNS), " ns", )
# print("2nd run: ", second / float(RUNS), " ns", )

# print result microseconds
print("1st run: ", first / float(RUNS) / 1000.0, " µs", )
print("2nd run: ", second / float(RUNS) / 1000.0, " µs", )

# print result milliseconds
# print("1st run: ", first / float(RUNS) / 1.0e6, " ms", )
# print("2nd run: ", second / float(RUNS) / 1.0e6, " ms", )

# print result milliseconds
# print("1st run: ", first / float(RUNS) / 1.0e9, " s", )
# print("2nd run: ", second / float(RUNS) / 1.0e9, " s", )
