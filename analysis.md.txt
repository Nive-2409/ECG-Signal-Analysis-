
# ECG Signal Analysis System — Project Analysis

## 1. Introduction

The ECG Signal Analysis System is a Python-based
biomedical engineering project that analyzes a simulated
electrocardiogram (ECG) signal.

An ECG records the electrical activity of the heart.
This project generates a simulated ECG waveform,
detects R-peaks, calculates heart rate, and displays
the waveform graphically.

The project demonstrates the application of data
structures, algorithms, and basic signal processing
in biomedical engineering.

## 2. Objectives

- To generate a simulated ECG signal.
- To detect R-peaks in the ECG waveform.
- To calculate heart rate in beats per minute (BPM).
- To calculate RR intervals between consecutive peaks.
- To display the ECG waveform using a graph.
- To understand the application of DSA in biomedical
  signal analysis.

## 3. Tools and Technologies

- Programming language: Python
- NumPy: Numerical calculations and array operations
- Matplotlib: ECG waveform visualization
- Development environment: Python IDLE
- Version control and project hosting: GitHub

## 4. Methodology

The system follows these steps:

1. Generate a simulated ECG signal for a specified
   duration and heart rate.
2. Store the time values and signal amplitudes in arrays.
3. Scan the signal to identify local maximum points.
4. Select candidate peaks whose amplitude exceeds
   a predefined threshold.
5. Apply a minimum distance between detected peaks
   to reduce duplicate detections.
6. Calculate the RR intervals between consecutive peaks.
7. Calculate average heart rate using the RR intervals.
8. Display signal statistics and plot the ECG waveform
   with detected R-peaks.

## 5. Algorithm

Step 1: Start the program.

Step 2: Set the sampling rate, duration, and simulated
        heart rate.

Step 3: Generate the ECG waveform using mathematical
        functions representing P, Q, R, S, and T waves.

Step 4: Add a small amount of simulated noise.

Step 5: Scan the signal samples to detect local maxima
        above the selected threshold.

Step 6: Apply the minimum peak distance condition.

Step 7: Store the detected peak indices.

Step 8: Calculate RR intervals between consecutive peaks.

Step 9: Calculate average heart rate using:

        Heart Rate (BPM) = 60 / Average RR Interval

Step 10: Display the calculated statistics.

Step 11: Plot the ECG signal and detected R-peaks.

Step 12: Stop the program.

## 6. Data Structures Used

### Arrays

Arrays store the time samples, ECG amplitudes, and
detected peak indices.

Advantages:
- Efficient storage of numerical data.
- Easy access to signal samples using indices.
- Convenient processing using NumPy.

### List

A Python list stores the detected R-peak indices
during the scanning process.

Advantages:
- Dynamic size.
- Easy insertion of detected peak indices.
- Simple sequential access.

## 7. Algorithms Used

### Linear Scanning

The algorithm examines the ECG samples one by one
to identify local maxima above a threshold.

### Peak Detection

A sample is considered a candidate R-peak when its
amplitude exceeds the threshold and it is greater
than its neighboring samples.

### RR Interval Calculation

The difference between consecutive R-peak times
gives the RR interval.

RR Interval = Current Peak Time - Previous Peak Time

### Heart Rate Calculation

The mean RR interval is used to estimate heart rate.

Heart Rate (BPM) = 60 / Mean RR Interval in seconds

## 8. Time Complexity Analysis

Let n represent the number of ECG samples and k
represent the number of detected R-peaks.

### ECG Signal Generation

Each signal sample is updated for a fixed number
of wave components per heartbeat.

For a fixed number of heartbeats and wave components,
the generation process is approximately O(n).

### R-Peak Detection

The algorithm scans each sample once.

Time Complexity: O(n)

### RR Interval Calculation

The algorithm calculates differences between
consecutive detected peaks.

Time Complexity: O(k)

### Heart Rate Calculation

The mean of the RR intervals is calculated.

Time Complexity: O(k)

### Overall Analysis

For the peak detection and interval calculation
stages, the total time complexity is O(n + k),
which simplifies to O(n) because k cannot exceed n.

The storage complexity is O(n) because the signal
and time arrays contain n samples.

## 9. Test Cases

### Test Case 1: Normal Simulated Heart Rate

Input:
- Simulated heart rate: 75 BPM
- Duration: 10 seconds
- Sampling rate: 250 Hz

Expected result:
- An ECG waveform is generated.
- R-peaks are detected.
- The calculated heart rate should be close to
  the simulated heart rate, subject to detection accuracy.

### Test Case 2: Lower Simulated Heart Rate

Input:
- Simulated heart rate: 55 BPM

Expected result:
- The program generates a slower simulated waveform.
- The rate flag should indicate a value below 60 BPM
  if the calculated rate is below that threshold.

### Test Case 3: Higher Simulated Heart Rate

Input:
- Simulated heart rate: 110 BPM

Expected result:
- The program generates a faster simulated waveform.
- The rate flag should indicate a value above 100 BPM
  if the calculated rate exceeds that threshold.

### Test Case 4: Short Signal

Input:
- A signal duration too short to contain at least
  two detected R-peaks.

Expected result:
- The program should report insufficient R-peaks
  to calculate heart rate.

Note: These are planned test cases. Run each case and
record the actual output before reporting the results
as verified.

## 10. Applications

- Biomedical engineering education.
- Learning basic ECG signal characteristics.
- Demonstrating peak detection algorithms.
- Understanding heart rate and RR interval calculations.
- Introducing programming-based biomedical signal analysis.

## 11. Limitations

- The program uses simulated ECG data rather than
  real patient recordings.
- The peak detector uses a simple amplitude threshold.
- Noise and waveform variations may cause missed or
  incorrectly detected peaks.
- The algorithm has not been clinically validated.
- Heart rate flags are not medical diagnoses.

## 12. Future Enhancements

- Analyze real ECG recordings from an open dataset.
- Implement a more robust R-peak detection algorithm.
- Add filtering to reduce noise and baseline drift.
- Display heart rate trends over time.
- Add a graphical user interface.
- Compare detected peaks with annotated reference data.

## 13. Conclusion

The ECG Signal Analysis System demonstrates how Python,
data structures, and basic algorithms can be applied
to biomedical signal processing.

The project generates a simulated ECG waveform,
detects candidate R-peaks, calculates RR intervals,
estimates heart rate, and visualizes the signal.

It provides a foundation for understanding ECG analysis
and can be extended using real recordings and more
advanced signal-processing techniques.
