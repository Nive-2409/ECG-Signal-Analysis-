
import numpy as np
import matplotlib.pyplot as plt

# ECG SIGNAL ANALYSIS SYSTEM
# Educational project using simulated ECG data

def generate_ecg(duration=10, sampling_rate=250, heart_rate=75):
    """Generate a simulated ECG waveform."""

    t = np.arange(0, duration, 1 / sampling_rate)
    signal = np.zeros(len(t))

    rr_interval = 60 / heart_rate
    beat_times = np.arange(0.5, duration, rr_interval)

    # Create P, Q, R, S and T waves for every heartbeat
    waves = [
        (-0.20,  0.12, 0.040),  # P wave
        (-0.045, -0.15, 0.012), # Q wave
        (0.000,  1.00, 0.015),  # R peak
        (0.040, -0.25, 0.015),  # S wave
        (0.250,  0.35, 0.070)   # T wave
    ]

    for beat in beat_times:
        for offset, amplitude, width in waves:
            signal += amplitude * np.exp(
                -0.5 * ((t - (beat + offset)) / width) ** 2
            )

    # Add a small amount of simulated noise
    rng = np.random.default_rng(42)
    signal += rng.normal(0, 0.015, len(signal))

    return t, signal


def detect_r_peaks(signal, sampling_rate, threshold=0.5):
    """Detect R peaks using threshold and local maximum checks."""

    peaks = []
    min_distance = int(0.30 * sampling_rate)

    for i in range(1, len(signal) - 1):
        is_local_maximum = (
            signal[i] > signal[i - 1]
            and signal[i] >= signal[i + 1]
        )

        if is_local_maximum and signal[i] > threshold:
            if not peaks or i - peaks[-1] >= min_distance:
                peaks.append(i)
            elif signal[i] > signal[peaks[-1]]:
                # Keep the larger peak if two candidates
                # occur too close together
                peaks[-1] = i

    return np.array(peaks, dtype=int)


def analyze_ecg(t, signal, sampling_rate):
    """Calculate heart rate and basic signal statistics."""

    peaks = detect_r_peaks(signal, sampling_rate)

    print("\n========== ECG ANALYSIS REPORT ==========")
    print(f"Signal duration: {t[-1]:.2f} seconds")
    print(f"Sampling rate: {sampling_rate} Hz")
    print(f"Detected R peaks: {len(peaks)}")

    if len(peaks) >= 2:
        rr_intervals = np.diff(t[peaks])
        heart_rate = 60 / np.mean(rr_intervals)

        print(f"Average heart rate: {heart_rate:.2f} BPM")
        print(f"Mean RR interval: {np.mean(rr_intervals):.3f} seconds")

        if heart_rate < 60:
            print("Rate flag: Below 60 BPM")
        elif heart_rate > 100:
            print("Rate flag: Above 100 BPM")
        else:
            print("Rate flag: Within 60-100 BPM")

        print("Note: Rate flags are educational, not diagnoses.")

    else:
        print("Insufficient R peaks to calculate heart rate.")

    print(f"Mean signal amplitude: {np.mean(signal):.4f}")
    print(f"Maximum amplitude: {np.max(signal):.4f}")
    print(f"Minimum amplitude: {np.min(signal):.4f}")
    print("=========================================")

    # Plot the ECG waveform and detected R peaks
    plt.figure(figsize=(12, 5))
    plt.plot(t, signal, label="ECG Signal", linewidth=1)
    plt.plot(
        t[peaks],
        signal[peaks],
        "ro",
        label="Detected R Peaks"
    )

    plt.title("ECG Signal Analysis System")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude (arbitrary units)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


def main():
    sampling_rate = 250

    t, signal = generate_ecg(
        duration=10,
        sampling_rate=sampling_rate,
        heart_rate=75
    )

    analyze_ecg(t, signal, sampling_rate)


if __name__ == "__main__":
    main()
