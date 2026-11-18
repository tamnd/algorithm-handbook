## History

The first interest operator came from robotics. Hans Moravec described it in his 1980 Stanford thesis on the Stanford Cart, a robot that found its way by stereo vision, and took the smallest of four shifted window differences as the score. Chris Harris and Mike Stephens replaced the four shifts by the structure tensor in 1988, and Jianbo Shi and Carlo Tomasi derived the smaller eigenvalue as the right score in their 1994 paper Good features to track.

Scale space has two origins. Taizo Iijima proposed Gaussian smoothing as the unique linear scale space in Japan around 1960, a fact that Joachim Weickert, Seiji Ishikawa and Atsushi Imiya brought to wide notice in 1999. Andrew Witkin in 1983 and Jan Koenderink in 1984 gave the idea its Western form. Tony Lindeberg wrote the theory in his 1994 book and gave normalized derivatives and automatic scale selection in 1998. David Lowe used extrema of the difference of Gaussians for SIFT in 1999 and gave the full method in 2004, together with the ratio test and best bin first matching, which he had described with Jeffrey Beis in 1997.

The years around 2000 made detectors measurable. Cordelia Schmid, Roger Mohr and Christian Bauckhage defined repeatability in 2000. Krystian Mikolajczyk and Schmid gave the Harris-Laplace detector in 2001 and the affine detectors in 2004, and the 2005 comparison of affine region detectors by Mikolajczyk and seven coauthors, with its image sets under known homographies, became the standard test. Jiri Matas and his coauthors introduced MSER in 2002. Navneet Dalal and Bill Triggs gave HOG in 2005, Herbert Bay, Tinne Tuytelaars and Luc Van Gool gave SURF in 2006, and Edward Rosten and Tom Drummond gave FAST in 2006.

Binary descriptors followed the need for speed on small machines. Michael Calonder, Vincent Lepetit, Christoph Strecha and Pascal Fua presented BRIEF in 2010, and ORB, by Ethan Rublee, Vincent Rabaud, Kurt Konolige and Gary Bradski, and BRISK, by Stefan Leutenegger, Margarita Chli and Roland Siegwart, both appeared at ICCV 2011. Relja Arandjelović and Andrew Zisserman proposed RootSIFT in 2012. Chanop Silpa-Anan and Richard Hartley searched several k-d trees with one queue in 2008, and Marius Muja and Lowe built FLANN on randomized forests in 2009.

Learned methods came last. SuperPoint, by Daniel DeTone, Tomasz Malisiewicz and Andrew Rabinovich, appeared in 2018, SuperGlue, by Paul-Edouard Sarlin and the same group, in 2020, and LoFTR, by Jiaming Sun and coauthors, in 2021.

## Further reading

- Richard Szeliski, Computer Vision: Algorithms and Applications, second edition, Springer, 2022. Chapter 7 covers detectors, descriptors and matching with many pictures.
- Tinne Tuytelaars and Krystian Mikolajczyk, Local Invariant Feature Detectors: A Survey, Now Publishers, 2008. A full survey of corner, blob and region detectors, with their invariances and their measured repeatability.
- Tony Lindeberg, Scale-Space Theory in Computer Vision, Kluwer Academic Publishers, 1994. The theory of Gaussian scale space and of normalized derivatives, by its main author.
- David G. Lowe, Distinctive Image Features from Scale-Invariant Keypoints, International Journal of Computer Vision, 2004. The SIFT paper, with the DoG detector, the descriptor, the ratio test and best bin first search.
- Krystian Mikolajczyk and Cordelia Schmid, A Performance Evaluation of Local Descriptors, IEEE Transactions on Pattern Analysis and Machine Intelligence, 2005. The standard comparison of descriptors, with the protocol that later papers reuse.
