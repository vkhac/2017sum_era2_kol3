import unittest
from matrix import Matrix

class MyTestMatrixHector(unittest.TestCase):

    def setUp(self):
        self.l1 = [[1, 2], [3, 4]]
        self.l2 = [(0, 0), (0, 1), (1, 0), (1, 1)]
        
        self.l3 = [[5, 6], [7, 8]]
        
    def test_init(self):
        m1 = Matrix(self.l1)
        
        self.assertEqual(self.l1[0], m1.rows[0])
        self.assertEqual(self.l1[1], m1.rows[1])
        
        self.assertEqual(2, m1.nrows)
        self.assertEqual(2, m1.ncols)
        
        self.assertEqual(self.l2, m1.coordinates_vector)
        
    def test_add(self):
        m1 = Matrix(self.l1)
        m3 = Matrix(self.l3)
        
        m4 = m1 + m3
        m5 = m1 + 2
        m6 = 3 + m1
        
        self.assertEqual(m4.rows[0][0], 6)
        self.assertEqual(m4.rows[0][1], 8)
        self.assertEqual(m4.rows[1][0], 10)
        self.assertEqual(m4.rows[1][1], 12)
        
        self.assertEqual(m5.rows[0][0], 3)
        self.assertEqual(m5.rows[0][1], 4)
        self.assertEqual(m5.rows[1][0], 5)
        self.assertEqual(m5.rows[1][1], 6)
        
        self.assertEqual(m6.rows[0][0], 4)
        self.assertEqual(m6.rows[0][1], 5)
        self.assertEqual(m6.rows[1][0], 6)
        self.assertEqual(m6.rows[1][1], 7)
        
    def test_sub(self):
        m1 = Matrix(self.l1)
        m3 = Matrix(self.l3)
        
        m4 = m3 - m1
        m5 = m1 - 2
        m6 = 3 - m1
        
        self.assertEqual(m4.rows[0][0], 4)
        self.assertEqual(m4.rows[0][1], 4)
        self.assertEqual(m4.rows[1][0], 4)
        self.assertEqual(m4.rows[1][1], 4)
        
        self.assertEqual(m5.rows[0][0], -1)
        self.assertEqual(m5.rows[0][1], 0)
        self.assertEqual(m5.rows[1][0], 1)
        self.assertEqual(m5.rows[1][1], 2)
        
        self.assertEqual(m6.rows[0][0], 2)
        self.assertEqual(m6.rows[0][1], 1)
        self.assertEqual(m6.rows[1][0], 0)
        self.assertEqual(m6.rows[1][1], -1)
        
    def test_prod(self):
        m1 = Matrix(self.l1)
        m3 = Matrix(self.l3)
        
        m4 = m1.prod(m3)
        
        self.assertEqual(m4.rows[0][0], 19)
        self.assertEqual(m4.rows[0][1], 22)
        self.assertEqual(m4.rows[1][0], 43)
        self.assertEqual(m4.rows[1][1], 50)
        
    
    
    
    
    
    
    
    
    
        
        
