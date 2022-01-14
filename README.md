# PhD defense presentation
Using the [SimplePlus Beamer Theme]((https://github.com/PM25/SimplePlus-BeamerTheme)).


## Plan

- Introduction: the problem at hand; MRI is slow! -> prevents people from using it (queue + discomfort + impossibility to hold still or claustrophobia), costly
Therefore, we give ourselves the objective to accelerate MRI
- Intro to MRI: should I care? -> yes bc it enables this and that, also widely used already. Ok now we know it's important to accelerate it, how can I do that?
Let's first understand the physics behind it, in particular what makes it slow. OBSTACLE: impossible to compress the time needed for the spin to relax.
- SOLUTION: Chasing the redundancy: where is it already? Partial Fourier. Can we manufacture it? Parallel Imaging. Can we express it? Compressed Sensing!
Let's understand what CS says and how we can apply it to our problem.
Amazing, BUT the prior is not very rich, can we do better? BUT this prior is going to be a very complex function, that we cannot craft manually.
- SOLUTION: This is where DL comes in: possibility to learn very complex, highly nonlinear functions from data.
Comes at some costs:
    - data
    - compute
    - memory
    - black-box

- AND THEN: we can apply to MRI in different fashions, but we will focus only on 3 main ones:
    - model agnostic
    - single domain restoration
    - unrolled algorithms

Examples:
    - fastMRI 2020 reconstruction challenge: XPDNet
    - Cartesian acquisitions: NCPDNet

- BUT: is DL satisfying for MRI?
    - can it be made robust? yes, Learnlets
    - can it be made a bit made a bit more explanatory? yes, DDSM
    - can it be applied on proppective data and still be more efficient than classical algorithms? yes, IGOGD

- AND THEN: to gain even more performance we need deeper models. BUT activations is a challenge.
SOLUTION: DEQs
BUT DEQs are slow -> SHINE

