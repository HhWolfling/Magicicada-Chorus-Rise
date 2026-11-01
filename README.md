# Magicicada-Chorus-Rise: Dynamic Phase-Locking & Non-Euclidean Acoustic Topology ($\Phi = [H, C]$)

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

An advanced Digital Signal Processing (DSP), Non-Euclidean Geometric, and Phase-Coupling framework designed to analyze, map, and synthesize acoustic tracks beyond standard linear superimposition.

By reframing linear summation ($S_1 + S_2$) into non-linear dynamic commutator coupling ($\Phi = [H, C]$), this engine extracts non-linear entanglement, cross-spectral coherence, time-reversed vector interactions, and physical Chladni nodal geometries.

---

## 🔬 Core Theoretical Framework

Standard audio analysis assumes **separability**—treating overlapping tracks as isolated layers sitting in a room together. The **Magicicada-Chorus-Rise** models audio interactions as an entangled dynamic state vector:

$$\Phi = [\mathbf{v}_1, \mathbf{v}_2] = \mathbf{v}_1 \otimes \mathbf{v}_2^\dagger - \mathbf{v}_2 \otimes \mathbf{v}_1^\dagger$$

- **$\mathbf{v}_1(t)$ (Kinetic Spark $H$)**: Rapid, high-entropy transient vectors (fingerpicking attacks, $3\text{ kHz}-8\text{ kHz}$ air overtones).
- **$\mathbf{v}_2(t)$ (Grounded Anchor $C$)**: Low-entropy, stabilizing mass vectors (acoustic body resonance, low $C_2$ fundamental at $65.41\text{ Hz}$).
- **$\Phi$ (The Emergent *Mixtum* State)**: The non-linear cross-spectral sidebands and phase-locked nodes that exist in neither track individually.

---

## 🎨 Analysis Pipeline & Visual Diagnostics

The repository implements an 8-stage visual and numerical diagnostic pipeline:

1. **Dual Spectral Lie Group Plane ($G_2 / E_8$ Projection)**
   - Maps total spectral power distributions on a flat Lie algebra root system grid.
   - Highlights the core Helmholtz air resonance at **$65.41\text{ Hz}$ ($C_2$)**.

2. **Takens' Delay Embedding Phase-Space Attractor**
   - Reconstructs $x(t) \text{ vs } x(t + \tau)$ phase trajectories ($\tau = 0.54\text{ ms}$).
   - Isolates chaotic transient starbursts from stable, core-focused orbital tori.

3. **Hyperbolic Poincaré Disk Spectrum ($\mathbb{D}^2$)**
   - Conformal mapping where the $65.41\text{ Hz}$ fundamental sits at the hyperbolic center ($r = 0$) and high transients flare toward the boundary circle ($r \to 1$).

4. **Spectrogram Topological Heatmap**
   - Time-frequency Short-Time Fourier Transform (STFT) tracking the continuous $C_2$ floor and parallel harmonic laddering.

5. **Collapsed Inversion Manifold ($\mathbf{v}_1(t) \text{ vs } \mathbf{v}_2(-t)$)**
   - Evaluates the friction-free interaction of running a forward kinetic vector against a time-reversed grounded vector.
   - Models the **13:17 Prime Brood Periodicity** (analogous to prime Magicicada emergence cycles).

6. **Cross-Spectral Density & Coherence ($C_{xy}(f)$)**
   - Quantifies non-linear phase-locking, proving complete cross-phase coupling ($r \to 1.0$) across key harmonic nodes.

7. **2D Chladni Nodal Wave Simulation**
   - Simulates physical sand displacement on vibrating metal plates driven by $65.41\text{ Hz}$ (Mode 2,3) and $293.66\text{ Hz}$ (Mode 5,6).

8. **Kuramoto Order Parameter & Vector Sigil Synthesis**
   - Calculates time-varying phase synchronization $r(t)$ and renders the **13:17 Mixtum Seal** vector emblem.
   
   ## 🌀 Advanced Phase & Physical Manifold Extensions

The engine expands beyond 2D diagnostic representations into 3D physical acoustics, topological braid groups, toroidal manifolds, and fluid shear dynamics:

9. **3D Volumetric Chladni Acoustic Chamber (`src/chladni_3d_volumetric_clean.py`)**
   - Projects standing wave zero-displacement surfaces into 3D spatial volumes ($\mathbb{R}^3$), revealing the floating crystalline nodal lattice held by interfering $C_2$ and harmonic overtones.

10. **Non-Abelian Braid Group Topography ($B_3$) (`src/braid_group_b3.py`)**
    - Maps the phase trajectories of core frequencies ($65.41\text{ Hz}$, $196.00\text{ Hz}$, $293.66\text{ Hz}$) as interlocking fiber-optic strands obeying the braid generator word $w = \sigma_1 \sigma_2^{-1} \sigma_1 \sigma_2^{-1}$.

11. **Prime Residue Modular Torus Manifold ($\mathbb{T}^2$) (`src/prime_torus_manifold.py`)**
    - Wraps the phase-locked trajectories modulo the prime ratio ($13:17$), generating a closed, non-self-intersecting $(13, 17)$ prime torus knot.

12. **Viscoelastic Vorticity Shear Engine (`src/viscoelastic_vorticity_engine.py`)**
    - Models the interaction of kinetic attack vectors ($\mathbf{v}_1$) and structural body vectors ($\mathbf{v}_2$) as colliding fluids, yielding a stable von Kármán vortex street matrix with zero turbulent collapse.

---

## 🚀 Quick Start & Installation

### 1. Clone the Repository

# Clone the grimoire
git clone https://github.com/HhWolfling/Magicicada-Chorus-Rise.git

# Enter the circle
cd Magicicada-Chorus-Rise

# Initialize the chaos
python -m pip install -r requirements.txt
