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
        self.output = nn.Linear(100, 7)

    def forward(self, x):
        """TODO: Docstring for forward.

        :x: TODO
        :returns: TODO

        """
        x = self.linear1(x)
        x = self.activation(x)
        x = self.linear2(x)
        x = self.activation(x)
        x = self.linear2(x)
        x = self.activation(x)
        x = self.output(x)
        x = self.softmax(x)

        return x

class Critic(nn.Module):

    """Docstring for Critic. """

    def __init__(self):
        """TODO: to be defined. """
        super(Critic, self).__init__()

        self.linear1 = nn.Linear(49, 100)
        self.activation = nn.ReLU()
        self.linear2 = nn.Linear(100, 100)
        self.linear3 = nn.Linear(100, 1)
        self.tanh = nn.Tanh()

    def forward(self, x):
        
        x = self.linear1(x)
        x = self.activation(x)
        x = self.linear2(x)
        x = self.activation(x)
        x = self.linear2(x)
        x = self.activation(x)
        x = self.linear3(x)
        x = self.tanh(x)

        return x
