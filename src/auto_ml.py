
import numpy as np
from sklearn.linear_model import SGDClassifier
class AutoML:
    def __init__(self):
        self.model = SGDClassifier(loss='log', max_iter=1000)
        self._initialized = False

    def partial_fit_safe(self, X, y):
        try:
            if not self._initialized:
                self.model.partial_fit(X, y, classes=np.array([-1,0,1]))
                self._initialized = True
            else:
                self.model.partial_fit(X, y)
        except Exception as e:
            print(f"AutoML partial_fit falhou: {e}")
