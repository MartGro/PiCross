__author__ = 'martin'
import unittest
import Experiments
import PicrossAlgorithms
import bitarray

class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        pass

    def test_IOT_2_3(self):
        equal=[[0, 0, 0], [0, 0, 1], [0, 1, 1], [1, 1, 1]]
        self.assertEqual(PicrossAlgorithms.ImprovedOffsetMap(2,3),equal)

    def test_bitarray_2_1_2(self):
        lenstor=[2, 1, 2]
        posstor=[0, 3, 5]
        lg=8
        bita=bitarray.bitarray('11010110')
        self.assertEqual(PicrossAlgorithms.CreateBitarray(lenstor,posstor,lg),bita)

    def test_PA_2_1_2(self):
        self.assertEqual(PicrossAlgorithms.PossibleArrangements((2,1,2),8).__len__(),4)





if __name__ =="__main__":
    unittest.main()