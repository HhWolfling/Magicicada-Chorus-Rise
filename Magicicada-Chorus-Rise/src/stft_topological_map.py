import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

def plot_spectrogram_heatmap(file1_path, file2_path):
    print("Computing STFT Spectrogram Heatmaps...")
    # Load 30 seconds of audio
    y1, sr1 = librosa.load(file1_path, sr=22050, duration=30)
    y2, sr2 = librosa.load(file2_path, sr=22050, duration=30)

    # Compute STFT magnitude in dB
    D1 = librosa.amplitude_to_db(np.abs(librosa.stft(y1)), ref=np.max)
    D2 = librosa.amplitude_to_db(np.abs(librosa.stft(y2)), ref=np.max)

    # Setup figure
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 9), facecolor='#05050A', sharex=True)

    # Panel 1: Track 1 Heatmap
    ax1.set_facecolor('#05050A')
    img1 = librosa.display.specshow(D1, sr=sr1, x_axis='time', y_axis='log', ax=ax1, cmap='magma')
    ax1.axhline(y=65.41, color='#FFD700', linestyle='--', linewidth=1.5, alpha=0.85)
    ax1.set_title("TRACK 1: INTERCONNECTEDNESS — SPECTRAL TOPOLOGY (MAGMA MAPPING)", 
                  color='#FF007F', fontsize=12, fontweight='bold', pad=10)
    ax1.set_ylabel("Frequency (Hz) [Log]", color='#8A9BA8')
    ax1.set_ylim(20, 10000)
    fig.colorbar(img1, ax=ax1, format="%+2.0f dB", label="Power (dB)")

    # Panel 2: Track 2 Heatmap
    ax2.set_facecolor('#05050A')
    img2 = librosa.display.specshow(D2, sr=sr2, x_axis='time', y_axis='log', ax=ax2, cmap='viridis')
    ax2.axhline(y=65.41, color='#FFD700', linestyle='--', linewidth=1.5, alpha=0.85)
    ax2.set_title("TRACK 2: THE INSTAR EMERGENCE — SPECTRAL TOPOLOGY (VIRIDIS MAPPING)", 
                  color='#00FFCC', fontsize=12, fontweight='bold', pad=10)
    ax2.set_xlabel("Time (Seconds)", color='#8A9BA8')
    ax2.set_ylabel("Frequency (Hz) [Log]", color='#8A9BA8')
    ax2.set_ylim(20, 10000)
    fig.colorbar(img2, ax=ax2, format="%+2.0f dB", label="Power (dB)")

    # Annotate the shared core line
    ax1.text(1.0, 72, "  65.41 Hz (C2 Anchor)", color='#FFD700', fontweight='bold', fontsize=9)
    ax2.text(1.0, 72, "  65.41 Hz (C2 Anchor)", color='#FFD700', fontweight='bold', fontsize=9)

    plt.suptitle("SPECTROGRAM TOPOLOGICAL HEATMAP ANALYSIS\nTime-Frequency Energy Distribution & $C_2$ Harmonic Floor", 
                 color='#00FFCC', fontsize=14, fontweight='bold', y=0.98)

    plt.tight_layout()
    plt.savefig("spectrogram_topological_heatmap.png", dpi=300, facecolor=fig.get_facecolor())
    print("Saved heatmap as 'spectrogram_topological_heatmap.png'")
    plt.show()

# Execute script
plot_spectrogram_heatmap(
    "Cicada 3301_ Interconnectedness.mp3", 
    "Cicada 3301 - The Instar Emergence.mp3"
)