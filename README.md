# lowlevelneuralnetwork
Neural networks are made up of layers of nodes which are interconnected. These nodes are also called neurons or artificial neurons. The building block of a neural network is a perceptron. It is a basic model of a biological neuron. Below is an example of a single layer perceptron neural nework.

## 1. Input Layer
   Assume two input features: x1 and x2. These could be two features of an image.

## 2. Weighted Sum
   Each input is multiplied by a corresponding weight: w1 and w2. The weighted sum of inputs is calculated       below:

   z = weighted sum

   z = x1 * w2 + x2 * w2

## 3. Activation Function

   The weighted sum z is then passed through an activation function. A common activation function is a step       function.

   output = { 1 if z >= threshold; 0 otherwise }

## 4. Example

   Input features: 0.5, 0.7
   Weights: 0.2, 0.8
   Threshold: 0.5

   z = 0.5 x 0.2 + 0.7 x 0.8
   z = 0.1 + 0.56
   z = 0.66

   output = { 1 if z >= threshold = 0.5; 0 otherwise }

   z = 0.66 > threshold = 0.5 -> output = 1

## 5. Python Code

      def perceptron(input_features, weights, threshold):

            z = sum(x * w for x, w in zip(input_features, weights))

            output = 1 if z >= threshold else 0

            return output

      input_features = [0.5, 0.7]
      weights = [0.2, 0.8]
      threshold = 0.5

      output = perceptron(input_features, weights, threshold)

      print("Perceptron Output:", output)

## 6. Output

      Perceptron Output: 1
   
