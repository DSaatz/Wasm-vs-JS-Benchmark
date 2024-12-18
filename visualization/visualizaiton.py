import matplotlib.pyplot as plt


#the execution times of of the i+1th fibonacci number for i = 0, 1, 2, ..., 40 using JS and WASM in milliseconds

wasmTimes = [
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  1,
  0,
  0,
  1,
  1,
  1,
  2,
  3,
  5,
  9,
  15,
  23,
  42,
  59,
  96,
  163,
  217,
  363,
  572,
  917
]

jsTimes = [
  1,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  1,
  1,
  1,
  3,
  4,
  8,
  13,
  24,
  39,
  66,
  112,
  161,
  234,
  376,
  631,
  957,
  1502,
  2397
]

#plotting the data
plt.plot(wasmTimes, label="WASM")
plt.plot(jsTimes, label="JS")
plt.xlabel("Fibonacci Number")
plt.ylabel("Execution Time (ms)")
plt.title("Execution Time of Fibonacci Numbers")
plt.legend()
plt.show()
