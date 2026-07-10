# 7: AI for Treatment Planning

Treatment planning is a complex, iterative process that aims to deliver an optimal radiation dose to the target volume while minimizing dose to surrounding healthy tissues. This process traditionally requires significant expertise and time from medical physicists and dosimetrists. Deep learning approaches offer the potential to automate aspects of treatment planning, predict optimal dose distributions, and potentially improve plan quality and consistency while reducing planning time.

Planning models depend on correctly linked images, structures, prescriptions, plan versions, dose grids, and delivery records. See the canonical [radiotherapy data and informatics foundations](../medicalImaging/medicalImaging.md) for the object model, geometry and units, dose-grid alignment, cohort construction, and leakage-safe preprocessing used throughout this chapter.

## Dose Prediction Models

Dose prediction models use deep learning to estimate the radiation dose distribution that would result from a treatment plan, without performing the full physics-based dose calculation. These models can serve as rapid approximations or as components in automated planning systems.

### DVH Estimation

The Dose-Volume Histogram (DVH) is a fundamental tool in radiation therapy planning, summarizing the dose distribution within a structure as a curve showing the volume receiving at least a given dose. DVH-based metrics (e.g., V20 for lung, mean heart dose) are commonly used as plan evaluation criteria and predictors of toxicity risk.

Deep learning models for DVH estimation aim to predict these curves or metrics directly from patient anatomy and treatment parameters, without requiring a complete treatment plan. These models typically:

1. Take as input the patient's CT images, contours of target volumes and OARs, and potentially treatment parameters (e.g., prescription dose, treatment technique).

2. Output predicted DVH curves or specific DVH metrics for targets and OARs.

Architectures for DVH prediction include:

Convolutional neural networks (CNNs) that process 3D anatomical information to capture spatial relationships between structures.

Hybrid models that combine CNNs for feature extraction with fully connected layers to predict DVH points or parameters.

Graph neural networks that represent the spatial relationships between different anatomical structures and learn to predict their dosimetric interdependencies.

DVH prediction models can serve multiple purposes:

Pre-planning feasibility assessment: Quickly estimating whether dosimetric goals are achievable for a specific patient before detailed planning begins.

Plan quality evaluation: Comparing achieved DVHs against predicted "optimal" DVHs to identify potential improvements.

Treatment technique selection: Predicting DVHs for different modalities (e.g., IMRT vs. proton therapy) to guide the choice of technique.

The accuracy of DVH prediction models depends on the consistency of planning practices in the training data. These models essentially learn to mimic the planning patterns and trade-offs made by the institution that generated the training plans.

### Dose Distribution Prediction

Beyond summary DVH metrics, deep learning models can predict the full 3D dose distribution within the patient. These models map from patient anatomy (and potentially treatment parameters) to voxel-wise dose values throughout the planning volume.

Common architectures for dose prediction include:

U-Net and its variants, which have proven effective for this task due to their ability to capture both local and global anatomical context. The encoder pathway processes the input images and contours, while the decoder generates the predicted dose distribution.

Conditional Generative Adversarial Networks (cGANs), where the generator produces dose distributions conditioned on patient anatomy, and the discriminator learns to distinguish between real and generated dose distributions. This adversarial training can help produce more realistic dose distributions.

Attention-based architectures that learn to focus on the most relevant anatomical features for predicting dose at each location.

Dose prediction models face several challenges:

Handling the high dynamic range of dose values, which can span several orders of magnitude.
Accurately predicting dose in regions with complex tissue heterogeneity or at interfaces between different tissues.
Capturing the impact of different beam arrangements, which may not be explicitly provided as input.
Ensuring that predicted dose distributions satisfy physical constraints (e.g., dose cannot increase with depth beyond the build-up region for a single beam).

Despite these challenges, dose prediction models have shown promising results, with many achieving mean absolute errors of less than 5% of the prescription dose in most regions. These models can serve as rapid approximations for plan evaluation, as starting points for optimization, or as components in fully automated planning systems.

## Plan Quality Assessment

Evaluating the quality of radiation treatment plans is traditionally a manual process based on clinical experience and protocol-specific criteria. Deep learning approaches aim to automate and standardize this assessment, potentially improving plan consistency and quality.

### Automated Plan Evaluation

Automated plan evaluation models assess whether a treatment plan meets clinical goals and how it compares to historically "good" plans for similar cases. These models can:

Classify plans as acceptable or requiring improvement based on dosimetric and geometric features.
Score plans on a continuous scale, potentially highlighting specific aspects that could be improved.
Compare a plan against a database of previous plans for similar patients to identify potential outliers or areas for improvement.

Deep learning approaches to plan evaluation include:

Supervised classification or regression models trained on expert-labeled plans.
Anomaly detection models that identify unusual dose distributions or DVH characteristics.
Reinforcement learning frameworks that learn to evaluate plans based on clinical outcomes or expert preferences.

The features used for plan evaluation typically include:

DVH metrics for targets and OARs
Conformity and homogeneity indices
Spatial dose characteristics (e.g., gradient measures, hot spots)
Geometric relationships between dose distribution and anatomical structures

Automated plan evaluation can serve as a quality assurance tool, providing an objective second check of plans before approval. It can also help identify systematic differences in planning approaches between institutions or planners, potentially leading to standardization of best practices.

### Knowledge-based Planning

Knowledge-based planning (KBP) leverages historical treatment plans to predict achievable dose-volume objectives for new patients. While traditional KBP approaches often use statistical modeling, deep learning has enhanced these methods by capturing more complex relationships between patient anatomy and achievable dose distributions.

Deep learning-based KBP models typically:

1. Extract features from the patient's anatomy, particularly the spatial relationships between target volumes and OARs.

2. Predict achievable dose-volume constraints based on these features and a database of previously delivered plans.

3. Use these predictions to guide the optimization of new treatment plans.

Architectures for KBP include:

CNNs that process anatomical features to predict achievable dose metrics.
Recurrent neural networks (RNNs) that model the sequential nature of DVH curves.
Attention mechanisms that focus on the most relevant historical plans or anatomical features for a new patient.

KBP approaches have shown the ability to reduce planning time and improve plan quality, particularly for less experienced planners or centers. They can also help identify suboptimal plans by comparing achieved dose metrics against predicted achievable values.

The effectiveness of KBP models depends on the quality and diversity of the historical plans used for training. These models essentially learn to reproduce the planning patterns in their training data, which may not always represent optimal planning.

## Automated Treatment Planning

Fully automated treatment planning aims to generate complete, clinically acceptable plans with minimal human intervention. Deep learning approaches to automated planning range from enhancing specific steps in the planning workflow to end-to-end systems that generate deliverable plans directly from patient images and prescriptions.

### Knowledge-based Planning

Building on the KBP concepts discussed earlier, deep learning can automate the entire planning process by:

1. Predicting optimal dose distributions based on patient anatomy and prescription.

2. Generating beam parameters (angles, shapes, weights) that would produce the desired dose distribution.

3. Optimizing the final plan to meet clinical goals while ensuring deliverability.

Several approaches have been developed:

Two-stage models first predict an "ideal" dose distribution, then use inverse planning to determine the machine parameters needed to achieve it.

End-to-end models directly predict deliverable plan parameters from patient anatomy.

Hybrid approaches combine machine learning for certain steps (e.g., beam angle selection) with conventional optimization for others (e.g., fluence map optimization).

The advantages of automated planning include:

Reduced planning time, potentially enabling more adaptive approaches.
Consistent plan quality, reducing variability between planners.
Ability to rapidly explore multiple planning strategies.
Potential for improved plan quality by learning from the best examples in the training data.

Challenges include ensuring that the generated plans are physically deliverable, clinically acceptable across diverse patient anatomies, and robust to uncertainties in patient setup and internal motion.

### Reinforcement Learning Approaches

Reinforcement learning (RL) offers a promising framework for automated treatment planning, as it can directly optimize for clinical objectives without requiring labeled "optimal" plans for training. In an RL framework:

The state represents the current dose distribution, patient anatomy, and planning constraints.
Actions include adjusting beam parameters, optimization weights, or other planning variables.
Rewards are based on dosimetric criteria, conforming to clinical goals for target coverage and OAR sparing.

RL approaches to treatment planning include:

Beam angle selection, where the agent learns to sequentially select optimal beam directions.
Fluence map optimization, where the agent directly adjusts intensity patterns to optimize the dose distribution.
Multi-criteria optimization, where the agent learns to navigate trade-offs between competing objectives.

The advantage of RL is its ability to discover novel planning strategies that might not be present in historical data. However, challenges include:

Defining appropriate reward functions that accurately reflect clinical priorities.
Ensuring safe exploration during training, typically by using simulation environments.
Managing the large state and action spaces involved in treatment planning.

Research in RL for treatment planning is still emerging, with most applications focusing on specific aspects of the planning process rather than end-to-end solutions. As these methods mature, they could potentially discover novel planning approaches that outperform current clinical practice.

## Multi-criteria Optimization

Radiation therapy planning inherently involves balancing multiple competing objectives: maximizing tumor control while minimizing toxicity to various normal tissues. Multi-criteria optimization (MCO) explicitly addresses these trade-offs, and deep learning approaches are enhancing this process.

### Traditional MCO Approaches

Traditional MCO in radiation therapy generates a set of Pareto-optimal plans, where no objective can be improved without worsening another. Planners then navigate this Pareto surface to select a plan that best balances the clinical trade-offs.

Deep learning is enhancing MCO in several ways:

Predicting the Pareto surface more efficiently than generating multiple plans through conventional optimization.
Learning to navigate the Pareto surface based on historical planner preferences or clinical outcomes.
Identifying the most relevant trade-offs to explore for a specific patient anatomy.

Architectures for MCO include:

Generative models that can rapidly produce dose distributions at different points on the Pareto surface.
Recommendation systems that suggest promising regions of the Pareto surface to explore.
Interactive systems that learn from planner feedback to refine the presented trade-offs.

These approaches aim to make MCO more efficient and intuitive, potentially enabling more widespread clinical adoption of this powerful planning approach.

### Balancing Clinical Priorities

Beyond technical optimization, deep learning can help balance clinical priorities by:

Learning from historical decisions how different institutions or physicians weigh various clinical factors.
Predicting patient-specific risks of different toxicities to inform trade-off decisions.
Incorporating non-dosimetric factors (e.g., patient comorbidities, concurrent treatments) into planning decisions.

These approaches recognize that optimal planning involves more than just meeting generic dosimetric constraints—it requires considering the specific clinical context and patient characteristics.

## Current Research in Treatment Planning Prediction

Research in deep learning for treatment planning continues to advance rapidly, addressing remaining challenges and expanding capabilities.

### Plan Parameter Optimization

Current research in plan parameter optimization focuses on:

Beam angle optimization: Developing models that can predict optimal beam arrangements based on patient anatomy, potentially considering non-coplanar beams and novel delivery techniques.

Fluence map prediction: Directly predicting optimal fluence patterns that balance target coverage and OAR sparing, potentially reducing the need for iterative optimization.

Segment shape optimization: For direct machine parameter optimization, predicting deliverable multi-leaf collimator (MLC) shapes and weights.

Hyperparameter tuning: Automatically selecting optimization parameters (e.g., objective weights, priorities) that lead to high-quality plans.

These approaches aim to streamline the planning process by reducing the need for manual parameter selection and iterative refinement.

### Beam Angle Selection

Beam angle selection remains a challenging aspect of treatment planning, particularly for complex techniques like non-coplanar IMRT or VMAT. Deep learning approaches include:

Classification models that predict whether a potential beam angle would be beneficial for a specific patient.

Reinforcement learning agents that sequentially select beam angles to optimize overall plan quality.

Graph neural networks that model the geometric relationships between target volumes, OARs, and potential beam paths.

Attention-based models that learn to focus on the most relevant anatomical features for beam selection.

These models aim to automate a process that traditionally relies heavily on planner experience and can significantly impact plan quality.

### Adaptive Planning

Adaptive radiation therapy, where plans are modified during the treatment course to account for anatomical changes, presents unique challenges and opportunities for deep learning:

Predicting anatomical changes: Models that forecast how a patient's anatomy might change during treatment based on early observations, enabling proactive plan adaptation.

Automated replanning: Rapidly generating adapted plans based on new imaging, potentially enabling online adaptation.

Dose accumulation: Accurately estimating the total delivered dose across multiple fractions with changing anatomy.

Decision support: Predicting which patients would benefit most from plan adaptation based on observed anatomical changes.

These applications could help make adaptive radiotherapy more practical and widely available by reducing the time and resources required for replanning.

### Integration with Outcome Prediction

An emerging research direction is the integration of treatment planning with outcome prediction:

Outcome-aware planning: Directly optimizing plans to maximize predicted tumor control and minimize predicted toxicity, rather than using generic dosimetric constraints.

Personalized planning: Tailoring plans to individual patient characteristics that might affect radiosensitivity or toxicity risk.

Radiomics-guided planning: Using radiomic features extracted from pre-treatment images to identify tumor subregions that might benefit from dose escalation or de-escalation.

These approaches aim to move beyond one-size-fits-all planning to truly personalized radiation therapy that considers the unique characteristics of each patient and tumor.

As deep learning models for treatment planning continue to improve in accuracy, robustness, and clinical relevance, they hold the potential to significantly enhance the efficiency, consistency, and quality of radiation therapy planning. The integration of these models into clinical workflows, combined with appropriate quality assurance and human oversight, could ultimately improve outcomes for cancer patients receiving radiation therapy.
