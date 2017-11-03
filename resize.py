#!/usr/local/bin/python3
#!-*- coding: utf-8 -*-

import argparse
import os
import cv2
import numpy as np

def resizeImages(input_dir, output_dir):

    files = os.listdir(input_dir)

    for file in files:

        name, ext = os.path.splitext(file)

        if ext != '.jpg':
            print('[' + file + ']: not supported format.')

        img = cv2.imread(
            os.path.join(input_dir, file),
            cv2.IMREAD_COLOR
        )

        tmp = img[:, :]
        height, width = img.shape[:2]

        if (height > width):
            size = height
            limit = width
        else:
            size = width
            limit = height

        start = int((size - limit) / 2)
        fin = int((size + limit) / 2)

        resized_img = cv2.resize(np.zeros((1, 1, 3), np.uint8), (size, size))

        if (size == height):
            resized_img[:, start:fin] = tmp
        else:
            resized_img[start:fin, :] = tmp

        cv2.imwrite(
            os.path.join(output_dir, file),
            resized_img
        )

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', default='original')
    parser.add_argument('--output_dir', default='resized')
    args = parser.parse_args()

    resizeImages(args.input_dir, args.output_dir)

if __name__ == '__main__':

    main()
