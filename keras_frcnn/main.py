from detector import FasterRCNNDetector
import cv2


def main():

    detector = FasterRCNNDetector(model_path='./model/kitti_fcnn_last.hdf5')

    #img = cv2.imread('images/000000.png')
    img = cv2.imread('test_images/2af8cc56-033f-4428-bc65-24a886ac2ef4.jpeg')
    detector.detect_on_image(img)


if __name__ == '__main__':
    main()