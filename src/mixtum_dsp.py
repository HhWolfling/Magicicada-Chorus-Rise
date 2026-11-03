import numpy as np
import scipy.signal as signal
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

def generate_mixtum_audio(sample_rate=44100, duration=5.0):
    print("Initializing Mixtum Audio DSP Synthesizer Engine...")
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # 1. Generate Signal H (Kinetic Spark): 293.66 Hz + 196.00 Hz with phase modulation
    sig_H = 0.6 * np.sin(2 * np.pi * 293.66 * t + 0.5 * np.cos(2 * np.pi * 13 * t)) + \
            0.4 * np.sin(2 * np.pi * 196.00 * t)

    # 2. Generate Signal C (Structural Ground): 65.41 Hz + 17-Year Prime Brood Modulator
    sig_C = 0.8 * np.sin(2 * np.pi * 65.41 * t) + \
            0.3 * np.sin(2 * np.pi * (65.41 / 2) * t + np.sin(2 * np.pi * 17 * t))

    # 3. Compute STFT (Short-Time Fourier Transform) for both signals
    nperseg = 1024
    f, times, Z_H = signal.stft(sig_H, fs=sample_rate, nperseg=nperseg)
    _, _, Z_C = signal.stft(sig_C, fs=sample_rate, nperseg=nperseg)

    # 4. Apply Non-Linear Commutator Coupling: Phi = [H, C] in Complex Spectral Domain
    # Cross-phase matrix multiplication proxy in STFT space
    Z_HC = Z_H * np.conj(Z_C)
    Z_CH = Z_C * np.conj(Z_H)
    
    # Commutator difference: Phi = H*C - C*H
    Z_Phi = Z_HC - Z_CH

    # Phase-locking scale factor using 13:17 prime brood ratio
    phase_lock_mask = np.exp(1j * (np.angle(Z_H) * 13 - np.angle(Z_C) * 17))
    Z_mixtum = np.abs(Z_Phi) * phase_lock_mask

    # 5. Inverse STFT to rebuild time-domain audio signal
    _, audio_mixtum = signal.istft(Z_mixtum, fs=sample_rate, nperseg=nperseg)

    # Normalize audio output to avoid clipping [-1.0, 1.0]
    audio_mixtum = audio_mixtum / np.max(np.abs(audio_mixtum))

    # Save to 16-bit PCM WAV File
    audio_int16 = np.int16(audio_mixtum * 32767)
    wavfile.write("mixtum_output.wav", sample_rate, audio_int16)
    print("Saved synthesized audio track as 'mixtum_output.wav'")

    # 6. Plot Spectral Analysis of Synthesized Mixtum Track
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), facecolor='#05050A')

    # Time-domain Waveform
    ax1.set_facecolor('#05050A')
    ax1.plot(t[:2000], audio_mixtum[:2000], color='#00FFCC', linewidth=1.2)
    ax1.set_title("MIXTUM SYNTHESIZER: TIME-DOMAIN WAVEFORM (FIRST 45ms)", 
                  color='#00FFCC', fontsize=11, fontweight='bold')
    ax1.set_ylabel("Amplitude", color='#8A9BA8')
    ax1.grid(True, color='#121C2B', linestyle=':', alpha=0.5)

    # Spectrogram Heatmap
    ax2.set_facecolor('#05050A')
    ax2.pcolormesh(times, f[:120], np.abs(Z_mixtum[:120, :]), cmap='magma', shading='gouraud')
    ax2.set_title("SPECTRAL SPECTROGRAM OF THE COMMUTATOR MANIFOLD $\\Phi = [H, C]$", 
                  color='#00FFCC', fontsize=11, fontweight='bold')
    ax2.set_xlabel("Time [seconds]", color='#8A9BA8')
    ax2.set_ylabel("Frequency [Hz]", color='#8A9BA8')

    plt.tight_layout()
    plt.savefig("mixtum_dsp_analysis.png", dpi=300, facecolor=fig.get_facecolor())
    print("Saved DSP analysis plot as 'mixtum_dsp_analysis.png'")
    plt.show()

# Run
generate_mixtum_audio()