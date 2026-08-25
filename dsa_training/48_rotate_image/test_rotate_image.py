from rotate_image import Solution

def test_rotate_image():
    sol = Solution()
    
    # Test case 1
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    sol.rotate(matrix1)
    assert matrix1 == [[7,4,1],[8,5,2],[9,6,3]]
    
    # Test case 2
    matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    sol.rotate(matrix2)
    assert matrix2 == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

