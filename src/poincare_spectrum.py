import numpy as np
import matplotlib.pyplot as plt
import librosa

def analyze_poincare_disk(file1_path, file2_path):
    print("Computing Poincaré Hyperbolic Disk projections...")
    # Load audio
    y1, sr1 = librosa.load(file1_path, sr=22050, duration=30)
    y2, sr2 = librosa.load(file2_path, sr=22050, duration=30)

    # Compute FFT
    D1 = np.abs(librosa.stft(y1))
    D2 = np.abs(librosa.stft(y2))

    freqs = librosa.fft_frequencies(sr=sr1)
    spec1 = np.mean(D1, axis=1)
    spec2 = np.mean(D2, axis=1)

    # Normalize
    spec1 /= np.max(spec1)
    spec2 /= np.max(spec2)

    # Filter frequencies between 20 Hz and 10,000 Hz
    valid_idx = np.where((freqs >= 20) & (freqs <= 10000))[0]
    f_sub = freqs[valid_idx]
    s1_sub = spec1[valid_idx]
    s2_sub = spec2[valid_idx]

    # Map frequencies to radial distance r in [0, 1) using log scale
    # Low frequencies (65 Hz) -> r near 0 (center)
    # High frequencies (10 kHz) -> r near 1 (boundary)
    r = (np.log10(f_sub) - np.log10(20)) / (np.log10(10000) - np.log10(20))

    # Assign polar angles theta: Track 1 on upper hemisphere, Track 2 on lower
    N = len(r)
    theta1 = np.linspace(0.1, np.pi - 0.1, N)
    theta2 = np.linspace(np.pi + 0.1, 2*np.pi - 0.1, N)

    # Setup Polar Plot
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(10, 10), facecolor='#05050A')
    ax = fig.add_subplot(111, projection='polar')
    ax.set_facecolor('#05050A')

    # Draw Poincaré Disk Boundary
    boundary_theta = np.linspace(0, 2*np.pi, 200)
    ax.plot(boundary_theta, np.ones_like(boundary_theta), color='#00E5FF', linewidth=2, alpha=0.8)

    # Plot Track 1 (Upper Hemisphere - Kinetic Spikes)
    ax.plot(theta1, r, color='#FF007F', linewidth=1, alpha=0.5, label='Track 1 Geodesic Paths')
    scatter1 = ax.scatter(theta1, r, c=s1_sub, cmap='spring', s=s1_sub*80, alpha=0.9, label='Track 1 Power Density')

    # Plot Track 2 (Lower Hemisphere - Grounded Core)
    ax.plot(theta2, r, color='#00FFCC', linewidth=1, alpha=0.5, label='Track 2 Geodesic Paths')
    scatter2 = ax.scatter(theta2, r, c=s2_sub, cmap='viridis', s=s2_sub*80, alpha=0.9, label='Track 2 Power Density')

    # Highlight 65.41 Hz Core Resonance at Center (r ~ 0.19)
    r_c2 = (np.log10(65.41) - np.log10(20)) / (np.log10(10000) - np.log10(20))
    ax.plot(boundary_theta, np.full_like(boundary_theta, r_c2), color='#FFD700', linestyle='--', linewidth=1.5)
    ax.scatter([0], [0], color='#FFD700', s=250, zorder=5, label='65.41 Hz (C2) Core Origin')

    # Custom Polar Grid Aesthetics
    ax.set_rticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(['65 Hz', '200 Hz', '650 Hz', '2.5 kHz', '10 kHz'], color='#8A9BA8', fontsize=8)
    ax.grid(True, color='#121C2B', linestyle=':', alpha=0.7)

    plt.title("HYPERBOLIC POINCARÉ DISK SPECTRUM ($\mathbb{D}^2$ CONFORMAL MAP)\nCore Resonance ($r=0$) vs Boundary Transients ($r \\to 1$)", 
              color='#00FFCC', fontsize=13, fontweight='bold', pad=25)

    ax.legend(loc='lower right', facecolor='#0A0A14', edgecolor='#1A2B4C', bbox_to_anchor=(1.15, 0.0))

    plt.tight_layout()
    plt.savefig("poincare_disk_spectrum.png", dpi=300, facecolor=fig.get_facecolor())
    print("Saved Poincaré plot as 'poincare_disk_spectrum.png'")
    plt.show()

# Run
analyze_poincare_disk(
    "Cicada 3301_ Interconnectedness.mp3", 
    "Cicada 3301 - The Instar Emergence.mp3"
)
