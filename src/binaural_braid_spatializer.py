import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

def generate_3d_binaural_braid(duration=10.0, sample_rate=44100):
    print("Synthesizing Layer 3: 3D Binaural Braid Spatial Audio Engine...")
    
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    num_samples = len(t)
    
    # 1. B3 Braid Strand Fundamental Frequencies (Hz)
    f1 = 65.41   # C2 Base Anchor
    f2 = 196.00  # G3 Quint Anchor
    f3 = 293.66  # D4 Octave + Fifth
    
    # 2. Physical Head & Acoustic Constants
    r_head = 0.0875  # Head radius (~8.75 cm)
    ear_x = 0.09     # Ear displacement on X-axis (+/- 9cm)
    c_sound = 343.0  # Speed of sound (m/s)
    
    # Initialize Left and Right Audio Buffers
    left_channel = np.zeros(num_samples, dtype=np.float64)
    right_channel = np.zeros(num_samples, dtype=np.float64)
    
    # 3. 3D Trajectory Orbits for the 3 Braid Strands
    # Braid Word Trajectory: w = sigma_1 * sigma_2^-1 * sigma_1 * sigma_2^-1
    orbit_speed = 0.5  # Revaluations per second
    
    # Strand 1 Orbit
    pos1_x = 2.0 * np.cos(2 * np.pi * orbit_speed * t)
    pos1_y = 2.0 * np.sin(2 * np.pi * orbit_speed * t)
    pos1_z = 0.5 * np.sin(2 * np.pi * 3 * orbit_speed * t)
    
    # Strand 2 Orbit (Phase shifted by 120 deg)
    pos2_x = 2.0 * np.cos(2 * np.pi * orbit_speed * t + 2 * np.pi / 3)
    pos2_y = 2.0 * np.sin(2 * np.pi * orbit_speed * t + 2 * np.pi / 3)
    pos2_z = 0.5 * np.sin(2 * np.pi * 3 * orbit_speed * t + 2 * np.pi / 3)
    
    # Strand 3 Orbit (Phase shifted by 240 deg)
    pos3_x = 2.0 * np.cos(2 * np.pi * orbit_speed * t + 4 * np.pi / 3)
    pos3_y = 2.0 * np.sin(2 * np.pi * orbit_speed * t + 4 * np.pi / 3)
    pos3_z = 0.5 * np.sin(2 * np.pi * 3 * orbit_speed * t + 4 * np.pi / 3)
    
    strands = [
        (f1, pos1_x, pos1_y, pos1_z),
        (f2, pos2_x, pos2_y, pos2_z),
        (f3, pos3_x, pos3_y, pos3_z)
    ]
    
    # 4. Binaural Spatial Synthesis Loop
    for freq, px, py, pz in strands:
        # Base Carrier Wave
        carrier = np.sin(2 * np.pi * freq * t)
        
        # Calculate distances to Left Ear (-ear_x, 0, 0) and Right Ear (+ear_x, 0, 0)
        dist_L = np.sqrt((px - (-ear_x))**2 + py**2 + pz**2)
        dist_R = np.sqrt((px - ear_x)**2 + py**2 + pz**2)
        
        # Interaural Level Difference (Inverse Distance Attenuation)
        amp_L = 1.0 / (dist_L**1.2)
        amp_R = 1.0 / (dist_R**1.2)
        
        # Interaural Time Delay (Phase Shift)
        delay_L_samples = (dist_L / c_sound * sample_rate).astype(int)
        delay_R_samples = (dist_R / c_sound * sample_rate).astype(int)
        
        # Apply Time Delays and Amplitudes into Channels
        for i in range(num_samples):
            idx_L = i - delay_L_samples[i]
            idx_R = i - delay_R_samples[i]
            
            if idx_L >= 0:
                left_channel[i] += carrier[idx_L] * amp_L[i]
            if idx_R >= 0:
                right_channel[i] += carrier[idx_R] * amp_R[i]
                
    # Normalize Audio Output Peak to -1.0 dB
    max_val = max(np.max(np.abs(left_channel)), np.max(np.abs(right_channel)))
    left_channel = (left_channel / max_val * 0.9).astype(np.float32)
    right_channel = (right_channel / max_val * 0.9).astype(np.float32)
    
    # Interleave Stereo Channels
    stereo_signal = np.vstack((left_channel, right_channel)).T
    
    # Save Audio Output WAV
    output_filename = "binaural_braid_3d.wav"
    wavfile.write(output_filename, sample_rate, (stereo_signal * 32767).astype(np.int16))
    print(f"Successfully generated 3D Binaural Spatial Audio: '{output_filename}'")
    
    # Plot Spatial Orbit Trajectories
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(10, 6), facecolor='#05050A')
    ax = fig.add_subplot(111, projection='3d', facecolor='#05050A')
    
    ax.plot(pos1_x, pos1_y, pos1_z, color='#00FFCC', label='Strand 1 (65.41 Hz)', linewidth=1.5)
    ax.plot(pos2_x, pos2_y, pos2_z, color='#FF007F', label='Strand 2 (196.00 Hz)', linewidth=1.5)
    ax.plot(pos3_x, pos3_y, pos3_z, color='#FFD700', label='Strand 3 (293.66 Hz)', linewidth=1.5)
    
    # Draw Ear Listener Marker
    ax.scatter([0], [0], [0], color='#FFFFFF', s=100, label='Listener Head Center')
    
    ax.set_title("3D B₃ BRAIN SPATIAL ORBIT TRAJECTORIES\nInteraural Acoustic Delay Field", color='#00FFCC', fontsize=11, fontweight='bold')
    ax.set_xlabel("X (Left / Right) [m]", color='#8A9BA8')
    ax.set_ylabel("Y (Front / Back) [m]", color='#8A9BA8')
    ax.set_zlabel("Z (Up / Down) [m]", color='#8A9BA8')
    ax.legend(loc='upper right', fontsize=8, framealpha=0.2)
    
    plot_filename = "binaural_braid_trajectories.png"
    plt.savefig(plot_filename, dpi=300, facecolor=fig.get_facecolor())
    print(f"Saved 3D Trajectory Plot as '{plot_filename}'")
    plt.show()

if __name__ == "__main__":
    generate_3d_binaural_braid()
