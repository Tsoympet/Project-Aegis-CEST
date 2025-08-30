
import unittest
from config import load_choices
from ble_models import kfi_from_projectile
from cest_calculator import cdp, prf

class TestShieldingFunctions(unittest.TestCase):

    def test_cdp(self):
        result = cdp(p_GeVc=1.7, q=1.0, B=10.0, L=1.0)
        self.assertAlmostEqual(result, 0.0, delta=0.1)

    def test_prf(self):
        result = prf(rpm=0.6, rsbs=0.7, chi=0.2)
        self.assertAlmostEqual(result, 0.8, delta=0.1)

    def test_kfi_from_projectile(self):
        result = kfi_from_projectile(D=10.0, V=2.0, tb=0.5, S=1.0, model='stuffed')
        self.assertGreater(result, 0.5)

if __name__ == '__main__':
    unittest.main()
