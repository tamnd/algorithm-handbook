A spam filter, a malware detector or an image classifier is trained to be right on average, on data drawn from the same distribution as its training set. An attacker does not draw from that distribution. A change of each pixel by $8/255$, too small to see, can move an image across the decision boundary of a network; a few hundred poisoned training images can plant a trigger that sends any input to a chosen label; and a model's answers can show whether one person's record was in its training set. Adversarial machine learning studies these attacks so that defenders can measure them and build models and systems that resist them. The chapter takes the defender's side throughout. Each attack is stated by its threat model: what the attacker wants, what it knows (white box, black box with scores, labels only), and what it may change (a test input in an $\ell_p$ ball, or a fraction of the training data). Then it shows how the attack is measured, detected or prevented.

Two kinds of results run through the chapter and must not be confused. An attack that succeeds gives an upper bound on robust accuracy, and an attack that fails proves nothing. A certificate, from a verifier or from randomized smoothing, gives a lower bound that holds against every attacker in the threat model. Success rates and robust accuracies quoted in the entries are measurements on the stated models, data and budgets.

## What the chapter covers

1. **Threat models and adversarial examples.** The definition of an [adversarial example](/adversarial-example/) and of an [evasion attack](/evasion-attack/) as an optimization problem with an explicit adversary.
2. **White-box evasion attacks.** The [fast gradient sign method](/fast-gradient-sign-method/), the [PGD attack](/pgd-attack/), [DeepFool](/deepfool/), the [Carlini-Wagner attack](/carlini-wagner-attack/), the [Jacobian saliency map attack](/jacobian-saliency-map-attack/) and the [universal adversarial perturbation](/universal-adversarial-perturbation/). On a linear model most of them have closed forms, which the exercises use.
3. **Black-box evasion.** [Transferability](/adversarial-transferability/), the [zeroth order optimization attack](/zeroth-order-optimization-attack/) with scores, and the label-only [boundary attack](/boundary-attack/).
4. **Evaluating defenses.** [Defensive distillation](/defensive-distillation/), which hid gradients and was broken, and the two tools for testing such defenses: [BPDA](/backward-pass-differentiable-approximation/) and [expectation over transformation](/expectation-over-transformation/).
5. **Certified robustness.** The [verification problem](/neural-network-verification-problem/) and its exact solver [Reluplex](/reluplex/); the sound but incomplete [interval bound propagation](/interval-bound-propagation/) and [linear bound propagation](/linear-bound-propagation/); and [randomized smoothing](/randomized-smoothing/), which certifies a smoothed classifier.
6. **Poisoning and backdoors.** [Data poisoning](/data-poisoning/) in general, the [SVM poisoning attack](/svm-poisoning-attack/), [clean-label poisoning](/clean-label-poisoning/), [backdoor attacks](/backdoor-attack/), the [spectral signatures](/spectral-signatures-defense/) filter and [Krum](/krum-aggregation/) for distributed training.
7. **What a trained model reveals.** [Membership inference](/membership-inference-attack/) and the [likelihood ratio attack](/likelihood-ratio-membership-attack/), [model inversion](/model-inversion-attack/), [gradient inversion](/gradient-inversion-attack/), [training data extraction](/training-data-extraction/) and [model extraction](/model-extraction-attack/).
8. **Forgetting training data.** [Machine unlearning](/machine-unlearning/), exact and approximate, and [SISA training](/sisa-training/).
9. **Language models.** [Prompt injection](/prompt-injection/), the [GCG attack](/greedy-coordinate-gradient-attack/) on safety training, described at the level of its threat model, and the [green list watermark](/language-model-watermarking/).

## A first reading

Read these entries first, in this order:

1. [Adversarial example](/adversarial-example/), for the threat model and the minimal perturbation of a linear classifier.
2. [Fast gradient sign method](/fast-gradient-sign-method/).
3. [PGD attack](/pgd-attack/), the standard strong first-order attack.
4. [Backward pass differentiable approximation](/backward-pass-differentiable-approximation/), for why defenses must be tested by adaptive attacks.
5. [Interval bound propagation](/interval-bound-propagation/), the simplest certificate.
6. [Randomized smoothing](/randomized-smoothing/).
7. [Data poisoning](/data-poisoning/).
8. [Backdoor attack](/backdoor-attack/).
9. [Membership inference attack](/membership-inference-attack/).
10. [Machine unlearning](/machine-unlearning/).
11. [Prompt injection](/prompt-injection/).

On a first pass you can skip the Carlini-Wagner and JSMA attacks, the black-box group, Reluplex, the SVM and clean-label attacks, and the likelihood ratio attack. They refine ideas met in the first reading. The certified group is the most mathematical; IBP and smoothing are enough to see what a certificate says.

## Before you start

The chapter assumes the basics of supervised learning: [logistic regression](/logistic-regression/), the [cross-entropy loss](/cross-entropy-loss/), [empirical risk minimization](/empirical-risk-minimization/) and [overfitting](/overfitting/) from Volume 25, with [ReLU](/relu/) networks and [backpropagation](/backpropagation/). From Volume 15 it uses [gradient descent](/gradient-descent/), [projected gradient descent](/projected-gradient-descent/) and [stochastic gradient descent](/stochastic-gradient-descent/). The privacy group and machine unlearning use the [definition of differential privacy](/differential-privacy-definition/) from the differential privacy chapter of this volume. Randomized smoothing and the membership tests use the [Neyman-Pearson lemma](/neyman-pearson-lemma/) and the [Clopper-Pearson interval](/clopper-pearson-interval/) from Volume 33. The bound propagation entries use [interval arithmetic](/interval-arithmetic/) from Volume 12, and Reluplex uses the [SMT problem](/smt-problem/) from Volume 16. The language-model group assumes a [language model](/language-model/) from Volume 41.
