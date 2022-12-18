# camera-matrix

## Task
1- Set your phone to a fixed direction and focal length and calculate its camera matrix, using photographs of an arbitrary object of your choice
2- Decompose the camera matrix into intrinsic and extrinsic matrices

## Solution
First, we need to define the world coordinates of 3D points using checkerboard patterns of known size. Then capture the images of the checkerboard from different viewpoints since the orientations of the camera were the same and the distance between the object and the camera was 1 meter. We use findChessboardCorners method in OpenCV to find the pixel coordinates(u,v) for each 3D point in different images. Finally, find camera parameters using calibraeCamera method in OpenCV, the 3D points, and pixel coordinates.

The camera matrix, also known as the intrinsic matrix, is a 3x3 matrix that describes the intrinsic properties of a camera. It maps 3D points in the world to 2D points on the image plane. The intrinsic matrix is typically denoted as K.


$$ K = {\left\lbrack \matrix{f & 0 & px \cr 0 & f & py \cr 0 & 0 & 1} \right\rbrack} $$

where f is the focal length, px and py are the coordinates of the principal point, and 1 is the scaling factor. Once we have calculated the intrinsic matrix, we can then calculate the extrinsic matrix, R and t, which describe the orientation and position of the camera in the world coordinate system. The extrinsic matrix is calculated as follows:

The intrinsic matrix has three main components, the focal length, the principal point, and the skew. The focal length determines the field of view and the magnification of the image. The principal point is the center of the image, and the skew describes any distortion in the x and y axes. To decompose the camera matrix into intrinsic and extrinsic matrices, we first need to add one column on the right to change its shape to 34 then calculate the intrinsic matrix, K.

Also can be written as:
P = K[I|o]]
We can use the cv2.decomposeProjectionMatrix() function from the OpenCV library in Python. This function takes as input the 34 projection matrix and returns the intrinsic and extrinsic matrices of the camera.
