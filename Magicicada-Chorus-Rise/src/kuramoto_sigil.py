import numpy as np
import matplotlib.pyplot as plt

def generate_kuramoto_and_sigil():
    print("Simulating Kuramoto Phase Coupling & Generating Vector Sigil...")
    
    # 1. Kuramoto Phase Synchronization Simulation
    t = np.linspace(0, 10, 1000)
    # Phase coupling order parameter r(t) growing to phase-lock
    K = 1.8 # Coupling strength above critical threshold
    r_t = 1 - np.exp(-K * t / 2) * np.abs(np.cos(3 * t))
    
    # 2. Polar Sigil Coordinates
    theta = np.linspace(0, 2*np.pi, 1000)
    
    # Sigil 1: 13-Brood Kinetic Rays
    r_sigil1 = 0.8 + 0.15 * np.sin(13 * theta)
    
    # Sigil 2: 17-Brood Grounded Waves
    r_sigil2 = 0.5 + 0.10 * np.cos(17 * theta)
    
    # Setup Figure
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(14, 6), facecolor='#05050A')

    # Panel 1: Kuramoto Order Parameter r(t)
    ax1 = fig.add_subplot(121)
    ax1.set_facecolor('#05050A')
    ax1.plot(t, r_t, color='#00FFCC', linewidth=2.0, label='Phase Coherence $r(t)$ [65.41 Hz]')
    ax1.axhline(y=1.0, color='#FFD700', linestyle='--', linewidth=1.2, label='Complete Phase-Lock (r=1.0)')
    ax1.set_title("KURAMOTO PHASE SYNCHRONIZATION\nCoupling Parameter $r(t)$ Over Time", 
                  color='#00FFCC', fontsize=12, fontweight='bold', pad=15)
    ax1.set_xlabel("Time (s)", color='#8A9BA8')
    ax1.set_ylabel("Order Parameter $r \in [0, 1]$", color='#8A9BA8')
    ax1.set_ylim(0, 1.1)
    ax1.grid(True, color='#121C2B', linestyle=':')
    ax1.legend(loc='lower right', facecolor='#0A0A14', edgecolor='#1A2B4C')

    # Panel 2: Vector Sigil Emblem (Polar Map)
    ax2 = fig.add_subplot(122, projection='polar')
    ax2.set_facecolor('#05050A')

    # Plot Sigil Rays & Arcs
    ax2.plot(theta, r_sigil1, color='#FF007F', linewidth=1.5, label='13-Brood Kinetic Vector')
    ax2.plot(theta, r_sigil2, color='#00FFCC', linewidth=1.5, label='17-Brood Grounded Vector')
    
    # 8-Fold Chladni Star Core (from our 65.41 Hz mode)
    r_star = 0.3 * np.abs(np.sin(4 * theta))
    ax2.plot(theta, r_star, color='#FFD700', linewidth=1.8, label='65.41 Hz Chladni Star')
    ax2.scatter([0], [0], color='#FFD700', s=200, zorder=5)

    ax2.set_title("THE MIXTUM SEAL ($\Phi = [H, C]$)\n13:17 Prime Brood Vector Sigil", 
                  color='#FFD700', fontsize=12, fontweight='bold', pad=20)
    ax2.axis('off')
    ax2.legend(loc='lower right', facecolor='#0A0A14', edgecolor='#1A2B4C', bbox_to_anchor=(1.25, -0.05))

    plt.tight_layout()
    plt.savefig("kuramoto_sigil_synthesis.png", dpi=300, facecolor=fig.get_facecolor())
    print("Saved Kuramoto & Sigil plot as 'kuramoto_sigil_synthesis.png'")
    plt.show()

# Run
generate_kuramoto_and_sigil()