# coding: utf-8
import cv2
# import numpy as np
from transform import resize


class CvFilterStack(object):
    """Represents a bunch of filters"""
    def __init__(self, image, identifier=None):
        super(CvFilterStack, self).__init__()
        self.image = image
        self.filters = []
        self.identifier = identifier or ''

    def window_id(self, filterr):
        return '{}:{}'.format(self.identifier, type(filterr).__name__)

    def imshow(self):
        result = self.image
        for filterr in self.filters:
            result = filterr.apply(result)
            cv2.imshow(self.window_id(filterr), result)

    def create_trackbars(self):
        for filterr in self.filters:
            window_name = self.window_id(filterr)
            cv2.namedWindow(window_name)
            for handle_name, handle in filterr.get_handles().items():
                maxx, *_ = handle
                cv2.createTrackbar(handle_name, window_name,
                                   0, maxx, self.update)

    def update(self, value):
        for filterr in self.filters:
            window_name = self.window_id(filterr)
            for handle_name, handle in filterr.get_handles().items():
                value = cv2.getTrackbarPos(handle_name, window_name)
                if value != handle[2]:
                    print('updating', handle_name, value)
                    handle[1](value)
        self.imshow()


class GreyFilter(object):
    """docstring for Filter"""
    def apply(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def get_handles(self):
        return {}


class GaussianFilter(object):
    """docstring for Filter"""
    def __init__(self):
        super(GaussianFilter, self).__init__()
        self.kernel_size = 3
        self.sigma = 1.4

    def apply(self, image):
        return cv2.GaussianBlur(image,
                                tuple([self.kernel_size * 2 + 1] * 2),
                                (self.sigma + 1) * .1)

    def get_handles(self):
        def set_kernel_size(value):
            self.kernel_size = value

        def set_sigma(value):
            self.sigma = value

        return {'kernel_size': (10, set_kernel_size, self.kernel_size),
                'sigma': (15, set_sigma, self.sigma)}


class CannyFilter(object):
    """docstring for Filter"""
    def __init__(self):
        super(CannyFilter, self).__init__()
        self.threshold = 200
        self.ratio = 3

    def apply(self, image):
        return cv2.Canny(image, self.threshold + 1,
                         (self.ratio + 1) * self.threshold)

    def get_handles(self):
        def set_threshold(value):
            self.threshold = value

        def set_ratio(value):
            self.ratio = value

        return {'threshold': (300, set_threshold, self.threshold),
                'ratio': (5, set_ratio, self.ratio)}


class ResizeFilter(object):
    """docstring for Filter"""
    def __init__(self):
        super(ResizeFilter, self).__init__()
        self.ratio = .1

    def apply(self, image):
        return resize(image, ratio=(self.ratio + 1) * .1)

    def get_handles(self):
        def set_ratio(value):
            self.ratio = value

        return {'ratio': (10, set_ratio, self.ratio)}


def main():
    # get image
    img = cv2.imread('tests/images/sheet.jpg')
    img = resize(img, width=500)
    cv2.namedWindow('test')
    fs = CvFilterStack(img, 'test')
    fs.filters = [GreyFilter(), GaussianFilter(), CannyFilter()]
    # fs.filters = [ResizeFilter(), GreyFilter(), GaussianFilter(), CannyFilter()]
    fs.create_trackbars()
    fs.imshow()
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
