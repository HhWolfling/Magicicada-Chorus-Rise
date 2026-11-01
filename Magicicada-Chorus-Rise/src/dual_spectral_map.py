import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

def analyze_and_plot_spectral_map(file1_path, file2_path):
    print("Loading audio files...")
    # Load audio files (mono, 22050 Hz)
    y1, sr1 = librosa.load(file1_path, sr=22050, duration=60)
    y2, sr2 = librosa.load(file2_path, sr=22050, duration=60)

    # Compute Short-Time Fourier Transform (STFT)
    D1 = np.abs(librosa.stft(y1))
    D2 = np.abs(librosa.stft(y2))

    # Calculate mean frequency spectrum
    freqs = librosa.fft_frequencies(sr=sr1)
    mean_spec1 = np.mean(D1, axis=1)
    mean_spec2 = np.mean(D2, axis=1)

    # Normalize spectra for comparison
    mean_spec1 /= np.max(mean_spec1)
    mean_spec2 /= np.max(mean_spec2)

    # Set up styling (Dark Hadal Obsidian theme)
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(14, 8), facecolor='#05050A')
    ax = fig.add_subplot(111)
    ax.set_facecolor('#05050A')

    # Plot Track 1 Spectrum (Kinetic Vector - Pink/Cyan)
    ax.plot(freqs, mean_spec1, color='#FF007F', alpha=0.85, linewidth=1.8, 
            label='Track 1: Interconnectedness (Transient Vector)')
    ax.fill_between(freqs, mean_spec1, color='#FF007F', alpha=0.15)

    # Plot Track 2 Spectrum (Ground Vector - Amber/Emerald)
    ax.plot(freqs, -mean_spec2, color='#00FFCC', alpha=0.85, linewidth=1.8, 
            label='Track 2: Instar Emergence (Grounded Vector)')
    ax.fill_between(freqs, -mean_spec2, color='#00FFCC', alpha=0.15)

    # Highlight the 64 - 67 Hz (C2 / Helmholtz Resonance) Zone
    c2_idx = np.where((freqs >= 60) & (freqs <= 70))[0]
    ax.axvspan(64, 67, color='#FFD700', alpha=0.35, label='65.41 Hz (C2) Helmholtz Core')
    ax.axvline(x=65.41, color='#FFD700', linestyle='--', linewidth=1.5)

    # Add geometric polar grid overlay simulation (Lie Group Root projection aesthetic)
    theta = np.linspace(0, 2*np.pi, 100)
    r_max = 1.0
    for r in [0.25, 0.5, 0.75, 1.0]:
        circle_x = r * 1000 * np.cos(theta) + 500
        circle_y = r * np.sin(theta)
        ax.plot(circle_x, circle_y, color='#1A2B4C', linestyle=':', alpha=0.4)

    # Logarithmic scale for frequency clarity
    ax.set_xscale('log')
    ax.set_xlim(20, 10000)
    ax.set_ylim(-1.1, 1.1)

    # Annotations and Labels
    ax.set_title("DUAL SPECTRAL LIE GROUP PLANE ($G_2 / E_8$ PROJECTION)\nFrequency Resonance Comparison", 
                 color='#00FFCC', fontsize=14, pad=20, fontweight='bold')
    ax.set_xlabel("Frequency (Hz) [Logarithmic]", color='#8A9BA8', fontsize=11)
    ax.set_ylabel("Normalized Magnitude Vector", color='#8A9BA8', fontsize=11)

    # Custom Grid & Axes
    ax.grid(True, which="both", ls="-", color='#121C2B', alpha=0.6)
    ax.annotate('65.41 Hz Peak\n(Low C2 Anchor)', xy=(65.41, 0.8), xytext=(120, 0.9),
                arrowprops=dict(facecolor='#FFD700', shrink=0.05, width=1, headwidth=6),
                color='#FFD700', fontsize=10, fontweight='bold')

    ax.legend(loc='upper right', facecolor='#0A0A14', edgecolor='#1A2B4C')
    plt.tight_layout()
    plt.savefig("dual_spectral_lie_map.png", dpi=300, facecolor=fig.get_facecolor())
    print("Map generated and saved as 'dual_spectral_lie_map.png'")
    plt.show()

# Run script with your file paths
analyze_and_plot_spectral_map(
    "Cicada 3301_ Interconnectedness.mp3", 
    "Cicada 3301 - The Instar Emergence.mp3"
)