from _typeshed import OptExcInfo
import pandas as pd
import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as pt

from typing import Tuple


def least_squares_slr(X:npt.NDArray[np.number], y: npt.NDArray[np.number]) -> Tuple[np.number, np.number]:
    slope: np.number = np.sum((X - X.mean())*(y - y.mean()))/np.sum((X - X.mean())**2)
    intercept: np.number = y.mean() - slope*X.mean()

    return slope, intercept
