A trained classifier can be fooled. A change to an image too small for a person to see can make a network label a panda as a gibbon with high confidence, and such adversarial examples often fool other networks trained on the same task. A model can also be attacked before it is trained, by poisoning its training data or planting a backdoor that a trigger pattern switches on, and after it is trained, by queries that reveal whether a person's record was in the training set or that copy the model itself. Adversarial machine learning studies these attacks and the defenses against them.

Most attacks are optimization problems: maximize the loss over a small ball around the input, or find the training points that move the decision boundary most. Many proposed defenses were later broken by stronger attacks, so the chapter separates empirical defenses from certified ones, which prove that no perturbation within a stated radius changes the output. Randomized smoothing gives such a certificate with high probability; exact verification of a ReLU network is NP-complete.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Evasion attacks.** Adversarial examples, the fast gradient sign method, projected gradient descent attacks, the Carlini-Wagner attack, DeepFool, saliency map attacks, universal perturbations, transferability, black-box attacks such as the boundary attack and zeroth-order optimization, and the expectation over transformation and BPDA methods for breaking defenses.
2. **Poisoning and backdoors.** Poisoning of support vector machines, clean-label poisoning, backdoor attacks, spectral signatures for finding poisoned data and Byzantine-robust aggregation such as Krum.
3. **Privacy attacks on models.** Membership inference and the likelihood ratio attack, model inversion, model extraction, gradient inversion, training data extraction, and machine unlearning with SISA training.
4. **Certified defenses.** Neural network verification, Reluplex, interval bound propagation, linear bound propagation, randomized smoothing and defensive distillation.
5. **Language models.** Prompt injection, the GCG suffix attack and green-list watermarks for generated text.

## What to read meanwhile

Read [adversarial training](/adversarial-training/) in Volume 25 first; it is the main empirical defense. The attacks need [backpropagation](/backpropagation/), the [ReLU](/relu/) and the [cross-entropy loss](/cross-entropy-loss/) from Volume 25, and the PGD attack is [projected gradient descent](/projected-gradient-descent/) of Volume 15 run on the input. Poisoning of a [support vector machine](/support-vector-machine/), in Volume 25, is a bilevel problem. Krum and other robust aggregators replace the mean by something like the [geometric median](/geometric-median/) of Volume 13. Verification of ReLU networks is posed as [mixed-integer programming](/mixed-integer-programming/) in Volume 15 or as an [SMT problem](/smt-problem/) in Volume 16, and the randomized smoothing certificate rests on the tail bounds of the [Chernoff bound](/chernoff-bound/) in Volume 1.
