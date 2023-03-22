from face_landmarks_detection import generate_face_correspondences
from delauny_trianglation import make_delaunay
from face_morph import generate_morph_sequence
import cv2


##############Inputs##############
img_path_one = "img/1.jpg"
img_path_two = "img/2.jpg"
alpha = 0.7
#################################


def doMorphing(img1, img2,alpha):
	[size, img1, img2, points1, points2, list3] = generate_face_correspondences(img1, img2)
	tri = make_delaunay(size[1], size[0], list3, img1, img2)
	generate_morph_sequence(img1, img2, points1, points2, tri,alpha)


image1 = cv2.imread(img_path_one)
image1 = cv2.resize(image1,(600,800))
image2 = cv2.imread(img_path_two)
image2 = cv2.resize(image2,(600,800))

doMorphing(image1, image2,alpha)
