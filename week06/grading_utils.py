import numpy as np


def test_vocab(vocab):
    return [
        len(vocab),
        len(np.unique(vocab)),
    ]


def test_network(network):
    return int(all(param.grad is not None for param in network.parameters()))


def test_batch(batch):
    return int(batch[0].shape[0])
