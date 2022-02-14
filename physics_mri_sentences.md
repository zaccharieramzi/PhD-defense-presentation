In order to understand why it's so difficult to accelerate MRI, let's take a closer look at the physics underlying it.
To do so, let's consider that the MRI scanner generates a strong magnetic field B zero, and that the brain is composed of protons, whose spins align with the magnetic field in a precession movement.
To image the proton density, we send a radio frequency pulse on them, tipping their spin into the plane orthogonal to the magnetic field: this is the excitation phase, the first phase of Nuclear Magnetic Resonance (NMR).
Afterwards, the spin aligns back up to the magnetic field, and sends back a radio frequency pulse, called the Free Induction Decay (FID) which we record: this is the relaxation phase.
For each NMR instance, the recorded signal corresponds to a trajectory in the Fourier space or k-space of the anatomical object.
If we have enough of them, we can recover the object from the k-space using the Inverse Fourier Transform or its fast version the IFFT.
Importantly, MRI is slow because the relaxation phase is slow.
