import numpy as np
import matplotlib.pyplot as plt
import librosa

def compute_phase_space(file_path, tau=12, max_samples=150000):
    # Load audio segment
    y, sr = librosa.load(file_path, sr=22050, duration=15)
    
    # Subsample for clean trajectory plotting
    y = y[:max_samples]
    
    # Delay embedding x(t) vs x(t + tau)
    x_t = y[:-tau]
    x_tau = y[tau:]
    return x_t, x_tau

def plot_dual_phase_space(file1_path, file2_path):
    print("Computing delay embeddings...")
    x1, x1_tau = compute_phase_space(file1_path)
    x2, x2_tau = compute_phase_space(file2_path)

    # Styling Setup
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), facecolor='#05050A')

    # Panel 1: Track 1 Attractor (Kinetic/Chaotic)
    ax1.set_facecolor('#05050A')
    ax1.plot(x1, x1_tau, color='#FF007F', alpha=0.35, linewidth=0.5, label='Track 1 Transient Loop')
    ax1.scatter(x1[::50], x1_tau[::50], color='#00E5FF', s=1.5, alpha=0.6, label='Phase Vector Nodes')
    ax1.set_title("TRACK 1: KINETIC PHASE ATTRACTOR\n$x(t)$ vs $x(t + \\tau)$", 
                  color='#FF007F', fontsize=12, fontweight='bold', pad=12)
    ax1.set_xlabel("$x(t)$ Amplitude", color='#8A9BA8')
    ax1.set_ylabel("$x(t + \\tau)$ Delay Vector", color='#8A9BA8')
    ax1.grid(True, color='#121C2B', linestyle='--', alpha=0.5)
    ax1.legend(loc='upper right', facecolor='#0A0A14', edgecolor='#1A2B4C')
    ax1.set_aspect('equal')

    # Panel 2: Track 2 Attractor (Grounded Torus)
    ax2.set_facecolor('#05050A')
    ax2.plot(x2, x2_tau, color='#00FFCC', alpha=0.35, linewidth=0.5, label='Track 2 Grounded Torus')
    ax2.scatter(x2[::50], x2_tau[::50], color='#FFD700', s=1.5, alpha=0.6, label='$65.41$ Hz Resonance Lock')
    ax2.set_title("TRACK 2: GROUNDED PHASE ATTRACTOR\n$x(t)$ vs $x(t + \\tau)$", 
                  color='#00FFCC', fontsize=12, fontweight='bold', pad=12)
    ax2.set_xlabel("$x(t)$ Amplitude", color='#8A9BA8')
    ax2.set_ylabel("$x(t + \\tau)$ Delay Vector", color='#8A9BA8')
    ax2.grid(True, color='#121C2B', linestyle='--', alpha=0.5)
    ax2.legend(loc='upper right', facecolor='#0A0A14', edgecolor='#1A2B4C')
    ax2.set_aspect('equal')

    plt.suptitle("PHASE-SPACE RECURRENCE ATTRACTOR ANALYSIS\nTakens' Embedding Metric ($\tau = 0.54\text{ ms}$)", 
                 color='#00FFCC', fontsize=14, fontweight='bold', y=0.98)

    plt.tight_layout()
    plt.savefig("phase_space_attractors.png", dpi=300, facecolor=fig.get_facecolor())
    print("Saved plot as 'phase_space_attractors.png'")
    plt.show()

# Execute analysis
plot_dual_phase_space(
    "Cicada 3301_ Interconnectedness.mp3", 
    "Cicada 3301 - The Instar Emergence.mp3"
)