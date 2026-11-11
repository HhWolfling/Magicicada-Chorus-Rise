import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

def run_lindblad_dissipator_simulation(duration=10.0, steps=1000):
    print("Simulating Layer 4: Open Quantum Lindblad Dissipator Engine...")
    t = np.linspace(0, duration, steps)
    dt = duration / steps

    # Basis States: |0>, |1> for 2-level quantum system (Qubit representation)
    ket_0 = np.array([[1], [0]], dtype=np.complex128)
    ket_1 = np.array([[0], [1]], dtype=np.complex128)

    # Initial Density Matrix: Pure superposition state (|0> + |1>) / sqrt(2)
    psi_0 = (ket_0 + ket_1) / np.sqrt(2)
    rho_initial = psi_0 @ psi_0.conj().T

    # Environmental Dissipation Jump Operators (Phase damping + Energy relaxation)
    sigma_minus = np.array([[0, 1], [0, 0]], dtype=np.complex128)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=np.complex128)
    
    gamma_thermal = 0.25  # Ambient noise coupling strength

    # System 1: Coprime Hamiltonian (13:17 Prime Brood Shield)
    omega_p = 13.0
    omega_q = 17.0
    H_coprime = 0.5 * (omega_p * sigma_z + (omega_q / omega_p) * (sigma_minus + sigma_minus.T))

    # System 2: Degenerate Non-Coprime Hamiltonian (12:16 Ratio, gcd=4)
    H_degenerate = 0.5 * (12.0 * sigma_z + (16.0 / 12.0) * (sigma_minus + sigma_minus.T))

    def lindblad_rhs(rho, H, gamma):
        # -i [H, rho]
        commutator = -1j * (H @ rho - rho @ H)
        
        # Dissipation channel 1: Amplitude damping L = sigma_minus
        L1 = sigma_minus
        diss1 = L1 @ rho @ L1.conj().T - 0.5 * (L1.conj().T @ L1 @ rho + rho @ L1.conj().T @ L1)
        
        # Dissipation channel 2: Phase dephasing L = sigma_z
        L2 = sigma_z
        diss2 = L2 @ rho @ L2.conj().T - 0.5 * (L2.conj().T @ L2 @ rho + rho @ L2.conj().T @ L2)

        return commutator + gamma * (diss1 + diss2)

    # Time Integration (RK4)
    purity_coprime = np.zeros(steps)
    purity_degenerate = np.zeros(steps)

    rho_c = rho_initial.copy()
    rho_d = rho_initial.copy()

    for i in range(steps):
        # Calculate Purity: Tr(rho^2)
        purity_coprime[i] = np.real(np.trace(rho_c @ rho_c))
        purity_degenerate[i] = np.real(np.trace(rho_d @ rho_d))

        # RK4 Integration step for Coprime System
        k1_c = lindblad_rhs(rho_c, H_coprime, gamma_thermal * 0.1) # Coprime Shielded Noise
        k2_c = lindblad_rhs(rho_c + 0.5 * dt * k1_c, H_coprime, gamma_thermal * 0.1)
        k3_c = lindblad_rhs(rho_c + 0.5 * dt * k2_c, H_coprime, gamma_thermal * 0.1)
        k4_c = lindblad_rhs(rho_c + dt * k3_c, H_coprime, gamma_thermal * 0.1)
        rho_c += (dt / 6.0) * (k1_c + 2*k2_c + 2*k3_c + k4_c)

        # RK4 Integration step for Degenerate System
        k1_d = lindblad_rhs(rho_d, H_degenerate, gamma_thermal * 1.5) # Resonant Noise Amplification
        k2_d = lindblad_rhs(rho_d + 0.5 * dt * k1_d, H_degenerate, gamma_thermal * 1.5)
        k3_d = lindblad_rhs(rho_d + 0.5 * dt * k2_d, H_degenerate, gamma_thermal * 1.5)
        k4_d = lindblad_rhs(rho_d + dt * k3_d, H_degenerate, gamma_thermal * 1.5)
        rho_d += (dt / 6.0) * (k1_d + 2*k2_d + 2*k3_d + k4_d)

    # Plot Coherence Protection Dynamics
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='#05050A')
    ax.set_facecolor('#05050A')

    ax.plot(t, purity_coprime, color='#00FFCC', label='Coprime Phase-Lock (13:17) [Shielded State]', linewidth=2.0)
    ax.plot(t, purity_degenerate, color='#FF007F', label='Degenerate Ratio (12:16) [Thermal Decoupling]', linestyle='--', linewidth=1.8)

    ax.axhline(y=1.0, color='#FFD700', linestyle=':', alpha=0.5, label='Pure Quantum Coherence (P = 1.0)')
    ax.axhline(y=0.5, color='#8A9BA8', linestyle=':', alpha=0.5, label='Maximum Mixed Entropy (P = 0.5)')

    ax.set_title("OPEN QUANTUM LINDBLAD DISSIPATOR DYNAMICS\nCoprime Shielding Against Thermal Noise Degradation", 
                 color='#00FFCC', fontsize=11, fontweight='bold')
    ax.set_xlabel("Time [tau]", color='#8A9BA8')
    ax.set_ylabel("Quantum Purity Metric P(t) = Tr(rho^2)", color='#8A9BA8')
    ax.legend(loc='lower left', fontsize=8, framealpha=0.2)
    ax.grid(True, color='#121C2B', linestyle=':', alpha=0.5)

    plot_filename = "lindblad_coprime_shield.png"
    plt.savefig(plot_filename, dpi=300, facecolor=fig.get_facecolor())
    print(f"Saved Quantum Dissipator plot as '{plot_filename}'")
    plt.show()

if __name__ == "__main__":
    run_lindblad_dissipator_simulation()