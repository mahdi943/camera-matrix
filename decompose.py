import cv2
import numpy as np
import json

# Open the JSON file
with open('camera.json') as json_file:
  # Load the array from the file
  arr = json.load(json_file)


# Camera matrix
mtx = np.array(arr["CamMtx"])
print("Camera matrix:\n",mtx)

# Column vector of zeros
zeros = np.zeros((mtx.shape[0], 1))

# Stack the matrices horizontally to insert the column of zeros
A = np.hstack((mtx, zeros))


# Decompose the projection matrix
K, R, t, _, _, _, _ = cv2.decomposeProjectionMatrix(A)

# Print the intrinsic and extrinsic matrices
print("\nIntrinsic matrix:\n",K)
print("\nExtrinsic matrix:\n",R)
print("\nt=\n",t)
