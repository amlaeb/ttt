import torch
import torch.nn as nn


class net(nn.Module):
    def __init__(self, n_features):
        super(net, self).__init__()
        self.connection_1 = nn.Linear(n_features, 10)
        self.connection_2 = nn.Linear(10, 5)
        self.connection_3 = nn.Linear(5, 1)

    def forward(self,input_tensor):
        output_tensor = torch.nn.Sigmoid(self.connection_1(input_tensor))
        output_tensor = torch.nn.Sigmoid(self.connection_2(output_tensor))
        output_tensor = self.connection_3(output_tensor)
        return output_tensor
