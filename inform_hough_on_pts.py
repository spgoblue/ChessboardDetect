# Given a set of ML pruned saddle points, remove outliers or keep only chessboard area
import numpy as np
import matplotlib.pyplot as plt


pts = np.array([[237, 332],
 [242, 287],
 [245, 263],
 [247, 360],
 [249, 337],
 [252, 314],
 [255, 290],
 [257, 389],
 [258, 266],
 [260, 366],
 [262, 342],
 [268, 294],
 [271, 269],
 [274, 372],
 [280, 323],
 [286, 272],
 [286, 404],
 [291, 353],
 [295, 328],
 [298, 302],
 [298, 437],
 [301, 411],
 [304, 386],
 [311, 333],
 [318, 279],
 [318, 420],
 [321, 393],
 [324, 366],
 [329, 339],
 [332, 311],
 [336, 283]])

outliers = np.array([
  [50,23],
  [30,63],
  [400,203],
  [250,370],
  [500,303],
  ])

pts = np.vstack([pts, outliers])


# plt.plot(outliers[:,0],outliers[:,1],'rx')
# plt.plot(pts[:,0],pts[:,1],'.')
# plt.show()
N = len(pts)

new_order = np.arange(N)
np.random.shuffle(new_order)
pts = pts[new_order,:]

print pts



import time

ta = time.time()

outlier = calculateOutliers(pts)
pred_outliers = pts[outlier,:]

tb =  time.time()

proc_time = tb-ta
print("Processed in %.2f ms" % (proc_time*1e3))


# plt.plot(outliers[:,0],outliers[:,1],'rx')
plt.plot(pred_outliers[:,0],pred_outliers[:,1],'rx')
plt.plot(pts[:,0],pts[:,1],'.')
plt.show()