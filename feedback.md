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

## PAC feedback
La seule remarque qui me restait c'etais sur le schéma du. XPDNet , où y a la double flèche (dont une grande courbe) , ça manquait d'une légende de l'input, ou au moins décalé la partir courbe vers la droite pour bien marquer le départ.

# Feedback 2

Explain more how the redundancy works (PI)

Don't see why not presenting papers -> shrink introduction again

Recaps too repetitive and too long

Reduce n clicks

Find a pointer + remote

Highlight contributions selection more

## Slide by slide
TOC is long and useless

MRI physics can be made into 1min

Rm Grappa slide

CS -> Inverse Problems

Rm LIP slide
Rm prior slide

Ker A not necessary

Prior => régularisation ?

Not needed to be so low level

Rm Il => operator per channel

Say MRI reconstruction is linear

Add ref for 1.5 accel for CS

L1 prior is not linear: find better formulation

Deep Learning a enlever

Images des équations trop petites

No scaling : a justifier

Say DC allowed to constrain the network

f theta : is just for unrolled

Prox sort du chapeau
Remettre le problème d'optimisation sur slide unrolled model

PSNR a bien dire ce que c'est

Give datasets scale in benchmark, and globally more results in benchmark

Images before statistics

In XPDNET introduce the changing parts before slide change

Say PDNet before XPDNet

Add citation of my paper on top of each slide

TGCC vs Jean Zay

Zoom on XPDNet images

Explain out of distribution

For activations explain with chain rule

DEQs explain more fixed point and iterations

Chain rule vs IFT

In DEQ figure explain more that runtime is green

B is low rank

Pour Shine d'abord présenter DEQS avant HOAG

Explain more JF

Not talk about refine

Rajouter Theorem

Ccl manque de recul

Pursued by a enlever

Autres Idées pour future work

## SF feedback
Excellent presentation @Zaccharie Ramzi! This is a very impressive amount of work and you should certainly be very proud of what you have accomplished during your PhD. Sorry I could not be there in person for this rehearsal, but here are my thoughts.

The YouTube stream worked quite well overall. There were a couple of places where the sound and/or picture were slightly distorted, but this could simply be from my connection speed. Your voice was quite clear but I could barely hear most of the comments and questions from the audience.
I think the presentation style was quite good and in particular I liked the regular recaps of the take aways messages. I don’t really have any specific points that could be improved apart from some “ahs” and “ums” when transitioning between slides.
In some places the yellow text was not very easy to read (e.g. slide 33),
The diagram on slide 16 was also a bit hard to read.
I think the introductory sections were extremely clear and very easy to follow. :applaudissements: The sections on your own work were also well presented but some parts came and went very quickly (e.g slides 75 and 126).  I think in a few places you may want to take just an extra second or two to allow the audience to digest some of the information presented.
In several places you include intialisms/acronyms that I don’t believe are universally known (e.g. FID, ISTA, DEQ, etc.). While you did say what there were on each slide, if someone missed one it may be tricky to follow. I would suggest perhaps having them written out at least once, perhaps even in a footnote.
When presenting the performance of your results with respect to the state of the art, I think could again take an extra second to allow the audience to compare some of the images/residuals. I also think it would help to direct attention to the results of your methods (XPDNet, NC-PDNet, etc.) with an arrow or a box or whatever that makes these results stand out a bit from the others.
On slide 110 you mentioned results were from a 2019 challenge, but I did not see this written on the slide.
Finally, if you want, you could of course mention your contributions to PySAP in slide 146 or 147. :visage_légèrement_souriant:

## CG feedback
Thanks Zacc, as requested, here are my notes in real time:
Better enunciation/tonality at the beginning
Much better intro, less pedagodic
Good visual on the head coil
FYI: The system cut out at around slides 90-93
Slide 135: maybe you want to list the cases you stated where SHINE could be used
Slide 138: you stated I want to recall you - this is not English. Please say either I would like to "remind you" or "recall for you"
Slide 145: the names you stated for the future direction - I think it would be good if you could indicate that they are currently PhD students
Getting better and better. Bravo.

Zacc, last comment...regarding your explanation of k-space..it's a bit weak. I recall a, early slide set produced by Chaithya in which he discussed k-space in a really succinct way. You might want to ask him about checking out his slides...just a thought.
Cheers

## PC feedback
Il reste un passage confus dans la première partie c'est dans la façon tu introduits le k-space. Il faut que tu parles clairement de l'acquisition selon un schéma d'encodage spatial (ie à partir des gradients dans au moins deux directions de l'espace) pour qu'on comprenne mieux le lien entre acq et coef de Fourier. On en parle de vive voix plus tard. Tu peux mettre.
