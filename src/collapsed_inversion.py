import numpy as np
import matplotlib.pyplot as plt
import librosa

def analyze_collapsed_inversion(file1_path, file2_path):
    print("Computing Collapsed Inversion Manifold...")
    # Load audio clips
    y1, sr1 = librosa.load(file1_path, sr=22050, duration=30)
    y2, sr2 = librosa.load(file2_path, sr=22050, duration=30)

    # Time-reverse Track 2 (The Instar Emergence)
    y2_reversed = np.flip(y2)

    # Compute STFT
    D1 = np.abs(librosa.stft(y1))
    D2_rev = np.abs(librosa.stft(y2_reversed))

    freqs = librosa.fft_frequencies(sr=sr1)
    s1 = np.mean(D1, axis=1)
    s2_rev = np.mean(D2_rev, axis=1)

    # Normalize
    s1 /= np.max(s1)
    s2_rev /= np.max(s2_rev)

    # Collapsed Sum and Differential
    s_sum = s1 + s2_rev
    s_diff = np.abs(s1 - s2_rev)

    # Setup Styling
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(14, 8), facecolor='#05050A')
    ax = fig.add_subplot(111)
    ax.set_facecolor('#05050A')

    # Plot Collapsed Spectrum Sum (v1(t) + v2(-t))
    ax.plot(freqs, s_sum, color='#00FFCC', linewidth=2.0, alpha=0.9, 
            label='Collapsed Sum: Track 1 + Track 2(-t) [Frictionless Flow]')
    ax.fill_between(freqs, s_sum, color='#00FFCC', alpha=0.15)

    # Plot Differential Residue
    ax.plot(freqs, s_diff, color='#FF007F', linewidth=1.2, linestyle='--', alpha=0.75, 
            label='Differential Residue |v1(t) - v2(-t)|')

    # Highlight 65.41 Hz C2 Anchor
    ax.axvspan(64, 67, color='#FFD700', alpha=0.3, label='65.41 Hz (C2) Prime Brood Origin')
    ax.axvline(x=65.41, color='#FFD700', linestyle='--', linewidth=1.5)

    # Log Scale Settings
    ax.set_xscale('log')
    ax.set_xlim(20, 10000)
    ax.set_ylim(0, 2.2)

    # Annotations
    ax.set_title("COLLAPSED INVERSION MANIFOLD ANALYSIS\nTrack 1 Forward Vector $\mathbf{v}_1(t)$ vs Track 2 Time-Reversed Vector $\mathbf{v}_2(-t)$", 
                 color='#00FFCC', fontsize=13, fontweight='bold', pad=20)
    ax.set_xlabel("Frequency (Hz) [Logarithmic Scale]", color='#8A9BA8', fontsize=11)
    ax.set_ylabel("Collapsed Spectral Amplitude Density", color='#8A9BA8', fontsize=11)

    ax.annotate('13:17 Prime Brood Resonance\n(65.41 Hz Lock)', xy=(65.41, 1.8), xytext=(120, 1.9),
                arrowprops=dict(facecolor='#FFD700', shrink=0.05, width=1, headwidth=6),
                color='#FFD700', fontsize=10, fontweight='bold')

    ax.grid(True, which="both", ls="-", color='#121C2B', alpha=0.6)
    ax.legend(loc='upper right', facecolor='#0A0A14', edgecolor='#1A2B4C')

    plt.tight_layout()
    plt.savefig("collapsed_inversion_manifold.png", dpi=300, facecolor=fig.get_facecolor())
    print("Saved collapsed manifold plot as 'collapsed_inversion_manifold.png'")
    plt.show()

# Run script
analyze_collapsed_inversion(
    "Cicada 3301_ Interconnectedness.mp3", 
    "Cicada 3301 - The Instar Emergence.mp3"
)
