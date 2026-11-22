# 🌀 Magicicada Chorus Rise: Non-Linear Phase-Lock & Topological DSP Engine

[![Live WebGL — Prime Torus](https://img.shields.io/badge/Live_WebGL-Prime_Torus_Manifold-00FFCC?style=for-the-badge&logo=three.js)](https://hhwolfling.github.io/Magicicada-Chorus-Rise)
[![Live WebGL — 8D Octonion](https://img.shields.io/badge/Live_WebGL-8D_Octonion_Fano-FFD700?style=for-the-badge&logo=three.js)](https://hhwolfling.github.io/Magicicada-Chorus-Rise/octonionic_shader_webgl.html)
[![Live WebGL — Sri Meru Octonion](https://img.shields.io/badge/Live_WebGL-Sri_Meru_Octonion-FF007F?style=for-the-badge&logo=webgl)](https://hhwolfling.github.io/Magicicada-Chorus-Rise/sri_meru_octonion_webgl.html)

> **A non-linear acoustic synthesis and physical state engine mapping non-Abelian braid groups ($B_3$), prime torus knots ($(13, 17)$ on $\mathbb{T}^2$), viscoelastic vorticity dynamics, hypercomplex octonion rotations ($\mathbb{O}$), and biological relaxation oscillators.**

---

#### 🌐 Live Interactive WebGL Visualizers

Experience the high-dimensional phase space and acoustic resonators directly in your browser:

* **Interactive Prime Torus Engine (13, 17)**: [https://hhwolfling.github.io/Magicicada-Chorus-Rise/](https://hhwolfling.github.io/Magicicada-Chorus-Rise/)
* **Interactive 8D Octonionic Shader Canvas ($\mathbb{O}$)**: [https://hhwolfling.github.io/Magicicada-Chorus-Rise/octonionic_shader_webgl.html](https://hhwolfling.github.io/Magicicada-Chorus-Rise/octonionic_shader_webgl.html)
* **Interactive Sri Meru Octonion Manifold**: [https://hhwolfling.github.io/Magicicada-Chorus-Rise/sri_meru_octonion_webgl.html](https://hhwolfling.github.io/Magicicada-Chorus-Rise/sri_meru_octonion_webgl.html)
* **Kuramoto Sisterbrood Resonator (13:17 Biphase)**: [https://hhwolfling.github.io/Magicicada-Chorus-Rise/kuramoto_sisterbrood_webgl.html](https://hhwolfling.github.io/Magicicada-Chorus-Rise/kuramoto_sisterbrood_webgl.html)

---

## 📐 Mathematical & Physical Framework

The engine models acoustic and physical signal interactions across four core pillars:

### 1. The Commutator Operator ($\Phi$)
Energy transfer between kinetic transient drive vectors ($H$) and structural anchor vectors ($C$) is governed by non-commutative operator dynamics:

$$\Phi = [H, C] = H \cdot C - C \cdot H \neq 0$$

*Plaintext version*: Phi equals the commutator bracket of H and C, which is H times C minus C times H, and is non-zero.

When $H$ and $C$ are implemented as non-commuting 3D vector cross-products[cite: 2] or complex conjugate STFT spectra[cite: 3, 4], continuous energy dissipation collapses into discrete, periodic cardiac relaxation pulses (systole/diastole).

### 2. Prime Brood Coprimality & Torus Winding ($\mathbb{T}^2$)
The system locks phase trajectories onto a 2D modular torus surface using the $13$-year (*Magicicada tredecim*) and $17$-year (*Magicicada septendecim*) prime brood ratio:

$$\gcd(13, 17) = 1, \quad N_{\text{sync}} = 13 \times 17 = 221 \text{ years}$$

*Plaintext version*: The greatest common divisor of 13 and 17 equals 1, and the synchronization interval N_sync equals 13 times 17, which is 221 years.

Because $p=13$ and $q=17$ are prime integers, the phase winding traces a closed $(13, 17)$ prime torus knot on $\mathbb{T}^2$ with zero self-intersection and zero Ohmic drag[cite: 5]:

$$\Omega = 0$$

*Plaintext version*: The Ohmic drag Omega equals zero.

### 3. Hypercomplex Octonion Rotations ($\mathbb{O}$)
Signal coordinates rotate across an 8-dimensional normed division algebra governed by the real scalar axis ($x_0$) and the 7 imaginary units of the Fano Plane ($e_1 \dots e_7$)[cite: 1, 2, 5]:

$$\mathbf{O}(t) = x_0(t) + \sum_{i=1}^{7} x_i(t) e_i$$

*Plaintext version*: O(t) is an octonion signal equal to real component x_0(t) plus the sum from i=1 to 7 of x_i(t) times imaginary basis unit e_i.

Because octonionic multiplication is non-associative ($(e_i \cdot e_j) \cdot e_k \neq e_i \cdot (e_j \cdot e_k)$), phase chirps remain uncollapsible in high-dimensional projections[cite: 5].

### 4. Topological Knot Invariants ($B_3$)
The 3-strand braid generator word $w = \sigma_1 \sigma_2^{-1} \sigma_1 \sigma_2^{-1}$ maps to the immutable Trefoil Knot ($3_1$), yielding time-reversibility under the Alexander Polynomial[cite: 5]:

$$\Delta(t) = t - 1 + t^{-1}, \quad V(t) = t^{-1} + t^{-3} - t^{-4}$$

*Plaintext version*: Alexander polynomial Delta(t) equals t minus 1 plus 1/t, and Jones polynomial V(t) equals 1/t plus 1/t^3 minus 1/t^4.

---

#### 📁 Repository Module Manifest

| Script / Asset | Description |
| :--- | :--- |
| `index.html` / `prime_torus_webgl.html` | Interactive WebGL Three.js $(13, 17)$ prime torus knot engine with real-time $p, q, \tau$ controls and Web Audio tone generator. |
| `octonionic_shader_webgl.html` | Real-time GPU GLSL fragment shader raymarching 8D octonionic ($\mathbb{O}$) Fano plane field projections. |
| `sri_meru_octonion_webgl.html` | Interactive 3D Sri Meru pyramidal yantra coupled to 8D octonionic phase rotations and golden-ratio harmonics. |
| `kuramoto_sisterbrood_webgl.html` | 30-node ($13 + 17$) Kuramoto Sisterbrood phase-synchronization engine with 3D macro-cymatic sphere, Stella Octangula, and TOLT meridian spine. |
| `src/mixtum_dsp.py` | Non-linear DSP synthesizer processing STFT matrices into `mixtum_output.wav`. |
| `src/octonion_manifold_rotation.py` | 8D Fano plane non-associative signal trajectory verification and norm invariant plot. |
| `src/binaural_braid_spatializer.py` | 3D binaural acoustic spatializer using ITD/ILD head-orbit equations for $B_3$ braid frequencies ($65.41\text{ Hz}, 196\text{ Hz}, 293.66\text{ Hz}$). |
| `src/lindblad_quantum_dissipator.py` | Open quantum Lindblad master equation simulation demonstrating $(13, 17)$ coprime shielding against thermal decoherence. |
| `src/knot_invariants.py` | SymPy verification of Jones $V(t)$ and Alexander $\Delta(t)$ topological invariants. |
| `src/prime_kamea_tetractys.py` | $4 \times 4$ Prime Brood Kamea magic square and Pythagorean Tetractys grid. |
| `src/viscoelastic_vorticity_engine.py` | 2D fluid shear vorticity matrix $\omega = \nabla \times \mathbf{u}$ generating von Kármán eddies. |
| `src/braid_group_b3.py` | 3D non-Abelian braid topography visualization for frequencies $65.41\text{ Hz}, 196\text{ Hz}, 293.66\text{ Hz}$. |
| `src/chladni_3d_volumetric_clean.py` | 3D volumetric standing wave nodal isosurface acoustic chamber. |
---

## ⚡ Quickstart

```bash
# 1. Clone repository
git clone [https://github.com/HhWolfling/Magicicada-Chorus-Rise.git](https://github.com/HhWolfling/Magicicada-Chorus-Rise.git)
cd Magicicada-Chorus-Rise

# 2. Install core dependencies
pip install -r requirements.txt

# 3. Synthesize the base Mixtum audio relaxation pulse
python src/mixtum_dsp.py

# 4. Print the 10-voice STFT DSP profile matrix
python src/mahavidya_dsp_profiles.py

# 5. Synthesize a 16-bit PCM WAV file for a specific DSP profile (by index 1-10 or name)
python src/mahavidya_dsp_profiles.py "Tripura Sundari"
python src/mahavidya_dsp_profiles.py 1
