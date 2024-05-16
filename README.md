# Recursive-Packet-Distribution-Calculator

## Description
This Python script calculates all possible distributions of `M` packets across `T` time slots. It uses a recursive function `packets_arrived` to explore every possible combination. This functionality is useful in scenarios such as networking, where understanding the distribution of packets over time can impact system performance.

## Getting Started

### Dependencies
- Python 3.x

### Installing
- No additional libraries are required, just a Python interpreter.

### Executing Program
- Run the script using Python.
- Input the number of time slots (`T`) and the number of packets (`M`) when prompted.
- The script outputs all possible combinations of distributing the packets across the given time slots.

```bash
python packets_distribution.py
```

## Output
The script displays all possible packet arrival patterns and the total number of potential outcomes. Each outcome is presented as a separate line showing the distribution across the given time slots.

## Authors
Saroj Raj

## Version History
- 0.1
    - Initial Release
