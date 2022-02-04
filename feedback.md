# Feedback repet 1

`git commit 864824dd3f08f608f20ee645cbc81dcea8a3ef09`
Too much on the introduction
Defense is not a course
Not explain what MRI is

Example on how to undersample the k-space
Introduce the undersampling before CS

Give more on the results
More images of the results

Say something about acceleration in reconstruction that DL can provide

For Parallel Imaging => have a figure

Colors => not that bright

183: we do not know what the elements are.

No redundancy in the recaps

In intro clearly say orally, that I selected some contributions and details.

Add distinction between 2D and 3D.

Deep Learning MRI reconstruction: say input is kspace and label is image.

## Slide by slide

3: Show what the impact of motion on image quality + increased motion "over time"
4: No subcategories in the TOC. One sentence per section. (-> give number on each section title frame).
6: 2 different images to highlight the versatility. Say that MRI is noninvasive, high resolution.
7: non important
8-20: can be merged in a single figure
24: add image. Orally maybe mitigate more link redundancy. Maybe not mention Partial Fourier to be more efficient.
25: add figure
26: maybe move this to backup
27: acceleration factor is limited by number of coil. Be clearer on the fact that the AF is limiting. in 3D AF is 8 for PI. Explain what AF is.
45: add illustrations for Omega and S. Explain that x is complex-valued, because of susceptibility.
46: min -> argmin. Give wavelet decomposition of MRI scan. Give reference to Lustig. 1/2 in front of DC.
47: Do I really need this slide ? If so, actually introduce my benchmark contrib, and say that different algorithms exist
65: give an example formula for chain rule
76: Explain that there are a lot of models to parse, only presenting of few
77: explain more the cons of such an approach
78: explain single-domain learning "in the k-space" and "in the image space"
87: show images of the results. Why these networks? Motivation? Say that also OASIS.
97: here show the results (ie images)
99: just before, illustrate results vs GRAPPA. Have figure in plain slide.
103: add spiral.
105: recall IU = iteration unit
106: put results in plain slide
126: highlight implicit models (justify most promising)
133: spend time on the figure => say that there is a tradeoff between memory and computation, SHINE allows to win on both
142: say that the function is Logistic regression and can use QN
143: comment the graph, say what refine version is
144: comment figure more
150: conclusion -> conclusions
151: extension to fMRI (pursued by PAC)
152: just "additional contributions", maybe say why not presented.





NC-PDNet: specify that U-net is the competitor in this study.


## Backup slides
Add stuff that was not in the main presentation:
- learnlets
- dsm uq
- benchmark CS