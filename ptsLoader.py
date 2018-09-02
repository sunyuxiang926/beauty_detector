#code from https://github.com/HCIILAB/SCUT-FBP5500-Database-Release/issues/1

#data from following source
@article{liang2017SCUT,
title     = {SCUT-FBP5500: A Diverse Benchmark Dataset for Multi-Paradigm Facial Beauty Prediction},
author    = {Liang, Lingyu and Lin, Luojun and Jin, Lianwen and Xie, Duorui and Li, Mengru},
jurnal    = {arXiv:1801.06345}, 
year      = {2018}
}


import os
import re
import struct
import shutil

def get_files(dname, suffix):
    pts_list = []
    for fname in os.listdir(dname):
        if fname.endswith(suffix):
            pts_list += [fname]
    return pts_list

def pts2txt(din, dout, src):
    src_p = os.path.join(din, src)
    data = open(src_p, 'rb').read()
    points = struct.unpack('i172f', data)
    # print points
    
    dst = src.lower()
    dst = dst.replace('pts', 'txt')
    dst_p = os.path.join(dout, dst)
    # print dst_p
    
    fout = open(dst_p, 'w')
    pnum = len(points[1:])
    for i in range(1, pnum, 2):
        fout.write('%f ' % points[i])
        fout.write('%f\n' % points[i + 1])
    
    fout.close()

def main(files):
    src = 'SCUT-FBP5500_with_Landmarks/facial landmark/'+files
    dst = 'readable data'
    
    if not os.path.exists(dst):
        os.mkdir(dst)
    
    pts_list = get_files(src, 'pts')
    for pts in pts_list:
        pts2txt(src, dst, pts)
    
    jpg_list = get_files(src, 'jpg')
    for img in jpg_list:
        src_img = os.path.join(src, img)
        img_lower = img.lower()
        dst_img = os.path.join(dst, img_lower)
    
        shutil.copy(src_img, dst_img)

if __name__ == '__main__':
    for files in os.listdir('SCUT-FBP5500_with_Landmarks/facial landmark'):
        if files!='.DS_Store':
            main(files)