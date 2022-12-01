from utils import load_coefficients
import cv2
import glob

# Load coefficients
mtx, dist = load_coefficients('calibration_chessboard.yml')

input_dir = 'area1/'
file_extension = '.png'
output_dir = 'rectified/'

dir_path = input_dir+'*'+file_extension

for fname in glob.glob(dir_path):
	original = cv2.imread(fname)
	dst = cv2.undistort(original, mtx, dist, None, None)
	cv2.imwrite(fname.replace(input_dir[:-1],'rectified'), dst)