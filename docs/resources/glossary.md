# Cross-book Glossary

This is ART101's canonical vocabulary. Definitions are intentionally concise and cross-disciplinary; a chapter may add context but should not redefine a term incompatibly. Abbreviations are expanded at first use in each chapter and may be used alone afterward. A term that has a narrower local or regulatory meaning is labeled as such.

## AI and model development

- **Activation function:** A function applied to a neuron's weighted input, commonly to introduce nonlinearity.
- **Agent:** A system that uses a model in a loop to choose actions, inspect results, maintain state, and pursue a defined goal.
- **Artificial intelligence (AI):** The umbrella field of computational systems designed to perform tasks associated with perception, prediction, language, decision support, or action.
- **Attention:** A mechanism that weights relationships among elements of an input or representation.
- **Backpropagation:** An algorithm that applies the chain rule to compute how model parameters affect a loss.
- **Batch:** A group of examples processed together for one training update or inference operation.
- **Calibration:** Agreement between predicted probabilities and observed event frequencies in the relevant population.
- **Classification:** Prediction of one or more discrete categories.
- **Convolutional neural network (CNN):** A neural-network family that uses shared local filters, especially for grid-like data such as images.
- **Data:** Recorded observations used as inputs, context, labels, or evaluation outcomes.
- **Deep learning:** Machine learning using multilayer neural networks to learn representations and outputs.
- **Development set:** The data available to influence model creation; it normally includes separate training and validation subsets.
- **Distribution shift:** A meaningful difference between the data distribution encountered in use and the distribution represented during development or evaluation.
- **Epoch:** One pass through the training dataset.
- **Feature:** A variable supplied to a model, whether measured directly or derived from raw data.
- **Foundation model:** A model pretrained broadly and adapted or prompted for multiple downstream tasks; the label does not establish clinical fitness.
- **Generative adversarial network (GAN):** A generative model trained through competition between a generator and a discriminator.
- **Generalization:** Performance on relevant cases that did not influence model fitting or selection.
- **Gradient descent:** A family of optimization methods that update parameters in a direction intended to reduce loss.
- **Hyperparameter:** A setting chosen outside ordinary parameter fitting, such as learning rate or model depth.
- **Inference:** Application of a frozen model and preprocessing pipeline to new input to produce an output.
- **Label:** A reference target used for learning or evaluation; it can contain uncertainty, disagreement, or bias and is not automatically ground truth.
- **Large language model (LLM):** A high-capacity model pretrained on large text collections to predict or generate token sequences and adaptable to varied language tasks.
- **Learning rate:** A hyperparameter controlling the size of an optimization update.
- **Loss function:** The objective minimized or otherwise optimized during training.
- **Machine learning (ML):** Approaches in which model behavior is estimated from data rather than exhaustively programmed as rules.
- **Model:** A parameterized mapping from defined inputs to outputs. A clinical AI system additionally includes preprocessing, interfaces, people, policies, and controls.
- **Overfitting:** Learning patterns specific to development data that do not generalize to relevant new data.
- **Parameter:** A value estimated during model fitting, such as a neural-network weight.
- **Preprocessing:** Transformations applied before model input; any transformation learned from data must be fitted without access to held-out evaluation data.
- **Regression:** Prediction of a continuous quantity.
- **Retrieval-augmented generation (RAG):** Generation conditioned on passages retrieved from an external source at inference time.
- **Segmentation:** Assignment of a class or value to image pixels or voxels, commonly to delineate anatomy.
- **Self-supervised learning:** Learning from targets constructed from the data themselves rather than separately supplied task labels.
- **Supervised learning:** Learning a mapping from examples paired with reference labels or outcomes.
- **Test set:** Data withheld from fitting and model selection and used after choices are fixed to estimate performance.
- **Training:** Estimation of model parameters from development examples.
- **Transfer learning:** Reusing a model or representation learned for one setting as a starting point for another.
- **Transformer:** A neural-network architecture built primarily around attention operations.
- **U-Net:** An encoder-decoder segmentation architecture with skip connections that combine multiscale context and spatial detail.
- **Validation set:** Within model development, data used to guide choices without fitting ordinary parameters. In broader clinical usage, *validation* also means evidence that a frozen system is fit for its intended use; writers must identify which meaning they intend.
- **Vision-language model (VLM):** A model that connects visual and textual representations for retrieval, classification, question answering, or generation.

## Statistics and evidence

- **Accuracy:** The proportion of evaluated cases classified correctly; it can be misleading with class imbalance or unequal error costs.
- **Area under the receiver operating characteristic curve (AUROC):** The probability that a randomly selected positive case is ranked above a randomly selected negative case; it does not specify calibration or clinical utility.
- **Bias:** Systematic deviation from the target quantity or intended behavior; in machine learning it may arise from data, labels, design, evaluation, or deployment.
- **Causal effect:** The contrast between outcomes under alternative interventions for the same target population, estimated under explicit assumptions; association alone is insufficient.
- **Censoring:** In time-to-event analysis, incomplete observation of an event time beyond a known follow-up point.
- **Confidence interval (CI):** A repeated-sampling uncertainty interval constructed by a stated procedure; it is not generally the probability that the fixed true value lies within the observed interval.
- **Confounding:** Mixing of an exposure-outcome association with effects of common causes.
- **Data leakage:** Information unavailable at the intended prediction time, or information from held-out cases, influencing model fitting, preprocessing, selection, or evaluation.
- **Decision-curve analysis:** Evaluation of net benefit across decision thresholds under specified relative costs of false-positive and false-negative decisions.
- **Discrimination:** Ability of a score to rank or separate cases with different outcomes.
- **External validation:** Evaluation of a frozen pipeline on meaningfully separate data, such as another institution, time period, or population.
- **F1 score:** Harmonic mean of precision and recall at a chosen threshold.
- **Ground truth:** A term best reserved for a reference known with negligible uncertainty. Expert annotations and clinical outcomes are usually better called *reference standards* or *labels*.
- **Internal validation:** Evaluation using data from the same source as development with separation methods such as a holdout, cross-validation, or bootstrapping.
- **Precision / positive predictive value (PPV):** Among positive predictions, the proportion that are reference-positive; it depends on prevalence.
- **Prospective evaluation:** Evaluation in which the data and outcomes are collected forward under a prespecified protocol; it is not necessarily interventional.
- **Recall / sensitivity:** Among reference-positive cases, the proportion predicted positive.
- **Reference standard:** The procedure or information used to define the condition or target against which a system is evaluated.
- **Specificity:** Among reference-negative cases, the proportion predicted negative.
- **Uncertainty:** Limited knowledge about an input, label, parameter, prediction, or consequence. A model score is not automatically a valid uncertainty estimate.

## Imaging and radiotherapy data

- **Computed tomography (CT):** X-ray imaging reconstructed into cross-sectional attenuation information; CT numbers are commonly reported in Hounsfield units.
- **Digital Imaging and Communications in Medicine (DICOM):** The standard for medical-image information objects, encoding, files, and network services.
- **DICOM-RT:** Informal collective term for DICOM radiotherapy objects such as RT Structure Set, RT Plan, RT Dose, and RT treatment records.
- **Dose-volume histogram (DVH):** A summary relating structure volume to received dose; it discards spatial location.
- **Frame of reference:** The DICOM patient-based coordinate context used to relate spatial objects.
- **Hounsfield unit (HU):** A CT value relative to water and air under the scanner's reconstruction and calibration.
- **Image registration:** Estimation of a spatial transformation that aligns coordinate systems or corresponding anatomy across images.
- **Interpolation:** Estimation of values at unsampled locations during resampling; the appropriate method depends on whether values represent intensities, labels, or other quantities.
- **Modality:** An imaging or treatment technology, such as CT, magnetic resonance imaging, positron emission tomography, or proton therapy.
- **Ontology:** A formal representation of concepts and their relationships, used in part to harmonize names and meanings across datasets.
- **Pixel / voxel:** A sampled element in two-dimensional / three-dimensional image data. Its array index is not a physical coordinate without origin, orientation, and spacing.
- **Provenance:** Traceable information about the origin, processing, versions, and custody of data or an output.
- **Resampling:** Creating values on a new spatial grid using a defined coordinate transformation and interpolation method.
- **RT Dose:** A DICOM radiotherapy object representing a sampled dose distribution with geometry, units, scaling, and references.
- **RT Plan:** A DICOM radiotherapy object describing planned treatment geometry, technique, fractionation, and machine parameters, with referenced structures and related objects.
- **RT Structure Set (RTSTRUCT):** A DICOM radiotherapy object commonly representing named regions as contours tied to image geometry.
- **Segmentation object (SEG):** A DICOM object representing segment labels on referenced image frames.

## Radiation oncology

- **Absorbed dose:** Energy imparted by ionizing radiation per unit mass, measured in gray.
- **Adaptive radiotherapy (ART):** Reassessment and possible modification of a treatment course in response to anatomical, biological, or other changes; it is distinct from this book's name, ART101.
- **Brachytherapy:** Radiotherapy delivered using sealed radioactive sources placed in or near the treatment target.
- **Clinical target volume (CTV):** A tissue volume containing demonstrated disease and/or suspected microscopic disease that is intended to receive treatment.
- **Fraction:** One delivered portion of a prescribed radiotherapy course.
- **Gray (Gy):** The SI unit of absorbed dose, equal to one joule per kilogram.
- **Gross tumor volume (GTV):** Demonstrable extent of gross tumor, defined for the relevant clinical and imaging context.
- **Image-guided radiotherapy (IGRT):** Use of imaging at or near treatment to verify or correct patient, target, or delivery geometry.
- **Intensity-modulated radiotherapy (IMRT):** External-beam radiotherapy in which beam intensity is varied spatially to shape dose.
- **Monitor unit (MU):** A machine-specific quantity used to prescribe or record accelerator output under calibrated conditions; it is not itself absorbed dose.
- **Organ at risk (OAR):** Normal tissue whose radiation sensitivity can influence planning or treatment decisions.
- **Planning target volume (PTV):** A geometric concept used to account for uncertainties so the clinical target receives the intended dose under specified conditions.
- **Prescription:** The authorized clinical directive defining what is treated and the intended dose, fractionation, and relevant technique or constraints.
- **Quality assurance (QA):** Planned and systematic activities that provide confidence that requirements for quality and safety will be fulfilled.
- **Radiotherapy:** Clinical use of ionizing radiation to treat disease, commonly cancer.
- **Stereotactic body radiotherapy (SBRT):** Highly conformal, image-guided external-beam treatment delivered in a small number of fractions to an extracranial target; terminology and practice vary by jurisdiction and protocol.
- **Volumetric modulated arc therapy (VMAT):** Rotational IMRT delivered while machine parameters vary during gantry motion.

## Validation, safety, deployment, and regulation

- **Abstention:** A designed system response that withholds an ordinary prediction or action when stated conditions are not met; it still requires a safe workflow path.
- **Acceptance testing:** Verification that an installed system meets specified purchase, manufacturer, and institutional requirements before clinical commissioning.
- **Automation bias:** Tendency to favor an automated output despite contradictory information or insufficient evidence.
- **Change control:** A documented process for proposing, assessing, approving, testing, deploying, and if needed reversing a change.
- **Clinical utility:** Evidence that use of a system beneficially changes decisions, workflow, safety, outcomes, experience, or resource use for its intended setting.
- **Commissioning:** Institution-specific work that establishes that a system is understood, configured, tested, documented, and suitable for defined clinical use.
- **Drift:** Change over time in inputs, relationships, workflow, performance, or outcomes relevant to a deployed system.
- **Fairness:** Equitable design, access, performance, burden, and benefit across relevant groups; no single metric fully defines it.
- **Hazard:** A potential source of harm. **Risk** combines the probability and severity of harm under stated conditions.
- **Human factors:** Study and design of interactions among people, tools, tasks, organizations, and environments.
- **Intended use:** A bounded statement of users, population, inputs, output, clinical purpose, setting, and degree of automation.
- **Monitoring:** Planned measurement and review of deployed system behavior, context, performance, incidents, and outcomes against action thresholds.
- **Post-deployment surveillance:** Ongoing collection and assessment of safety and performance evidence after a system enters use.
- **Quality control (QC):** Operational techniques and measurements used to verify that specified quality requirements are met.
- **Regulation:** Legally enforceable rules within a jurisdiction. Regulator guidance, consensus guidance, standards, policy, and ethics carry different authority.
- **Retirement:** Controlled cessation of a system's use, including communication, fallback, access removal, record retention, and successor arrangements.
- **Rollback:** Return to a previously approved system version or workflow after a failed or unsafe change.
- **Silent evaluation:** Prospective operation on live data without exposing outputs to care decisions, used to assess local behavior before clinical influence.
- **Stop rule:** A prespecified condition that pauses or ends use, evaluation, or escalation and defines who acts and what fallback applies.
- **Technical performance:** Measured agreement of system outputs with a reference under a defined test design; it does not by itself establish clinical validity or utility.

## Usage and first-use convention

Use the expanded term followed by the abbreviation in parentheses at first use in each standalone chapter—for example, *organ at risk (OAR)*—then use the abbreviation consistently. Preserve capitalization for standards and named objects, but use sentence case for general concepts. Where communities use conflicting meanings, write the intended meaning explicitly; notable examples are development-set versus clinical *validation*, ART101 versus adaptive radiotherapy (ART), and quality assurance (QA) versus quality control (QC).
