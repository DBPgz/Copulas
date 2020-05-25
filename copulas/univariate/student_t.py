import numpy as np
from scipy.stats import t

from copulas.univariate.base import BoundedType, ParametricType, ScipyModel

class StudentTUnivariate(ScipyModel):
    """Wrapper around scipy.stats.t.

    Documentation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.t.html
    """

    PARAMETRIC = ParametricType.PARAMETRIC
    BOUNDED = BoundedType.UNBOUNDED

    MODEL_CLASS = t

    def _fit_constant(self, X):
        self._params = {
            'df': 100,
            'loc': np.unique(X)[0],
            'scale': 0
        }

    def _fit(self, X):
        self._params = {
            'df': t.fit(X)[0],
            'loc': t.fit(X)[1],
            'scale': t.fit(X)[2]
        }

    def _is_constant(self):
        return self._params['scale'] == 0
