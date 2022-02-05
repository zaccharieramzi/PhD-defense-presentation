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

## GDF's feedback
(1) je voulais rappeler un coup le commentaire de PA sur les couleurs trop vives, en particulier vert et jaune
(2) slide 70: la mention de black-box me dérange. Est-ce qu'il s'agit d'un piège pour que les reviewers posent la question de l'interpretabilité et de la confiance dans les algos de ML ? Est ce que tu as préparé des slides supplémentaires pour répondre à ça ?
(3) slide 94: Je ne crois pas que tu introduises le terme de CNN, ce qui peut être déroutant dans certaines slides sachant que la structure du PDNet & Co n'est pas détaillée
(4) slide 95: Pareil pour les cartes de sensitivité, Le raffinage des cartes manque d'une phrase de contexte, ou au moins d'un piil plus d'emphase
(5) slide 102: a l'oral, tu introduisais la slide en disant qu'on allait se demander pourquoi on a besoin du non cartésien, sans qu'on sache ce que le Cartesien est, puis explique ce qu'est le non Cartesien plutôt que pourquoi on en a besoin. Les quelques phrases d'introduction étaient déroutantes
(6) slide 108: les noms au dessus du tableau sont un peu petits
(7) slide 115: magnifiques dessins, très explicite
(8) slide 151: perso je préfère le terme de B0 in homogeneity correction, ou bien off-resonance correction. Juste B0 corrections n'est pas assez explicite
(9) quelques éléments d'anglais sur lesquels j'ai tiqué, mais ça vient peut être seulement de moi. Des moments où tu disais "less" au lieu de "fewer", et surtout slide 153 j'entendais "co-funding" au lieu de "co-founding"

## CG's feedback
Presentation and slide appearance
Please remember to start on time
At the beginning, I would have preferred if you had told us what you are going to 
tell us – like prepping us for the good talk ahead. Tell us how you increase the 
knowledge base
 A shortened form of the following would be good (I rewrote it slightly as it’s oriented to a 
verbal delivery): 
The main objective of my PhD thesis is to propose new architecture designs for 
acquisition scenarios, which deviate from the typical Cartesian 2D sampling. To this end, 
I review various neural networks for MRI reconstruction. I show you that we had a  
superior performance with , “the PDNet” model, which was used in two contexts: The 
fastMRI 2020 reconstruction challenge and the 3D non-Cartesian data problem. The 
clinical applicability of deep learning for medical imaging is important and to address this 
I will propose ways in which to build a robust model that can be thoroughly inspected, 
and tested. I show you how deep learning frameworks can implement deeper MRI 
reconstruction models, and will conclude with the introduction ot my new acceleration 
method (called SHINE) for the training of such models.
Good spacing and not too much info on each slide and an easy transition for over 
100 slides!
At the end, I couldn’t hear anybody but you
Content
I was surprised at the level you started at. – super elementary. Although the 
information was correct, it seemed to be MRI 101 which your jury members might 
find redundant. This was especially offsetting, when you introduced the concept of
acceleration after the graph of the number of French MRI scans that are 
effectuated.  – sudden complexity!
You talked about the concept of procession. You said ‘it’s sort of procession’ but 
what you meant it is procession. That qualifier is certainly not needed in a thesis 
presentation
Record – you said this numerous times like you say ‘ I play a record (récord). 
Actually, it’s pronounced REE_CORD. “We Ree_cord the measurements...”
So appreciated your numerous recaps of why MRI is slow...
Slide 17 is finally when the true beauty of your talk begins
Slide 24 starts to ramp up in complexity suddenly in comparison with the rest
Side 25: Could you include an image of these multiple coils?
Slide 34 at first it was super easy to understand and then suddenly you just state 
Ker A ≠[0] without an explanation....
Slide 132 is a good explanation of memoryless training
Delivery 
This concerns how you spoke, tonality and speed. All really good, a few too many 
hmms, ahhs a few times which gave the impression that you were thinking out 
loud instead of giving us a well-rehearsed presentation – take this as a comment 
for perfecting your already good presentation
Your enunciation at the end of your sentences drops off very slightly – but overall 
is really good! Bravo