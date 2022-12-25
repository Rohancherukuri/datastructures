# Creating a NeRF algorithm in python
import jax.numpy as np
from typing import Callable


# Define the Neural Network architecture
class NeRF(object):
    """This is a NeRF class"""
    def __init__(self, input_size: int, hidden_size: int, output_size: int) -> None:
        """This is a NeRF class constructor"""
        self.w1 = np.random.randn(input_size, hidden_size)
        self.b1 = np.zeros(hidden_size)
        self.w2 = np.random.randn(hidden_size, output_size)
        self.b2 = np.zeros(output_size)
    
    def forward(self, x: np.ndarray) -> np.ndarray:
        """This method calculates the derivatives in forward pass"""
        # Perform the first linear transformation
        z1 = np.dot(x, self.w1) + self.b1
        # Apply the activation function
        a1 = np.maximum(0, z1)
        # Perform the second linear transformation
        z2 = np.dot(a1, self.w2) + self.b2
        # Apply the output function
        y = z2
        return y
    
    def transform(self) -> Callable:
        """This method return's the forward method of Nerf class"""
        return self.forward
    
    def __repr__(self) -> str:
        """This is special method for object representation"""
        return f"NeRF()"
        
def main() -> None:
    """This is a main function"""
    try:
        # Define the input size, hidden size, and output size
        params = {
                   "input_size": 128,
                    "hidden_size": 256,
                    "output_size": 128
                }

        nn = NeRF(**params)
        result = nn.transform()
        print("The Neural Radiance Fields Model is:", nn)
        # Generate an image using the NeRF network
        inputs = np.random.randn(1, params.get("input_size", np.nan))
        outputs = result(inputs)
        print("The output is: " + str(outputs))
    except (KeyboardInterrupt, Exception) as e:
        print("An error occured inside the main function " + str(e))

if __name__ == "__main__":
    main()



        