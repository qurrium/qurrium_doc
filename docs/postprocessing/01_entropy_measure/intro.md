# Entanglement Entropy by Different Methods

1. [Hadamard Test](./1_hadamard.ipynb)
2. Randomized Measurement
   a. [Randomized Measurement](./2a_randomized_measure.ipynb)
   b. [Randomized Measurement with Error Mitigation](./2b_randomized_measure.ipynb)
3. Classical Shadow (Documentation in progress)
4. Randomized Measurement V1 - the deprecated version
   a. [Randomized Measurement](./4a_randomized_measure_v1.ipynb)
   b. [Randomized Measurement with Error Mitigation](./4b_randomized_measure_v1.ipynb)
   - This method is deprecated, and we recommend **not** using it for post-processing except when dealing with data from versions **below `0.9.1`**
   - `EntropyRandomizedMeasureV1` is a deprecated version of `EntropyRandomizedMeasure` because it lacks clarity on the relationship between bitstrings and qubit indices. This limitation can easily cause confusion, especially when working with systems that do not measure all qubits. However, it is retained for backward compatibility.
