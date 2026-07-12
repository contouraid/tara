# 2: Fundamentals of Artificial Intelligence through Deep Learning

## Before you begin

**Prerequisites:** Read [Chapter 1](../intro/intro.md), especially the {ref}`common clinical artificial intelligence (AI) lifecycle <common-ai-lifecycle>`. Complete beginners should also know from Chapters 3 and 4 what a radiotherapy task and its imaging data represent. Use the [cross-book glossary](../resources/glossary.md) for canonical definitions.

**Learning objectives:** After this chapter, you should be able to:

1. represent a prediction as features, weights, bias, activation, output, and loss;
2. explain at a conceptual level how forward propagation, backpropagation, and gradient-based optimization train a network;
3. compare convolutional, recurrent, autoencoder, generative adversarial, transformer, and U-Net families by the data relationship they encode;
4. select a plausible architecture and objective for classification, regression, generation, or segmentation; and
5. explain why architecture choice alone does not establish generalization, clinical utility, or safety.

**Reading route:** Technical readers can study the mathematics in sequence. Clinicians may focus first on the overview, loss functions, convolutional neural networks, transformers, U-Net, and recap. The companion pages cover [language models, generative AI, and agents](llm.md) and [vision-language models](vlm.md). In the recurring cases, this chapter explains the model components behind Case A's autocontour and the prediction or automation systems in Cases B and C.

---

## The Perceptron Model

The perceptron represents the fundamental building block of neural networks and serves as an excellent starting point for understanding how these complex systems function. Rosenblatt described its probabilistic model and learning system in 1958 [[1]](https://doi.org/10.1037/h0042519).

At its core, a perceptron takes multiple input signals, applies weights to these inputs, sums them together with a bias term, and then passes this sum through an activation function to produce an output. Mathematically, this can be represented as:

$$y = f\left(\sum_{i} w_i x_i + b\right)$$

Where $x_i$ represents the input features, $w_i$ represents the corresponding weights, $b$ is the bias term, and $f$ is the activation function. In the original perceptron model, the activation function was a simple step function that output 1 if the weighted sum exceeded a threshold and 0 otherwise.

The perceptron's significance lies in its ability to learn from data through a simple update rule. When the perceptron makes an incorrect prediction, the weights are adjusted proportionally to the error and the input values. This learning process continues until the perceptron correctly classifies all training examples or reaches a maximum number of iterations.

Despite its simplicity, the perceptron can solve linearly separable problems—those where a single straight line (or hyperplane in higher dimensions) can separate the different classes. This capability makes it suitable for basic classification tasks, such as distinguishing between different tissue types based on a few radiological features.

However, the perceptron has significant limitations. As Marvin Minsky and Seymour Papert demonstrated in their 1969 book "Perceptrons," a single perceptron cannot solve problems that are not linearly separable, such as the exclusive OR (XOR) problem. This limitation arises because a single perceptron can only represent a linear decision boundary.

In radiation oncology, many problems involve complex, non-linear relationships between features and outcomes. For instance, the relationship between radiation dose and tumor control probability follows a sigmoid curve rather than a straight line. Similarly, the interaction between dose distribution and normal tissue complication probability involves complex, non-linear relationships that a single perceptron cannot capture.

These limitations led to the development of multi-layer perceptrons (MLPs) or feedforward neural networks, which overcome the linear separability constraint by stacking multiple layers of perceptrons. This advancement, combined with effective training algorithms like backpropagation, paved the way for the deep learning revolution we see today.

Understanding the perceptron model provides a foundation for grasping more complex neural network architectures used in modern radiation oncology applications, from contouring organs at risk to predicting treatment outcomes based on multidimensional data.

---

## Feature Engineering and Selection

Feature engineering—the process of creating, transforming, and selecting relevant features from raw data—plays a crucial role in the success of traditional machine learning algorithms. While deep learning can learn representations jointly with a task, feature engineering remains important for structured data and interpretable models [[2]](https://www.deeplearningbook.org/).

Common feature engineering techniques include:

1. **Normalization and standardization**: Scaling features to a common range or distribution to prevent certain features from dominating the learning process due to their magnitude.

2. **Polynomial features**: Creating interaction terms between existing features to capture non-linear relationships.

3. **Discretization**: Converting continuous variables into categorical ones, which can sometimes reveal patterns not apparent in the continuous representation.

4. **Text and image processing**: Extracting meaningful features from unstructured data like medical reports or images.

Feature selection helps identify the most informative features while reducing dimensionality, which can improve model performance, reduce overfitting, and enhance interpretability. Methods include filter approaches (selecting features based on statistical measures), wrapper methods (evaluating feature subsets based on model performance), and embedded methods (incorporating feature selection into the model training process).

In radiation oncology, domain knowledge plays a vital role in feature engineering. Clinically relevant features might include dosimetric parameters (like V20 for lung or mean heart dose), anatomical measurements, or derived metrics that capture aspects of the dose distribution known to correlate with outcomes.

> **Figure suggestion:** Add a simple diagram of a perceptron showing inputs, weights, bias, activation function, and output.

---

## Activation Functions

Activation functions introduce non-linearity into neural networks. Without them, a stack of affine layers collapses to another affine transformation [[2]](https://www.deeplearningbook.org/).

### Comparison of Common Activation Functions

| Function      | Formula                                  | Output Range | Pros                        | Cons                        | Typical Use Cases           |
|---------------|------------------------------------------|--------------|-----------------------------|-----------------------------|-----------------------------|
| Sigmoid       | $\sigma(x) = \frac{1}{1+e^{-x}}$        | $(0, 1)$     | Probabilistic output        | Vanishing gradients         | Binary classification       |
| Tanh          | $\tanh(x) = \frac{e^{x}-e^{-x}}{e^{x}+e^{-x}}$ | $(-1, 1)$    | Zero-centered, smooth       | Vanishing gradients         | Hidden layers (legacy)      |
| ReLU          | $f(x) = \max(0, x)$                    | $[0, \infty)$ | Fast, less vanishing grad.  | Dying ReLU                  | Most hidden layers          |
| Leaky ReLU    | $f(x) = x$ if $x > 0$ else $\alpha x$ | $(-\infty, \infty)$ | Prevents dying ReLU         | Adds a parameter            | Hidden layers               |
| PReLU         | $\alpha$ learnable                     | $(-\infty, \infty)$ | Learns negative slope       | Slightly more complex       | Hidden layers               |
| Exponential linear unit (ELU) | $f(x) = x$ if $x > 0$ else $\alpha(e^{x}-1)$ | $(-\alpha, \infty)$ | Smooth, less bias shift | More computation | Hidden layers |
| Swish         | $f(x) = x \cdot \sigma(x)$             | $(-\infty, \infty)$ | Sometimes better than ReLU  | More computation            | Deep networks               |

### Sigmoid, Tanh, ReLU and Variants

The sigmoid function, defined as $\sigma(x) = \frac{1}{1 + e^{-x}}$, maps input values to the range $(0,1)$. This makes it interpretable as a probability, which is useful for binary classification problems. In early neural networks, sigmoid was a popular choice for hidden layer activations. However, it suffers from the "vanishing gradient problem" when used in deep networks—as inputs move away from zero, the gradient becomes extremely small, slowing down learning in earlier layers.

The hyperbolic tangent (tanh) function is similar to sigmoid but maps inputs to the range (-1,1), making the outputs zero-centered. This property often leads to faster convergence during training compared to sigmoid. Like sigmoid, tanh also suffers from the vanishing gradient problem in deep networks.

The Rectified Linear Unit (ReLU), defined as $f(x) = \max(0,x)$, has become the most widely used activation function in modern deep learning. ReLU simply outputs the input if it's positive and zero otherwise. Its advantages include computational efficiency (requiring only a simple threshold operation) and reduced likelihood of vanishing gradients for positive inputs. However, ReLU can suffer from the "dying ReLU" problem, where neurons can become permanently inactive if they consistently receive negative inputs.

Several variants of ReLU have been developed to address its limitations:

Leaky ReLU allows a small gradient when the input is negative ($f(x) = \alpha x$ for $x < 0$, where $\alpha$ is a small constant like 0.01), preventing neurons from "dying".

Parametric ReLU (PReLU) makes the slope for negative inputs a learnable parameter, allowing the model to determine the optimal value during training.

Exponential Linear Unit (ELU) uses an exponential function for negative inputs, providing smoother transitions and potentially better performance in some applications.

Swish, defined as $f(x) = x \cdot \sigma(x)$, was discovered through automated search and has shown promising results in deep networks.

In radiation oncology applications, the choice of activation function can significantly impact model performance. For instance, in dose prediction models, ReLU and its variants might be preferred for hidden layers due to their training efficiency, while sigmoid activations might be used in the output layer to constrain dose predictions to a reasonable range.

### Properties and Use Cases

Different activation functions have distinct properties that make them suitable for specific use cases:

Output range considerations: Sigmoid and tanh have bounded outputs, making them suitable for problems where predictions should fall within a specific range. In contrast, ReLU has an unbounded positive range, which can be advantageous for modeling quantities like radiation dose that cannot be negative but have no theoretical upper limit.

Gradient behavior: The gradient of sigmoid and tanh approaches zero for inputs with large magnitude, potentially causing training to stall. ReLU has a constant gradient of 1 for positive inputs, facilitating more stable training in deep networks.

Computational efficiency: ReLU and its variants are computationally efficient, requiring simple operations compared to the exponential calculations in sigmoid and tanh. This efficiency becomes significant when training large models on medical imaging data.

Sparsity promotion: ReLU activations naturally induce sparsity in neural networks, as they output exactly zero for negative inputs. This sparsity can be beneficial for model regularization and interpretability, potentially important considerations in medical applications where understanding model behavior is crucial.

In practice, modern deep learning architectures for radiation oncology applications typically use ReLU or its variants for hidden layers due to their training efficiency and effectiveness. For output layers, the activation function is chosen based on the specific task:

Sigmoid for binary classification (e.g., tumor vs. normal tissue)
Softmax for multi-class classification (e.g., multiple organ segmentation)
Linear (no activation) for regression tasks (e.g., dose prediction)
ReLU or similar for outputs that must be non-negative (e.g., dose-volume histograms)

Understanding the properties of different activation functions helps in designing effective neural network architectures for specific radiation oncology applications and in diagnosing issues that may arise during training.

---

## Feedforward Neural Networks

Feedforward neural networks, also known as multi-layer perceptrons (MLPs), pass information from input to output without recurrent connections [[2]](https://www.deeplearningbook.org/).

### Architecture and Layers

The architecture of a feedforward neural network is defined by its layer structure:

The input layer receives the raw features or data. In radiation oncology applications, these might include patient characteristics, dosimetric parameters, or flattened image data. The number of neurons in this layer corresponds to the dimensionality of the input data.

Hidden layers perform intermediate computations and transformations. Each hidden layer consists of multiple neurons, with each neuron connected to all neurons in the previous layer (fully connected or dense layers). The number of hidden layers and neurons per layer are hyperparameters that significantly impact the network's capacity and performance. Deeper networks (more layers) can learn more complex hierarchical representations but may be more difficult to train and prone to overfitting, especially with limited data.

The output layer produces the final prediction or classification. Its structure depends on the specific task:
- For binary classification (e.g., malignant vs. benign), a single neuron with sigmoid activation is typically used.
- For multi-class classification (e.g., organ segmentation), multiple neurons with softmax activation provide class probabilities.
- For regression tasks (e.g., dose prediction), one or more neurons with linear or appropriate bounded activation functions output the predicted values.

The connections between layers are represented by weight matrices, with each weight indicating the strength of the connection between two neurons. Additionally, each neuron (except in the input layer) has a bias term that allows the activation function to shift, providing greater flexibility in modeling.

In radiation oncology, feedforward neural networks have been applied to various problems, including predicting treatment outcomes, estimating toxicity risks, and serving as building blocks for more complex architectures used in image analysis and treatment planning.

### Forward and Backward Propagation

The operation of feedforward neural networks involves two key processes: forward propagation and backward propagation.

Forward propagation is the process of computing the network's output given an input. For each layer, the weighted sum of inputs from the previous layer is calculated, the bias term is added, and the result is passed through the activation function. This process continues layer by layer until reaching the output. Mathematically, for layer $l$:

$$Z^{(l)} = W^{(l)}a^{(l-1)} + b^{(l)}$$
$$a^{(l)} = f(Z^{(l)})$$

Where $W^{(l)}$ is the weight matrix, $a^{(l-1)}$ is the activation from the previous layer, $b^{(l)}$ is the bias vector, $f$ is the activation function, $Z^{(l)}$ is the weighted input, and $a^{(l)}$ is the activation output.

Backward propagation (backpropagation) is the process of computing gradients of the loss function with respect to the network parameters (weights and biases). These gradients indicate how to adjust the parameters to reduce the error. The process starts at the output layer by computing the error derivative with respect to the output, then works backward through the network using the chain rule of calculus.

For the output layer, the gradient depends on the difference between predicted and actual values, modified by the derivative of the activation function. For hidden layers, the gradient depends on the weighted sum of gradients from the subsequent layer, again modified by the activation function derivative.

Once gradients are computed, parameters are updated using an optimization algorithm like gradient descent:

$$W^{(l)} = W^{(l)} - \alpha \frac{\partial L}{\partial W^{(l)}}$$
$$b^{(l)} = b^{(l)} - \alpha \frac{\partial L}{\partial b^{(l)}}$$

Where $\alpha$ is the learning rate and $\frac{\partial L}{\partial W^{(l)}}$ and $\frac{\partial L}{\partial b^{(l)}}$ are the gradients of the loss function with respect to the weights and biases.

In radiation oncology applications, efficient and accurate backpropagation is crucial for training models that can reliably predict treatment outcomes or generate accurate contours. The complexity of the data and the critical nature of the predictions make proper training essential.

---

## Loss Functions

Loss functions quantify the difference between a model's predictions and the ground truth, providing a signal for how to adjust the model parameters during training. The choice of loss function significantly impacts what the model learns and how it performs on different types of errors.

### Summary Table: Loss Functions

| Name                | Formula                                    | Typical Use Case                | Notes                                  |
|---------------------|--------------------------------------------|---------------------------------|----------------------------------------|
| Mean Squared Error  | $MSE = \frac{1}{n}\sum_i (y_i - \hat{y}_i)^2$ | Regression (e.g., dose prediction) | Sensitive to outliers                  |
| Cross-Entropy       | See text                                   | Classification                   | Penalizes confident wrong predictions  |
| Focal Loss          | See text                                   | Imbalanced classification/segmentation | Down-weights easy examples        |
| Dice Loss           | $DL = 1 - \frac{2\sum(y_i \cdot \hat{y}_i)}{\sum y_i + \sum \hat{y}_i}$ | Segmentation                     | Directly optimizes overlap             |
| Hausdorff Loss      | See text                                   | Segmentation (boundaries)         | Focuses on boundary accuracy           |
| Combined Losses     | Weighted sum                               | Complex tasks                    | E.g., Cross-Entropy + Dice             |

### Mean Squared Error

Mean Squared Error (MSE) is one of the most common loss functions for regression problems. It calculates the average of the squared differences between predicted and actual values:

$$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

Where $y_i$ is the true value, $\hat{y}_i$ is the predicted value, and $n$ is the number of samples.

MSE heavily penalizes large errors due to the squaring operation, making it particularly sensitive to outliers. This property can be both an advantage and a disadvantage, depending on the application. In radiation oncology, MSE might be appropriate for dose prediction tasks where large deviations could have significant clinical consequences. However, its sensitivity to outliers could be problematic when working with noisy medical data.

A variant of MSE is the Root Mean Squared Error (RMSE), which takes the square root of the MSE. This brings the error metric back to the same scale as the original data, making it more interpretable in the context of the specific problem.

### Cross-entropy

Cross-entropy loss is the standard choice for classification problems. For binary classification, it is defined as:

$$BCE = -\frac{1}{n} \sum_{i=1}^{n} \left[y_i \log(\hat{y}_i) + (1-y_i) \log(1-\hat{y}_i)\right]$$

Where $y_i$ is the true label (0 or 1), and $\hat{y}_i$ is the predicted probability of class 1.

For multi-class classification, categorical cross-entropy is used:

$$CCE = -\frac{1}{n} \sum_{i=1}^{n} \sum_{j=1}^{C} y_{ij} \log(\hat{y}_{ij})$$

Where $y_{ij}$ is 1 if sample $i$ belongs to class $j$ and 0 otherwise, and $\hat{y}_{ij}$ is the predicted probability that sample $i$ belongs to class $j$.

Cross-entropy has several desirable properties for classification tasks. It heavily penalizes confident but wrong predictions, encouraging the model to output calibrated probabilities. It also produces larger gradients for misclassified examples compared to squared error, potentially leading to faster learning.

In radiation oncology, cross-entropy is commonly used for classification tasks like tumor detection or organ segmentation (when framed as pixel-wise classification). However, for segmentation tasks, it's often combined with other loss functions to address class imbalance issues, as we'll discuss next.

### Focal Loss and Specialized Functions

Standard loss functions may not be optimal for all problems in radiation oncology. Specialized loss functions have been developed to address specific challenges:

Focal Loss modifies cross-entropy to address class imbalance by down-weighting well-classified examples. It's defined as:

$$FL = -\frac{1}{n} \sum_{i=1}^{n} \left[\alpha (1-\hat{y}_i)^\gamma y_i \log(\hat{y}_i) + (1-\alpha) \hat{y}_i^\gamma (1-y_i) \log(1-\hat{y}_i)\right]$$

Where $\alpha$ balances the importance of positive/negative examples, and $\gamma$ is a focusing parameter that reduces the loss contribution from easy examples. Focal loss is particularly useful in medical image segmentation where background pixels often vastly outnumber the pixels belonging to structures of interest.

Dice Loss is based on the Dice similarity coefficient, a metric commonly used to evaluate segmentation quality. It's defined as:

$$DL = 1 - \frac{2 \sum (y_i \cdot \hat{y}_i)}{\sum y_i + \sum \hat{y}_i}$$

Dice loss directly optimizes for overlap between predicted and ground truth segmentations, making it well-suited for medical image segmentation tasks like organ contouring in radiation therapy planning.

Hausdorff Distance-based losses incorporate distance metrics between predicted and ground truth boundaries. These are particularly relevant for radiation oncology, where the precise delineation of boundaries between tumors and organs at risk is critical for treatment planning.

Boundary-aware losses place greater emphasis on accurately predicting the boundaries between different structures, which is crucial for precise contouring in radiation therapy.

Combined losses often yield the best results for complex tasks. For instance, a weighted combination of cross-entropy and Dice loss can balance pixel-wise accuracy with overall segmentation quality. Similarly, adding regularization terms to the loss function can encourage desirable properties like smoothness in contours or dose distributions.

In radiation oncology applications, the choice of loss function should be guided by clinical considerations. For example, in treatment planning, certain types of errors (like underdosing the tumor or overdosing critical structures) may have more severe consequences than others, suggesting the need for asymmetric loss functions that penalize these errors more heavily.

---

## Gradient-based Learning

Gradient-based learning uses derivatives of an objective to update trainable parameters. Backpropagation efficiently applies the chain rule through a network and underpins modern multilayer representation learning [[3]](https://doi.org/10.1038/323533a0).

### Backpropagation Algorithm

Backpropagation is the fundamental algorithm for efficiently computing gradients in neural networks. While we introduced it briefly earlier, let's explore it in more detail:

The algorithm consists of two main phases:

1. Forward pass: Input data is propagated through the network to compute predictions and the resulting loss.

2. Backward pass: The gradient of the loss with respect to each parameter is computed by working backward from the output layer to the input layer.

The key insight of backpropagation is the efficient computation of these gradients using the chain rule of calculus. Rather than computing each gradient independently, intermediate results are cached and reused, dramatically reducing the computational cost.

For a given layer $l$, the gradient of the loss $L$ with respect to the weights $W^{(l)}$ is:

$$\frac{\partial L}{\partial W^{(l)}} = \frac{\partial L}{\partial Z^{(l)}} \cdot \frac{\partial Z^{(l)}}{\partial W^{(l)}} = \delta^{(l)} (a^{(l-1)})^T$$

Where $\delta^{(l)} = \frac{\partial L}{\partial Z^{(l)}}$ is the "error" at layer $l$, and $a^{(l-1)}$ is the activation from the previous layer.

The error term $\delta^{(l)}$ is computed recursively:

For the output layer: $\delta^{(L)} = \frac{\partial L}{\partial a^{(L)}} \odot f'(Z^{(L)})$

For hidden layers: $\delta^{(l)} = ((W^{(l+1)})^T \delta^{(l+1)}) \odot f'(Z^{(l)})$

Where $\odot$ represents element-wise multiplication, and $f'$ is the derivative of the activation function.

This recursive computation allows the error signal to propagate backward through the network, with each layer's parameters receiving gradients that indicate how they contributed to the final error.

In radiation oncology applications, backpropagation enables models to learn complex relationships between input data such as computed tomography (CT) or magnetic resonance imaging (MRI) and output targets such as organ contours or dose distributions. The efficiency of backpropagation makes it practical to train deep networks on the large, high-dimensional datasets typical in medical imaging.

### Computational Graphs

Computational graphs provide a powerful framework for understanding and implementing backpropagation. A computational graph represents a mathematical expression as a directed graph where nodes are operations and edges represent data flowing between operations.

For example, a simple neural network layer computing a = f(Wx + b) would be represented as a graph with nodes for matrix multiplication, addition, and the activation function, with edges showing how data flows through these operations.

Computational graphs make the dependencies between variables explicit, facilitating the automatic computation of gradients. Modern deep learning frameworks like TensorFlow and PyTorch use computational graphs (either static or dynamic) to implement automatic differentiation, relieving developers from having to manually derive and implement gradient calculations.

The forward pass through the graph computes the output values, while the backward pass computes gradients by applying the chain rule at each node. Each node knows how to compute the gradient of the output with respect to its inputs, given the gradient of the output with respect to its output.

In complex models for radiation oncology applications, computational graphs can become quite large, with thousands or millions of operations. Automatic differentiation through these graphs enables the training of sophisticated models for tasks like multi-organ segmentation or dose prediction without requiring manual derivation of gradients.

Understanding computational graphs also helps in diagnosing and addressing training issues, as it provides insight into how gradients flow through the network and where problems like vanishing or exploding gradients might occur.

---

## Initialization Strategies

Initialization affects signal and gradient propagation. Xavier/Glorot initialization was developed for symmetric activations [[4]](https://proceedings.mlr.press/v9/glorot10a.html), while He initialization adapts the variance calculation to rectifiers [[5]](https://doi.org/10.1109/ICCV.2015.123).

### Summary Table: Initialization Methods

| Method         | Formula/Approach                           | Best For                | Notes                                 |
|----------------|--------------------------------------------|-------------------------|---------------------------------------|
| Random         | Uniform or Normal distribution              | Shallow nets            | Can cause vanishing/exploding gradients|
| Xavier/Glorot  | $\text{Var}(W) = \frac{2}{n_{\text{in}}+n_{\text{out}}}$ | Tanh/Sigmoid activations| Balances variance across layers       |
| He             | $\text{Var}(W) = \frac{2}{n_{\text{in}}}$ | ReLU activations        | Prevents vanishing gradients          |
| Orthogonal     | Orthogonal matrix                          | Deep/recurrent nets     | Preserves gradient magnitude          |
| Identity       | Close to identity matrix                   | Residual nets           | Preserves input features              |
| Pretrained     | From other tasks/datasets                  | Transfer learning       | Leverages external data               |

The initial values of neural network parameters significantly impact training dynamics and final performance. Poor initialization can lead to slow convergence, getting stuck in poor local minima, or even failure to train due to vanishing or exploding gradients.

### Random Initialization

Simple random initialization from a uniform or normal distribution was used in early neural networks. However, this approach often leads to suboptimal training, especially in deep networks.

Xavier/Glorot initialization, proposed by Xavier Glorot and Yoshua Bengio, draws weights from a distribution with variance scaled according to the number of input and output connections:

$$\text{Var}(W) = \frac{2}{n_{\text{in}} + n_{\text{out}}}$$

This scaling helps maintain the variance of activations and gradients across layers, preventing them from growing or shrinking exponentially with network depth.

He initialization, developed by Kaiming He, modifies Xavier initialization for ReLU activations:

$$\text{Var}(W) = \frac{2}{n_{\text{in}}}$$

This accounts for the fact that ReLU activations effectively reduce the variance by setting negative values to zero.

In radiation oncology applications, proper initialization is crucial for training deep networks on limited medical data. Good initialization can lead to faster convergence and better final performance, which is particularly important when working with the complex, high-dimensional data typical in medical imaging.

### Specialized Initialization Methods

Beyond standard methods, specialized initialization strategies have been developed for specific architectures and problems:

Orthogonal initialization sets weight matrices to be orthogonal, which helps preserve gradient magnitudes during backpropagation. This can be particularly useful in very deep networks or recurrent architectures.

Identity initialization, where weight matrices start close to the identity matrix, has shown benefits in residual networks by initially preserving the input features and allowing the network to gradually learn transformations.

Pretrained initialization uses weights from models trained on related tasks or larger datasets. This transfer learning approach is especially valuable in medical imaging, where labeled data may be limited. For example, a segmentation model for radiation therapy planning might initialize with weights from a network pretrained on general medical image segmentation tasks.

In radiation oncology applications, the choice of initialization strategy should consider the network architecture, activation functions, and the specific characteristics of the data. Proper initialization can help models converge to better solutions, particularly when working with the limited datasets often available in medical applications.

---

## Batch Normalization

Batch normalization standardizes mini-batch activation statistics and learns a subsequent scale and offset. Ioffe and Szegedy introduced the method and reported faster optimization in the architectures they tested [[6]](https://proceedings.mlr.press/v37/ioffe15.html); benefit in a new task remains empirical rather than guaranteed.

### How Batch Normalization Works

BatchNorm normalizes the pre-activation values of a layer by subtracting the batch mean and dividing by the batch standard deviation:

$$\hat{x} = \frac{x - \mu_B}{\sqrt{\sigma_B^2 + \varepsilon}}$$

Where $\mu_B$ and $\sigma_B^2$ are the mean and variance of the current mini-batch, and $\varepsilon$ is a small constant for numerical stability.

After normalization, BatchNorm applies a learnable scale and shift:

$$y = \gamma \hat{x} + \beta$$

Where $\gamma$ and $\beta$ are learnable parameters that allow the network to undo the normalization if necessary.

During training, BatchNorm uses mini-batch statistics for normalization. During inference, it uses running estimates of the population mean and variance accumulated during training.

### Benefits of Batch Normalization

BatchNorm offers several advantages that make it particularly valuable for training deep networks:

Reduced internal covariate shift: By normalizing layer inputs, BatchNorm reduces the changes in distribution that hidden layers experience as earlier layers update during training. This stabilizes the learning process.

Faster training: BatchNorm often allows the use of higher learning rates and reduces the number of epochs required for convergence.

Regularization effect: The noise introduced by estimating statistics from mini-batches acts as a form of regularization, potentially reducing the need for dropout or weight decay.

Reduced sensitivity to initialization: BatchNorm makes networks less sensitive to the choice of initialization scheme, as it normalizes the activations regardless of their initial scale.

In radiation oncology applications, these benefits can be particularly valuable when training complex models on limited data. The stabilizing effect of BatchNorm can help models converge to better solutions, while its regularization effect can reduce overfitting on small medical datasets.

### Considerations for Medical Applications

While BatchNorm is widely used, there are some considerations specific to medical applications:

Batch size dependency: BatchNorm's performance depends on having reasonably sized mini-batches to estimate statistics. In medical imaging, where high-resolution 3D images may limit batch sizes due to memory constraints, alternatives like Group Normalization or Instance Normalization might be more appropriate.

Domain shift: When applying models to data from different institutions or scanners, the statistics used by BatchNorm may no longer be appropriate. Techniques like Adaptive BatchNorm or Domain Adaptation methods may be needed to address this issue.

Inference consistency: In clinical applications where reproducibility is crucial, the stochasticity introduced by BatchNorm during training needs to be carefully managed to ensure consistent inference results.

Despite these considerations, BatchNorm or its variants are commonly used in deep learning models for radiation oncology applications, contributing to more stable and efficient training of complex architectures for tasks like organ segmentation and dose prediction.

---

## Convolutional Neural Networks (CNNs)

Convolutional neural networks (CNNs) use shared local filters and hierarchical representations for grid-like data such as images [[7]](https://doi.org/10.1038/nature14539). They are commonly used in radiotherapy image analysis, but architecture choice alone does not establish clinical performance.

### Convolutional Layers and Operations

The convolutional layer is the core building block of CNNs. Unlike fully connected layers that connect each neuron to every neuron in the previous layer, convolutional layers use a set of learnable filters (or kernels) that slide across the input, computing dot products between the filter weights and the input values at each spatial position. This operation, called convolution, can be mathematically represented as:

$$(I * K)(x, y) = \sum_{m} \sum_{n} I(x-m, y-n) K(m, n)$$

Where $I$ is the input, $K$ is the kernel, and $(x, y)$ represents spatial coordinates.

Each filter in a convolutional layer detects specific patterns or features, such as edges, textures, or more complex structures in deeper layers. The key properties that make convolutional layers particularly effective for image processing include:

Parameter sharing: The same filter weights are applied across the entire input, dramatically reducing the number of parameters compared to fully connected layers. This makes CNNs more efficient and less prone to overfitting, especially important when working with limited medical imaging datasets.

Local connectivity: Each neuron connects only to a small region of the input (the receptive field), reflecting the local nature of many image features. This mimics how the human visual system processes information and helps the network focus on relevant local patterns.

Translation invariance: Features can be detected regardless of their position in the image, making CNNs robust to spatial translations of the input. This is particularly valuable in medical imaging, where anatomical structures may appear in different locations across patients.

In radiation oncology applications, convolutional layers can learn to identify relevant anatomical structures, tumor boundaries, and tissue characteristics from CT, MRI, or PET images. The hierarchical feature learning in CNNs—from simple edges in early layers to complex anatomical patterns in deeper layers—aligns well with the multi-scale nature of medical image analysis.

### Pooling Layers

Pooling layers reduce the spatial dimensions of feature maps, providing several benefits:

Dimensionality reduction: By downsampling the feature maps, pooling reduces the computational load and memory requirements of the network. This is particularly important when working with high-resolution medical images.

Translation invariance: Pooling increases the network's robustness to small translations or distortions in the input, as the exact location of a feature becomes less important after pooling.

Increasing receptive field: By reducing spatial dimensions, pooling allows neurons in subsequent layers to "see" a larger portion of the original input, helping the network capture larger-scale patterns.

The most common pooling operations include:

Max pooling: Takes the maximum value within each pooling window, effectively selecting the strongest feature response. This is the most widely used pooling operation due to its simplicity and effectiveness.

Average pooling: Computes the average value within each pooling window, preserving more information but potentially diluting strong feature activations.

In modern CNN architectures for medical imaging, max pooling is commonly used after convolutional layers to progressively reduce spatial dimensions while preserving the most salient features. However, in segmentation networks like U-Net, which are widely used in radiation oncology for contouring, the spatial information lost during pooling must be recovered through upsampling or transposed convolutions in the decoder path.

### CNN Architectures

The field of CNN architecture design has evolved rapidly, with numerous influential models that have progressively improved performance on image analysis tasks:

LeNet, developed by Yann LeCun in the late 1990s, was one of the earliest CNN architectures, designed for handwritten digit recognition. It established the basic pattern of alternating convolutional and pooling layers followed by fully connected layers.

AlexNet, which won the ImageNet competition in 2012, marked the beginning of the deep learning revolution in computer vision. It featured deeper layers, ReLU activations, and techniques like dropout and data augmentation to prevent overfitting.

VGG networks, introduced in 2014, used very small (3×3) convolutional filters throughout the network, showing that depth was more important than filter size for learning complex features. The simplicity and uniformity of VGG's design made it a popular choice for transfer learning in medical imaging.

ResNet (Residual Network) addressed the degradation problem in very deep networks by introducing skip connections that allow gradients to flow more easily during backpropagation. These residual connections enable the training of networks with hundreds of layers, significantly increasing model capacity without suffering from vanishing gradients.

DenseNet took the concept of skip connections further by connecting each layer to every other layer in a feed-forward fashion. This dense connectivity pattern encourages feature reuse and improves gradient flow, resulting in more efficient parameter usage.

EfficientNet optimized both network depth and width using a compound scaling method, achieving state-of-the-art performance with fewer parameters. This efficiency is particularly valuable in medical applications where computational resources may be limited.

In radiation oncology, these architectures have been adapted for tasks like tumor detection, organ segmentation, and treatment response prediction. The choice of architecture depends on factors like the specific task, available data, computational resources, and the need for real-time performance in clinical settings.

### Transfer Learning with CNNs

Transfer learning leverages knowledge gained from one task to improve performance on another, related task. In the context of CNNs, this typically involves:

1. Pretraining a network on a large dataset (like ImageNet) where data is abundant
2. Transferring the learned weights to a new network for the target task
3. Fine-tuning some or all of the weights on the target dataset

This approach is particularly valuable in medical imaging, where labeled data is often scarce. By starting with weights pretrained on natural images, models can leverage general visual features (edges, textures, shapes) that transfer well to medical images, despite the domain difference.

Several transfer learning strategies exist:

Feature extraction: The pretrained network is used as a fixed feature extractor, with only the final classification layers trained on the new task. This approach works well when the target dataset is small and similar to the pretraining dataset.

Fine-tuning: Some or all of the pretrained weights are updated during training on the new task. Typically, earlier layers (which capture more generic features) are frozen or updated with a smaller learning rate, while later layers (which capture more task-specific features) are fully fine-tuned.

Domain adaptation: Specific techniques are applied to address the domain shift between the pretraining data (e.g., natural images) and the target data (e.g., medical images). These might include adversarial training or specific loss functions designed to align feature distributions.

In radiation oncology, transfer learning has been successfully applied to various tasks, including organ segmentation, tumor classification, and treatment response prediction. For example, a CNN pretrained on natural images might be fine-tuned to segment organs at risk in CT scans, with the early layers capturing general image features and the later layers adapting to the specific characteristics of CT imaging and anatomical structures.

The effectiveness of transfer learning in medical imaging depends on several factors:

The similarity between the source and target domains
The amount of available target data
The complexity of the target task
The architecture of the pretrained model

When properly applied, transfer learning can significantly reduce the amount of labeled data needed for training, accelerate convergence, and improve final performance—all crucial advantages in the data-limited domain of radiation oncology.

**Clinical vignette:** In a recent study, a CNN-based model was used to automatically segment organs at risk in pelvic CT scans, reducing contouring time by 70% and improving consistency between clinicians.

---

## Recurrent Neural Networks (RNNs)

Recurrent neural networks (RNNs) maintain a state while processing sequential inputs. Long short-term memory introduced gated memory to address difficult long-range credit assignment in conventional recurrent networks [[8]](https://doi.org/10.1162/neco.1997.9.8.1735). Proposed radiotherapy uses remain task-specific hypotheses until validated on representative temporal data.

### Sequential Data Processing

RNNs process sequential data by maintaining an internal state (or "memory") that captures information from previous time steps. At each step, the network takes both the current input and its previous state to produce an output and update the state. This recurrent connection allows information to persist across the sequence.

The basic RNN computation can be expressed as:

$$h_t = f(W_{xh} x_t + W_{hh} h_{t-1} + b_h)$$
$$y_t = g(W_{hy} h_t + b_y)$$

Where:
- $x_t$ is the input at time step $t$
- $h_t$ is the hidden state at time step $t$
- $y_t$ is the output at time step $t$
- $W_{xh}, W_{hh}, W_{hy}$ are weight matrices
- $b_h, b_y$ are bias vectors
- $f$ and $g$ are activation functions

This recurrent structure enables RNNs to model dependencies between elements in a sequence, making them suitable for tasks like:

Time series prediction: Forecasting future values based on past observations, such as predicting tumor response based on sequential imaging or biomarker measurements.

Sequence classification: Assigning a label to an entire sequence, such as classifying a patient's treatment trajectory as responding or non-responding.

Sequence generation: Producing sequential outputs, such as generating synthetic treatment plans or patient trajectories for simulation.

In radiation oncology, sequential data appears in various forms: the progression of tumor response over a treatment course, longitudinal patient monitoring data, or even the spatial progression through slices of a 3D volume when computational constraints prevent processing the entire volume at once.

### Vanishing/Exploding Gradients

Despite their theoretical ability to capture long-range dependencies, basic RNNs suffer from the vanishing and exploding gradient problems during training:

Vanishing gradients occur when the gradients become extremely small as they're propagated back through time steps, effectively preventing the network from learning long-range dependencies. This happens because the repeated multiplication of small values (less than 1) during backpropagation causes gradients to decay exponentially.

Exploding gradients represent the opposite problem, where gradients grow exponentially large, causing unstable training and parameter updates that overshoot optimal values. This typically occurs when weights are large (greater than 1).

These issues are particularly problematic for long sequences, as the effects compound with each time step. In radiation oncology applications, this could limit the ability to model long-term dependencies in treatment response or patient monitoring data spanning many weeks or months.

Several techniques have been developed to address these issues:

Gradient clipping prevents exploding gradients by scaling gradients when their norm exceeds a threshold.

Careful weight initialization helps establish initial conditions that mitigate both vanishing and exploding gradients.

Skip connections or residual connections provide shortcuts for gradient flow, similar to their use in deep CNNs.

However, the most effective solution has been the development of specialized RNN architectures like LSTM and GRU, which we'll discuss next.

### Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU) Architectures

Long Short-Term Memory (LSTM) networks were designed specifically to address the vanishing gradient problem in RNNs. LSTMs introduce a more complex cell structure with three gates that regulate information flow:

The forget gate determines what information to discard from the cell state.
The input gate decides what new information to store in the cell state.
The output gate controls what parts of the cell state to output.

This gating mechanism allows LSTMs to preserve information over many time steps when needed, while also being able to update or forget information when appropriate. Mathematically, the LSTM operations can be expressed as:

$$f_t = \sigma(W_f [h_{t-1}, x_t] + b_f)$$ (Forget gate)

$$i_t = \sigma(W_i [h_{t-1}, x_t] + b_i)$$ (Input gate)

$$o_t = \sigma(W_o [h_{t-1}, x_t] + b_o)$$ (Output gate)

$$\tilde{c}_t = \tanh(W_c [h_{t-1}, x_t] + b_c)$$ (Candidate cell state)

$$c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t$$ (Cell state update)

$$h_t = o_t \odot \tanh(c_t)$$ (Hidden state output)

Where $\sigma$ is the sigmoid function, $\odot$ represents element-wise multiplication, and $[h_{t-1}, x_t]$ denotes concatenation.

Gated Recurrent Units (GRUs) are a simplified variant of LSTMs with fewer parameters. GRUs combine the forget and input gates into a single "update gate" and merge the cell state and hidden state. This simplification makes GRUs computationally more efficient while often achieving comparable performance to LSTMs.

In radiation oncology applications, LSTMs and GRUs can model complex temporal patterns in treatment response, capture long-term dependencies in patient monitoring data, or process 3D volumes slice by slice while maintaining spatial context across slices. For example, an LSTM might analyze a sequence of tumor measurements during treatment to predict the final response or to identify patients who might benefit from treatment adaptation.

The choice between LSTM and GRU often depends on the specific application, with GRUs being more efficient but LSTMs potentially offering more modeling capacity for complex sequences. In practice, both architectures significantly outperform basic RNNs for most tasks involving long-range dependencies.

**Clinical vignette:** An RNN was used to analyze weekly tumor volume measurements during radiotherapy, predicting which patients were likely to benefit from adaptive treatment plans.

---

## Autoencoders

Autoencoders are neural networks designed to learn efficient representations of data in an unsupervised manner. Their architecture consists of an encoder that compresses the input into a lower-dimensional latent space and a decoder that reconstructs the original input from this compressed representation. This structure makes autoencoders particularly useful for dimensionality reduction, feature learning, and generative modeling.

### Dimensionality Reduction

One of the primary applications of autoencoders is dimensionality reduction—transforming high-dimensional data into a lower-dimensional representation while preserving essential information. Unlike traditional methods like Principal Component Analysis (PCA), which is limited to linear transformations, autoencoders can learn non-linear mappings, potentially capturing more complex relationships in the data.

The encoder portion of an autoencoder compresses the input x into a latent representation z:

z = f_encoder(x)

Where f_encoder typically consists of multiple neural network layers with progressively fewer neurons, culminating in the bottleneck layer that represents the latent space.

In radiation oncology, dimensionality reduction through autoencoders can be valuable for:

Compressing high-dimensional medical images or dose distributions into more manageable representations for subsequent analysis or modeling.

Extracting meaningful features from complex, multi-modal data sources like combined CT, MRI, and PET images.

Visualizing high-dimensional patient data in lower dimensions to identify patterns or clusters that might inform treatment strategies.

Reducing the dimensionality of input data for other machine learning models, potentially improving their performance when training data is limited.

The effectiveness of an autoencoder for dimensionality reduction depends on its architecture (depth, width, activation functions), the dimensionality of the latent space, and the training procedure. The goal is to find a balance where the latent representation is compact enough to be useful but still retains the information necessary for the task at hand.

### Denoising Autoencoders

Denoising autoencoders (DAEs) are a variant designed to learn robust representations by reconstructing clean inputs from corrupted versions. During training, noise is deliberately added to the input, and the network learns to recover the original, uncorrupted data:

x̃ = corrupt(x)  # Add noise to input
z = f_encoder(x̃)  # Encode corrupted input
x' = f_decoder(z)  # Reconstruct original input
Loss = ||x - x'||²  # Compare reconstruction to original

This process forces the network to learn features that are robust to variations and noise in the input, rather than simply learning to copy the input to the output.

In medical imaging applications, denoising autoencoders can:

Improve image quality by removing noise from low-dose CT scans, potentially enabling dose reduction without sacrificing diagnostic quality.

Learn features that are invariant to common artifacts or variations in imaging protocols, improving the robustness of subsequent analysis.

Serve as a preprocessing step for other deep learning models, providing cleaner inputs that may lead to better performance.

The concept of denoising can be extended beyond simple noise removal to handling other types of corruption or variation, such as missing data, intensity variations between scanners, or motion artifacts—all common challenges in medical imaging.

### Variational Autoencoders (VAEs)

Variational Autoencoders (VAEs) extend the autoencoder framework to learn not just a compressed representation but a probabilistic latent space. Instead of encoding an input as a single point in the latent space, VAEs encode it as a probability distribution, typically a Gaussian with learned mean and variance parameters.

The encoder in a VAE outputs parameters of this distribution:

μ, σ = f_encoder(x)

A sample is then drawn from this distribution using the reparameterization trick to allow gradient-based training:

z = μ + σ * ε, where ε ~ N(0, 1)

The decoder then reconstructs the input from this sampled latent vector:

x' = f_decoder(z)

VAEs are trained with a composite loss function that balances reconstruction quality against the regularization of the latent space:

Loss = Reconstruction_Loss + KL_Divergence

The Kullback-Leibler divergence term encourages the learned latent distributions to be close to a standard normal distribution, creating a continuous, structured latent space that facilitates generation and interpolation.

In radiation oncology, VAEs offer several unique capabilities:

Generating synthetic medical images or dose distributions by sampling from the latent space, potentially useful for data augmentation or simulation.

Interpolating between different patients or treatment plans in the latent space to explore the continuum of possible variations.

Anomaly detection by identifying inputs that have high reconstruction error or that map to low-probability regions of the latent space, potentially flagging unusual anatomical configurations or treatment plans for review.

Disentangled representation learning, where different dimensions of the latent space capture independent factors of variation in the data, such as separating anatomical variations from pathological changes.

The probabilistic nature of VAEs makes them particularly suitable for medical applications where quantifying uncertainty is important. By generating multiple reconstructions or predictions through repeated sampling from the latent distribution, VAEs can provide a measure of confidence or variability in their outputs.

---

## Generative Adversarial Networks (GANs)

Generative adversarial networks train a generator against a discriminator in a two-player objective, as introduced by Goodfellow and colleagues in 2014 [[9]](https://proceedings.neurips.cc/paper/2014/hash/f033ed80deb0234979a61f95710dbe25-Abstract.html). Visual realism is not evidence that synthetic medical data preserve pathology or are safe for downstream use.

### Generator and Discriminator

The generator network G takes random noise z as input and produces synthetic data G(z) that aims to mimic the distribution of real data. The generator never sees the real data directly; it learns solely from the feedback provided by the discriminator.

The discriminator network D acts as a binary classifier, taking either real data x or generated data G(z) as input and outputting a probability that the input comes from the real data distribution rather than the generator. The discriminator's goal is to correctly distinguish between real and generated samples.

These two networks are trained simultaneously in a minimax game:

min_G max_D V(D, G) = E_x~p_data [log D(x)] + E_z~p_z [log(1 - D(G(z)))]

Where:
- The discriminator D tries to maximize V by correctly classifying real and fake samples
- The generator G tries to minimize V by producing samples that fool the discriminator

In radiation oncology applications, the generator might produce synthetic medical images, contours, or dose distributions, while the discriminator learns to distinguish these from real clinical data. As training progresses, the generator produces increasingly realistic outputs that capture the complex patterns and relationships present in the training data.

### Training Dynamics

Training GANs is notoriously challenging due to several issues:

Mode collapse occurs when the generator produces limited varieties of outputs, failing to capture the full diversity of the real data distribution. In medical applications, this might manifest as generating only the most common anatomical configurations while failing to represent rarer but clinically important variations.

Training instability arises from the adversarial nature of the training process. If one network becomes too powerful relative to the other, learning can stall or diverge. For example, if the discriminator becomes too effective too quickly, the generator may receive insufficient gradient information to improve.

Vanishing gradients can occur when the discriminator becomes too confident, providing minimal useful feedback to the generator. Conversely, if the generator consistently fools the discriminator, the latter may receive insufficient signal to improve.

Several techniques have been developed to address these challenges:

Wasserstein GAN (WGAN) replaces the original GAN objective with the Wasserstein distance, which provides more stable gradients throughout training.

Spectral normalization constrains the discriminator's capacity by normalizing its weights, helping maintain balance between the networks.

Progressive growing starts with low-resolution images and gradually increases resolution during training, allowing the networks to learn large-scale structure before fine details.

In medical applications, where data quality and diversity are paramount, addressing these training challenges is crucial for developing GANs that can generate clinically useful synthetic data.

### Applications in Image Synthesis

GANs have numerous applications in radiation oncology and medical imaging:

Synthetic data generation can augment limited datasets, helping to train more robust models for tasks like organ segmentation or treatment planning. For example, a GAN might generate additional variations of rare anatomical configurations to ensure models can handle these cases.

Image-to-image translation enables transforming images from one domain to another, such as converting MRI to synthetic CT for treatment planning when actual CT is unavailable, or translating between different MRI sequences.

Super-resolution techniques can enhance the quality of low-resolution medical images, potentially improving diagnostic accuracy or enabling more precise contouring.

Cross-modality synthesis can generate missing imaging modalities based on available ones, such as creating synthetic PET images from CT scans, potentially reducing the need for multiple scans.

Anomaly detection leverages the GAN's learned representation of normal anatomy to identify abnormalities or pathologies as deviations from this norm.

Domain adaptation uses GANs to align feature distributions between source and target domains, helping models trained on data from one institution or scanner generalize to others.

The quality and utility of GAN-generated images in clinical applications depend on several factors:

Training data quality and diversity
Network architecture and capacity
Training stability and convergence
Evaluation metrics that capture clinically relevant aspects of image quality

While GANs show tremendous promise for medical image synthesis, their deployment in clinical settings requires careful validation to ensure the generated images preserve the clinically relevant features of the original data and don't introduce artifacts that could affect diagnosis or treatment planning.

**Ethical note:** When using GAN-generated synthetic data in clinical research, it is important to validate that the synthetic images do not introduce artifacts or biases that could affect patient care.

---

## Transformers and Attention Mechanisms

Transformers replace recurrence with attention-based sequence processing. The original encoder-decoder architecture and scaled dot-product multi-head attention were described by Vaswani and colleagues [[10]](https://proceedings.neurips.cc/paper/7181-attention-is-all-you-need). Whether this improves a medical task must be tested against strong task-specific baselines.

### Self-attention

Self-attention is the core mechanism that allows transformers to weigh the importance of different elements in the input when processing each element. For each position in the input sequence, self-attention computes a weighted sum of all positions, with weights determined by the similarity between elements.

The standard self-attention mechanism, known as "scaled dot-product attention," is computed as:

Attention(Q, K, V) = softmax(QK^T / √d_k)V

Where:
- Q (queries), K (keys), and V (values) are linear projections of the input
- d_k is the dimension of the keys, used for scaling to prevent extremely small gradients
- The softmax function normalizes the attention weights

In medical imaging applications, self-attention allows the model to focus on relevant regions of an image when processing each location. For example, when segmenting a tumor, the model can attend to similar-appearing regions elsewhere in the image or to anatomical landmarks that provide context, even if they're distant from the current location.

The global receptive field of self-attention—each position can attend to all other positions—contrasts with the limited receptive field of convolutional operations, which only consider local neighborhoods. This global context is particularly valuable in medical imaging, where distant anatomical relationships often provide important diagnostic or segmentation cues.

### Multi-head Attention

Multi-head attention extends self-attention by running multiple attention operations in parallel, each with different learned projections. This allows the model to jointly attend to information from different representation subspaces and at different positions:

MultiHead(Q, K, V) = Concat(head_1, ..., head_h)W^O
where head_i = Attention(QW_i^Q, KW_i^K, VW_i^V)

Where W_i^Q, W_i^K, W_i^V, and W^O are learnable parameter matrices.

In medical imaging, multi-head attention enables the model to simultaneously capture different types of relationships:

One head might focus on texture similarities
Another might attend to shape correspondences
A third might emphasize anatomical positioning

This multi-faceted attention helps the model integrate various aspects of the image when making predictions, potentially leading to more accurate and robust performance on complex tasks like organ segmentation or tumor classification.

### Transformer Architecture

The complete transformer architecture consists of several key components:

Input embeddings convert the raw input (whether text tokens or image patches) into a continuous vector representation. In vision transformers, images are typically divided into fixed-size patches, each embedded as a vector.

Positional encodings add information about the position of each element, since self-attention itself is permutation-invariant. These encodings can be fixed sinusoidal functions or learned parameters.

The encoder stack consists of multiple identical layers, each containing:
- A multi-head self-attention mechanism
- A position-wise feed-forward network
- Layer normalization and residual connections

The decoder stack (used in sequence generation tasks) has a similar structure but includes an additional cross-attention mechanism that attends to the encoder's output.

In medical imaging applications, transformers have been adapted in several ways:

Vision Transformer (ViT) divides images into patches and processes them as a sequence, demonstrating competitive performance with CNNs on image classification tasks.

UNETR (UNet Transformer) combines the U-Net architecture popular in medical segmentation with transformer encoders, leveraging both local and global context.

Swin Transformer uses shifted windows to efficiently compute self-attention locally while allowing for cross-window connections, addressing the computational challenges of applying self-attention to high-resolution images.

These transformer-based architectures have shown promising results in radiation oncology applications, including organ segmentation, tumor detection, and treatment response prediction. Their ability to capture long-range dependencies complements the local pattern recognition strengths of CNNs, leading to hybrid approaches that combine the best of both worlds.

---

## U-Net and Segmentation Architectures

Segmentation assigns a class label to each pixel or voxel. U-Net's encoder, decoder, and same-scale skip connections established a widely reused biomedical segmentation design [[11]](https://doi.org/10.1007/978-3-319-24574-4_28).

### Encoder-decoder Structures

Encoder-decoder architectures for segmentation typically follow a pattern of:

1. An encoder path that progressively reduces spatial dimensions while increasing feature channels, capturing increasingly abstract representations
2. A decoder path that recovers spatial resolution while decreasing feature channels, generating the segmentation map

This structure allows the network to:

Capture hierarchical features at multiple scales in the encoder
Generate detailed, pixel-level predictions in the decoder
Maintain a reasonable parameter count by working with reduced spatial dimensions in the intermediate layers

The U-Net architecture, introduced by Ronneberger et al. in 2015 specifically for biomedical image segmentation, follows this encoder-decoder pattern but adds a crucial innovation: skip connections.

### Skip Connections

Skip connections directly connect layers in the encoder path to corresponding layers in the decoder path, allowing the decoder to access features from earlier layers. These connections serve several important purposes:

Preserving spatial information: While the encoder captures increasingly abstract features, it loses spatial precision due to pooling operations. Skip connections provide the decoder with access to the higher-resolution features from the encoder, helping generate more precise segmentation boundaries.

Mitigating the vanishing gradient problem: By providing shorter paths for gradient flow during backpropagation, skip connections help train deeper networks more effectively.

Combining multi-scale information: Skip connections allow the network to fuse features at different scales, capturing both fine details and broader contextual information.

In the original U-Net, skip connections are implemented as concatenations, where feature maps from the encoder are concatenated with the corresponding decoder features along the channel dimension. This allows the decoder to selectively use information from both paths.

The effectiveness of skip connections has made them a standard component in segmentation architectures, with variations appearing in numerous U-Net derivatives and other segmentation networks.

### Specialized Architectures for Medical Imaging

Building on the U-Net foundation, numerous specialized architectures have been developed to address the unique challenges of medical image segmentation:

V-Net extends U-Net to 3D volumes, using 3D convolutions throughout the network to process volumetric medical data like CT or MRI scans. This allows the network to leverage information across slices, capturing 3D anatomical relationships that might be missed when processing 2D slices independently.

Attention U-Net incorporates attention gates that help the model focus on relevant regions, suppressing irrelevant responses in feature maps. This is particularly valuable in medical imaging, where the structures of interest may occupy only a small portion of the image.

nnU-Net ("no new U-Net") is a self-configuring framework rather than a single architecture. It adapts preprocessing, topology, training, and post-processing rules to a dataset and was evaluated across 23 public biomedical segmentation datasets [[12]](https://doi.org/10.1038/s41592-020-01008-z).

TransUNet combines transformers with U-Net, using a transformer encoder to capture global context and a convolutional decoder with skip connections to generate detailed segmentations. This hybrid approach leverages the strengths of both transformers (global relationships) and CNNs (local patterns).

In radiation oncology, these specialized architectures have been applied to various segmentation tasks:

Multi-organ segmentation for treatment planning, identifying organs at risk to avoid during radiation delivery
Tumor delineation, precisely defining the target volume for treatment
Adaptive radiotherapy, tracking changes in anatomy over the course of treatment
Automatic contouring for routine structures, reducing the clinical workload

The choice of architecture depends on factors like the specific segmentation task, available computational resources, dataset characteristics, and required inference speed for clinical workflow integration.

---

```{toctree}
:maxdepth: 2
:caption: Contents
llm
vlm
```

## Current Research and Recent Advances

- **Self-configuring segmentation pipelines:** nnU-Net showed that systematic configuration of preprocessing, architecture, training, and post-processing can matter as much as a novel network block. Its results are benchmark evidence, not proof of clinical benefit [[12]](https://doi.org/10.1038/s41592-020-01008-z). _(added: 2026-07)_
- **Attention-based architectures:** Transformers permit global token interactions and parallel sequence processing, but their value in a medical task must be established against strong convolutional baselines on representative data [[10]](https://proceedings.neurips.cc/paper/7181-attention-is-all-you-need). _(added: 2026-07)_
- **Multimodal learning:** Models that connect images and language broaden the possible task set. Generalist biomedical results remain transfer evidence rather than radiotherapy validation; the dedicated [vision-language model chapter](vlm.md) covers the evidence and limitations [[13]](https://doi.org/10.1038/s41591-024-03185-2). _(added: 2026-07)_

## Recap

- **Objective 1:** A prediction combines input features with learned weights and a bias, then applies activations; a loss measures the discrepancy relevant to training.
- **Objective 2:** Forward propagation produces outputs, backpropagation computes how parameters affect loss, and an optimizer updates parameters from those gradients.
- **Objective 3:** Convolutional networks encode local spatial patterns, recurrent models encode order, autoencoders learn compressed representations, generative adversarial networks learn through competing networks, transformers use attention, and U-Net joins multiscale context with spatial detail.
- **Objective 4:** Output type and data structure guide the architecture and objective: class probabilities, continuous values, generated samples, and spatial masks require different constraints and losses.
- **Objective 5:** Architecture is one part of a frozen pipeline; representative data, leakage control, comparison, calibration, external validation, workflow evaluation, and monitoring determine whether it generalizes safely.

**Important limitation and misconception:** A more complex or newer architecture is not inherently better, deep learning is not essential for every high-dimensional task, and benchmark superiority is not evidence of patient benefit.

## References

1. Rosenblatt F. The perceptron: a probabilistic model for information storage and organization in the brain. *Psychological Review*. 1958. [DOI](https://doi.org/10.1037/h0042519)
2. Goodfellow I, Bengio Y, Courville A. *Deep Learning*. MIT Press; 2016. [Open textbook](https://www.deeplearningbook.org/)
3. Rumelhart DE, Hinton GE, Williams RJ. Learning representations by back-propagating errors. *Nature*. 1986. [DOI](https://doi.org/10.1038/323533a0)
4. Glorot X, Bengio Y. Understanding the difficulty of training deep feedforward neural networks. *AISTATS*. 2010. [PMLR](https://proceedings.mlr.press/v9/glorot10a.html)
5. He K, Zhang X, Ren S, Sun J. Delving deep into rectifiers. *ICCV*. 2015. [DOI](https://doi.org/10.1109/ICCV.2015.123)
6. Ioffe S, Szegedy C. Batch normalization: accelerating deep network training by reducing internal covariate shift. *ICML*. 2015. [PMLR](https://proceedings.mlr.press/v37/ioffe15.html)
7. LeCun Y, Bengio Y, Hinton G. Deep learning. *Nature*. 2015. [DOI](https://doi.org/10.1038/nature14539)
8. Hochreiter S, Schmidhuber J. Long short-term memory. *Neural Computation*. 1997. [DOI](https://doi.org/10.1162/neco.1997.9.8.1735)
9. Goodfellow IJ, Pouget-Abadie J, Mirza M, et al. Generative adversarial nets. *NeurIPS*. 2014. [Proceedings](https://proceedings.neurips.cc/paper/2014/hash/f033ed80deb0234979a61f95710dbe25-Abstract.html)
10. Vaswani A, Shazeer N, Parmar N, et al. Attention is all you need. *NeurIPS*. 2017. [Proceedings](https://proceedings.neurips.cc/paper/7181-attention-is-all-you-need)
11. Ronneberger O, Fischer P, Brox T. U-Net: convolutional networks for biomedical image segmentation. *MICCAI*. 2015. [DOI](https://doi.org/10.1007/978-3-319-24574-4_28)
12. Isensee F, Jaeger PF, Kohl SAA, Petersen J, Maier-Hein KH. nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. *Nature Methods*. 2021. [DOI](https://doi.org/10.1038/s41592-020-01008-z)
13. Tu T, Azizi S, Driess D, et al. Towards generalist biomedical AI. *Nature Medicine*. 2024. [DOI](https://doi.org/10.1038/s41591-024-03185-2)
