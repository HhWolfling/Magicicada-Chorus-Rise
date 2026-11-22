# 🌀 Magicicada Chorus Rise: Non-Linear Phase-Lock & Topological DSP Engine

[![Live Observatory — Portal](https://img.shields.io/badge/Live_Portal-Topological_Observatory-FFD700?style=for-the-badge&logo=githubpages)](https://hhwolfling.github.io/Magicicada-Chorus-Rise/)
[![Live WebGL — Prime Torus](https://img.shields.io/badge/Live_WebGL-Prime_Torus_Manifold-00FFCC?style=for-the-badge&logo=three.js)](https://hhwolfling.github.io/Magicicada-Chorus-Rise/prime_torus_webgl.html)
[![Live WebGL — 8D Octonion](https://img.shields.io/badge/Live_WebGL-8D_Octonion_Fano-00FFCC?style=for-the-badge&logo=webgl)](https://hhwolfling.github.io/Magicicada-Chorus-Rise/octonionic_shader_webgl.html)
[![Live WebGL — Sri Meru Octonion](https://img.shields.io/badge/Live_WebGL-Sri_Meru_Octonion-FF007F?style=for-the-badge&logo=webgl)](https://hhwolfling.github.io/Magicicada-Chorus-Rise/sri_meru_octonion_webgl.html)
[![Live WebGL — Kuramoto Sisterbrood](https://img.shields.io/badge/Live_WebGL-Kuramoto_Sisterbrood-00FFCC?style=for-the-badge&logo=three.js)](https://hhwolfling.github.io/Magicicada-Chorus-Rise/kuramoto_sisterbrood_webgl.html)

> **A non-linear acoustic synthesis and physical state engine mapping non-Abelian braid groups ($B_3$), prime torus knots ($(13, 17)$ on $\mathbb{T}^2$), viscoelastic vorticity dynamics, hypercomplex octonion rotations ($\mathbb{O}$), and biological relaxation oscillators.**

---

## 🌐 Live Interactive WebGL Visualizers

Experience the high-dimensional phase spaces directly in your browser (with real-time parameter sliders and Web Audio synthesis)[cite: 9]:

* **Topological Observatory Portal (`index.html`, `64.0 Hz` + `65.41 Hz` Drone):** [https://hhwolfling.github.io/Magicicada-Chorus-Rise/](https://hhwolfling.github.io/Magicicada-Chorus-Rise/)
* **Prime Brood Torus Manifold ($(13, 17)$ on $\mathbb{T}^2$):** [https://hhwolfling.github.io/Magicicada-Chorus-Rise/prime_torus_webgl.html](https://hhwolfling.github.io/Magicicada-Chorus-Rise/prime_torus_webgl.html)[cite: 9]
* **8D Octonionic Fano-Plane Shader ($\mathbb{O}$):** [https://hhwolfling.github.io/Magicicada-Chorus-Rise/octonionic_shader_webgl.html](https://hhwolfling.github.io/Magicicada-Chorus-Rise/octonionic_shader_webgl.html)
* **8D Octonion × 3D Sri Meru Volumetric Manifold:** [https://hhwolfling.github.io/Magicicada-Chorus-Rise/sri_meru_octonion_webgl.html](https://hhwolfling.github.io/Magicicada-Chorus-Rise/sri_meru_octonion_webgl.html)[cite: 9]
* **Kuramoto Sisterbrood Resonator ($13:17$ Biphase Cymatic Sphere):** [https://hhwolfling.github.io/Magicicada-Chorus-Rise/kuramoto_sisterbrood_webgl.html](https://hhwolfling.github.io/Magicicada-Chorus-Rise/kuramoto_sisterbrood_webgl.html)

---

## 📐 Mathematical & Physical Framework

The engine models acoustic and physical signal interactions across four core pillars[cite: 9]:

### 1. The Commutator Operator ($\Phi$)
Energy transfer between kinetic transient drive vectors ($H$) and structural anchor vectors ($C$) is governed by non-commutative operator dynamics[cite: 9]:

$$\Phi = [H, C] = H \cdot C - C \cdot H \neq 0$$

*Plaintext version*: Phi equals the commutator bracket of H and C, which is H times C minus C times H, and is non-zero[cite: 9].

When $H$ and $C$ are implemented as non-commuting 3D vector cross-products or complex conjugate STFT spectra, continuous energy dissipation collapses into discrete, periodic cardiac relaxation pulses (systole/diastole)[cite: 9].

### 2. Prime Brood Coprimality & Torus Winding ($\mathbb{T}^2$)
The system locks phase trajectories onto a 2D modular torus surface using the $13$-year (*Magicicada tredecim*) and $17$-year (*Magicicada septendecim*) prime brood ratio[cite: 9]:

$$\gcd(13, 17) = 1, \quad N_{\text{sync}} = 13 \times 17 = 221 \text{ years}$$

*Plaintext version*: The greatest common divisor of 13 and 17 equals 1, and the synchronization interval N_sync equals 13 times 17, which is 221 years[cite: 9].

Because $p=13$ and $q=17$ are prime integers, the phase winding traces a closed $(13, 17)$ prime torus knot on $\mathbb{T}^2$ with zero self-intersection and zero Ohmic drag[cite: 9]:

$$\Omega = 0$$

*Plaintext version*: The Ohmic drag Omega equals zero[cite: 9].

### 3. Hypercomplex Octonion Rotations ($\mathbb{O}$)
Signal coordinates rotate across an 8-dimensional normed division algebra governed by the real scalar axis ($x_0$) and the 7 imaginary units of the Fano Plane ($e_1 \dots e_7$)[cite: 9]:

$$\mathbf{O}(t) = x_0(t) + \sum_{i=1}^{7} x_i(t) e_i$$

*Plaintext version*: O(t) is an octonion signal equal to real component x_0(t) plus the sum from i=1 to 7 of x_i(t) times imaginary basis unit e_i[cite: 9].

Because octonionic multiplication is non-associative ($(e_i \cdot e_j) \cdot e_k \neq e_i \cdot (e_j \cdot e_k)$), phase chirps remain uncollapsible in high-dimensional projections[cite: 9].

### 4. Topological Knot Invariants ($B_3$)
The 3-strand braid generator word $w = \sigma_1 \sigma_2^{-1} \sigma_1 \sigma_2^{-1}$ maps to the immutable Trefoil Knot ($3_1$), yielding time-reversibility under the Alexander Polynomial[cite: 9]:

$$\Delta(t) = t - 1 + t^{-1}, \quad V(t) = t^{-1} + t^{-3} - t^{-4}$$

*Plaintext version*: Alexander polynomial Delta(t) equals t minus 1 plus 1/t, and Jones polynomial V(t) equals 1/t plus 1/t^3 minus 1/t^4[cite: 9].

---

## 📁 Repository Module Manifest

| File / Module | Description |
| :--- | :--- |
| `index.html` | Topological Observatory Portal with live $(p, q)$ commutator shader, `64.0 Hz` + `65.41 Hz` Web Audio drone, and engine switcher. |
| `prime_torus_webgl.html` | Interactive WebGL Three.js browser engine with real-time $p, q, \tau$ slider controls[cite: 9]. |
| `octonionic_shader_webgl.html` | Real-time GPU GLSL fragment shader raymarching 8D octonionic ($\mathbb{O}$) Fano plane field projections. |
| `sri_meru_octonion_webgl.html` | Self-contained volumetric raymarching WebGL visualizer projecting an 8D octonion Fano field onto a 3D stepped Sri Meru lattice with orbit camera and live `13:17` Web Audio drone[cite: 9]. |
| `kuramoto_sisterbrood_webgl.html` | 30-node ($13 + 17$) Kuramoto Sisterbrood phase-synchronization engine with 3D macro-cymatic sphere, Stella Octangula, and TOLT meridian spine. |
| `sri_meru_octonion_shader.glsl` | Standalone GLSL fragment shader source for the 8D octonion × 3D Sri Meru volumetric field[cite: 9]. |
| `mahavidya_dsp_profiles.py` | Deterministic 10-voice STFT commutator audio synthesizer ($\Phi = [Z_H, Z_C]$) locked to `64 Hz`, `65.41 Hz` (C2), `196 Hz` (G3), `293.66 Hz` (D4), and `432 Hz` with pure-Python fallback[cite: 9]. |
| `mahavidya_dsp_presets.json` | Machine-readable parameter matrix for all 10 deterministic STFT commutator profiles (*Kali* through *Kamala*)[cite: 9]. |
| `HARMONIC_TOPOLOGY.md` | Four-stage structural pipeline bridging coprime cicada broods, $\Phi = [H, C]$ commutators, 8D octonions, and the 10-voice STFT matrix. |
| `AXIS_MUNDI_MERU.md` | Historical and structural-morphological reference mapping stepped *Meru* architecture and Sanskrit phonetic combinatorics onto octonion and DSP coordinates[cite: 9]. |
| `src/mixtum_dsp.py` | Non-linear DSP synthesizer processing STFT matrices into `mixtum_output.wav`[cite: 9]. |
| `src/octonion_manifold_rotation.py` | 8D Fano plane non-associative signal trajectory map[cite: 9]. |
| `src/binaural_braid_spatializer.py` | 3D binaural acoustic spatializer using ITD/ILD head-orbit equations for $B_3$ braid frequencies ($65.41\text{ Hz}, 196\text{ Hz}, 293.66\text{ Hz}$). |
| `src/lindblad_quantum_dissipator.py` | Open quantum Lindblad master equation simulation demonstrating $(13, 17)$ coprime shielding against thermal decoherence. |
| `src/knot_invariants.py` | SymPy verification of Jones $V(t)$ and Alexander $\Delta(t)$ topological invariants[cite: 9]. |
| `src/prime_kamea_tetractys.py` | $4 \times 4$ Prime Brood Kamea magic square and Pythagorean Tetractys grid[cite: 9]. |
| `src/viscoelastic_vorticity_engine.py` | 2D fluid shear vorticity matrix $\omega = \nabla \times \mathbf{u}$ generating von Kármán eddies[cite: 9]. |
| `src/braid_group_b3.py` | 3D non-Abelian braid topography visualization for frequencies $65.41\text{ Hz}, 196\text{ Hz}, 293.66\text{ Hz}$[cite: 9]. |
| `src/chladni_3d_volumetric_clean.py` | 3D volumetric standing wave nodal isosurface acoustic chamber[cite: 9]. |

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

# 4. Print the 10-voice STFT DSP profile matrix and export mahavidya_dsp_presets.json
python mahavidya_dsp_profiles.py

# 5. Synthesize a 16-bit PCM WAV file for a specific DSP profile (by index 1-10 or name)
python mahavidya_dsp_profiles.py "Tripura Sundari"
python mahavidya_dsp_profiles.py 1
