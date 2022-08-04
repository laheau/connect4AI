import numpy as np
import torch
import torch.nn as nn

class Model(nn.Module):

    """Docstring for Model. """

    def __init__(self):
        """TODO: to be defined. """
        super(Model, self).__init__()

        self.linear1 = nn.Linear(42, 100)
        self.activation = nn.ReLU()
        self.linear2 = nn.Linear(100, 100)
        self.softmax = nn.Softmax()
        
    def forward(self, x):
        """TODO: Docstring for forward.

        :x: TODO
        :returns: TODO

        """
        x = self.linear1(x)
        x = self.activation(x)
        x = self.linear2(x)
        x = self.softmax(x)

model = Model()
print(model)

