import cv2
import glob
import numpy as np

class inputdata(object):
    
    def __init__(self, dataset):
        self.dataset = dataset

    def load_data2(self, size=(28, 28), num=-1):
        """データセットをロードしてGPUの共有変数に格納"""

        def flatten(mat):
            """
            type: list[list[float]] => list[float]
            Convert matrix to vector.
            """
            res = []
            for row in mat:
                for elem in row:
                    res.append(elem)
            return res

        def load_train(path, kind, size=(28, 28), num=-1):
            """ string => (List[[Array[float]], int)"""
            res = []
            teach = []
            currentteach = 0
            n = 0
            for k in range(kind):
                if n == num:
                	break
                res_kind = []
                kindDir = path + "kind_{k}/*".format(k=str(k))
                for g in glob.glob(kindDir):
                    if g[-4:]==".png" or g[-4:]==".jpg":
                        res_kind.append(flatten(cv2.resize(cv2.imread(g, 0), (size[0], size[1]))))
                        n += 1
                        teach.append(k)
                    if len(teach) != n:
                    	print("Err:: teach:{0}, n:{1}".format(len(teach), n))
                currentteach += 1
                normed = np.array(res_kind)/255.0
                res.append(normed.tolist())
                #print("n: {0}, currentteach: {1}".format(n, currentteach))
            return (res, teach)

        def load_test(path, size=(28, 28), num=-1):
            res = []
            for g in glob.glob(path + "*"):
                if g[-4:]==".png" or g[-4:]==".jpg":
                    res.append(flatten(cv2.resize(cv2.imread(g, 0), (size[0], size[1]))))
            return (np.array(res)/255.0, None)

        train_set = load_train("input/{dataset}/train/".format(dataset=self.dataset), 10, size, num)
        valid_set = load_train("input/{dataset}/valid/".format(dataset=self.dataset), 10, size, num)
        test_set = load_test("input/{dataset}/test/".format(dataset=self.dataset), size, num)

        test_set_x, test_set_y = test_set
        valid_set_x, valid_set_y = valid_set
        train_set_x, train_set_y = train_set

        rval = [(train_set_x, train_set_y),
                (valid_set_x, valid_set_y),
                (test_set_x, test_set_y)]

        return rval