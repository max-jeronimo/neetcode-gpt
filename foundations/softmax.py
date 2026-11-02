import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # define e^z, as the e^(z - max(z))
        exp_z = np.exp(z - np.max(z))
        # softmax is just the defined e^z formula we just created, divided by the sum
        # (big E), all e^z
        sm = exp_z / np.sum(exp_z)
        # return np.round(your_answer, 4)
        return np.round(sm, 4)    
