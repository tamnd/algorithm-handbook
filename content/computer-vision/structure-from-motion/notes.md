## History

Least squares is older than photography. Gauss fitted planetary orbits by it and described his method in 1809, and the step that bears his name with Newton's is the linearization he used. Kenneth Levenberg added a damping term in 1944 and Donald Marquardt rediscovered and popularized it in 1963. Michael Powell's dog leg method of 1970 and Jorge Moré's careful implementation of Levenberg-Marquardt in 1978 turned these ideas into robust trust-region codes.

Bundle adjustment came from photogrammetry. Duane Brown and others adjusted bundles of rays from aerial photographs in the late 1950s, and they already used the block structure that separates cameras from points. Computer vision met the method again in the 1990s. Bill Triggs, Philip McLauchlan, Richard Hartley and Andrew Fitzgibbon wrote the survey of 2000 that set out gauge freedom, the reduced camera system and sparse factorization for the field. Manolis Lourakis and Antonis Argyros released the sparse bundle adjustment package, described in 2009, and compared dog leg with Levenberg-Marquardt in 2005. Sameer Agarwal, Noah Snavely, Steven Seitz and Richard Szeliski showed in 2010 that conjugate gradients on the reduced system handle very large problems.

Factorization came from the tracking of features in video. Carlo Tomasi and Takeo Kanade published the orthographic method in 1992, Conrad Poelman and Kanade extended it to paraperspective in 1997, and Peter Sturm and Bill Triggs gave the projective version with depth scaling in 1996.

Large collections of photographs drove the incremental and global methods. Photo Tourism by Snavely, Seitz and Szeliski in 2006 reconstructed landmarks from internet photographs one image at a time, and COLMAP by Johannes Schönberger and Jan-Michael Frahm in 2016 made the incremental pipeline robust. Venu Madhav Govindu proposed rotation averaging in 2001 and its Lie-algebraic form in 2004; Daniel Martinec and Tomáš Pajdla, Hartley and coauthors in 2013, and Avishek Chatterjee and Govindu refined it. Kyle Wilson and Snavely's 1DSfM of 2014 and Onur Özyeşil and Amit Singer's work of 2015 addressed translation averaging, and GLOMAP in 2024 showed a global pipeline with the accuracy of incremental ones.

Visual odometry has its name from David Nistér, Oleg Naroditsky and James Bergen in 2004. Keyframe methods followed, among them PTAM in 2007 and ORB-SLAM in 2015. Christian Forster, Matia Pizzoli and Davide Scaramuzza introduced semi-direct odometry in 2014, and Jakob Engel, Vladlen Koltun and Daniel Cremers published direct sparse odometry in 2016, with the journal version in 2018.

## Further reading

- Bill Triggs, Philip McLauchlan, Richard Hartley and Andrew Fitzgibbon, Bundle Adjustment: A Modern Synthesis, Springer, 2000. The reference survey of the cost, its gauge and its sparse solution.
- Richard Hartley and Andrew Zisserman, Multiple View Geometry in Computer Vision, Cambridge University Press, 2004. Its chapters on iterative estimation and factorization cover the first half of this chapter.
- Jorge Nocedal and Stephen Wright, Numerical Optimization, Springer, 2006. Trust regions, Gauss-Newton, Levenberg-Marquardt and conjugate gradients in one place.
- Davide Scaramuzza and Friedrich Fraundorfer, Visual Odometry, IEEE Robotics and Automation Magazine, 2011 and 2012. A two-part tutorial on feature-based odometry and its error sources.
- Onur Özyeşil, Vladislav Voroninski, Ronen Basri and Amit Singer, A Survey of Structure from Motion, Acta Numerica, 2017. The view from rotation and translation averaging.
