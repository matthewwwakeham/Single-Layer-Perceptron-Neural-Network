def perceptron(input_features, weights, threshold):

      z = sum(x * w for x, w in zip(input_features, weights))

      output = 1 if z >= threshold else 0

      return output

input_features = [0.5, 0.7]
weights = [0.2, 0.8]
threshold = 0.5

output = perceptron(input_features, weights, threshold)

print("Perceptron Output:", output)