# Magicicada Chorus Rise

**Prime-Period Cyclical Emergence ($p = 13, q = 17$), Kuramoto Phase-Locking & 8D Octonionic GLSL Raymarching Engines**

> **Live Interactive Observatory:** **[https://hhwolfling.github.io/Magicicada-Chorus-Rise/](https://hhwolfling.github.io/Magicicada-Chorus-Rise/)**  
> **Digital Releases & Shader Packs:** **[https://hhwolfling.gumroad.com/](https://hhwolfling.gumroad.com/)**

---

## Interactive WebGL Studios & Standalone GLSL Shaders

Every manifold in this repository is paired 1-to-1 between an interactive 3D WebGL studio (`.html`) and a pure, dependency-free fragment shader (`.glsl`) ready for Shadertoy, KodeLife, or custom WebGL pipelines.

| Manifold | Live Interactive 3D Studio | Repository Source | Standalone GLSL Fragment Shader |
| :--- | :--- | :--- | :--- |
| **01. Prime Torus ($\mathbb{T}^2$)** | [Launch Prime Torus Studio](https://hhwolfling.github.io/Magicicada-Chorus-Rise/prime_torus_webgl.html) | `prime_torus_webgl.html` | `prime_torus_shader.glsl` |
| **02. Kuramoto Sisterbrood** | [Launch Kuramoto Studio](https://hhwolfling.github.io/Magicicada-Chorus-Rise/kuramoto_sisterbrood_webgl_2.html) | `kuramoto_sisterbrood_webgl_2.html` | `kuramoto_sisterbrood_shader.glsl` |
| **03. 8D Octonionic Fano** | [Launch Octonionic Studio](https://hhwolfling.github.io/Magicicada-Chorus-Rise/octonionic_shader_webgl_3.html) | `octonionic_shader_webgl_3.html` | `octonionic_fano_shader.glsl.txt` |
| **04. Sri Meru × 8D Octonion** | [Launch Sri Meru Studio](https://hhwolfling.github.io/Magicicada-Chorus-Rise/sri_meru_octonion_webgl.html) | `sri_meru_octonion_webgl.html` | `sri_meru_octonion_shader.glsl` |

---

## Studio Navigation & Export Hotkeys

All four `.html` WebGL studios share a unified control and capture console:

| Input / Key | Action |
| :--- | :--- |
| **Left-Drag** | Orbit 360° around the manifold (yaw & pitch) |
| **Scroll Wheel** | Fly inside the geometry and zoom through the aperture |
| **`[H]`** | Toggle the parameter HUD panel (auto-centers the manifold) |
| **`[C]`** | Toggle smooth cinematic auto-orbit |
| **`[S]`** | Capture an instant, HUD-free high-DPI `.png` snapshot |
| **`[R]`** | Record a seamless 5.0-second `.webm` video loop |
| **`[0]`** | Reset camera orbit and zoom to default observatory view |

---

## Mathematical Architecture

### 1. Coprime Brood Synchronization ($p = 13, q = 17$)
Periodical cicada broods avoid destructive harmonic overlap and predator phase-locking by emerging on coprime intervals ($p = 13$ and $q = 17$), delaying full co-emergence to their least common multiple:

$$\text{lcm}(13, 17) = 13 \times 17 = 221 \text{ cycles}$$

```text
Plain text: lcm(13, 17) = 13 * 17 = 221 cycles
```

On the Prime Torus ($\mathbb{T}^2$), biphase helical strands wind along the $(13, 17)$ torus knot geodesic governed by:

$$\psi(\phi, \theta, t) = q\phi - p\theta - \omega t$$

```text
Plain text: psi(phi, theta, t) = q * phi - p * theta - omega * t
```

### 2. Kuramoto Phase Coherence & Order Parameter
In the Sisterbrood resonator, 30 coupled oscillators ($13 + 17$) evolve under sinusoidal phase coupling $K$, measured by the complex Kuramoto order parameter $r(t)$:

$$r(t) e^{i\Psi(t)} = \frac{1}{N} \sum_{j=1}^{N} e^{i\theta_j(t)}$$

```text
Plain text: r(t) * exp(i * Psi(t)) = (1 / N) * sum_{j=1..N} exp(i * theta_j(t))
```

As coupling tension increases, phase variance collapses ($r(t) \to 1$) and the central spherical-harmonic cymatic core locks into a standing-wave resonance inside a counter-rotating Stella Octangula frame.

### 3. Non-Associative 8D Octonions ($\mathbb{O}$) & ACES Filmic Optics
The Octonionic Fano and Sri Meru engines project 8-dimensional norm-invariant hyper-shells into 3D signed distance fields modulated by the 7 directed imaginary triads ($e_1 \dots e_7$) of the Fano plane, rendered with ACES filmic tone mapping on `#05050A` void-black with `#00FFCC` cyan, `#FF007F` magenta, and `#FFD700` gold spectral channels.

---

## Unified GLSL Uniform Contract

All standalone `.glsl` fragment shaders expose a standardized uniform interface for drop-in integration:

```glsl
uniform vec2 u_resolution; // Viewport dimensions in pixels
uniform float u_time;      // Elapsed simulation time in seconds
uniform float u_p;         // Primary prime brood frequency (default: 13.0)
uniform float u_q;         // Secondary prime brood frequency (default: 17.0)
uniform float u_tau;       // Phase-lock coupling tension (0.0 .. 1.0)
```

---

## Running Locally

No build step or package manager is required:

1. Clone the repository:
   ```bash
   git clone [https://github.com/HhWolfling/Magicicada-Chorus-Rise.git](https://github.com/HhWolfling/Magicicada-Chorus-Rise.git)
   cd Magicicada-Chorus-Rise
   ```
2. Open `index.html` (or any `*_webgl*.html` studio) directly in a modern WebGL-enabled browser.

---

`[WE_WOZ_HERE]⁹⁹` · **Hanna Urbańska (`HhWolfling`)**

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
