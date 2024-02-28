'''
This code is to convert a series of 2d PNG files into a 3D Nifti volume.
-> This is implementation for CT Train Sets in CHAOS dataset. Here, each Train Set folder has 'DICOM_anon' and 'Ground' subfolders.

-> The code assumes that all PNG files in the directory belong to the same series and are slices of the same volume; and are ordered.
-> The affine transformation matrix used here (np.eye(4)) is an identity matrix. In real scenarios, you might need to use the correct affine matrix from the corresponding DICOM headers to preserve spatial orientation and scale.
-> The pixel spacing, slice thickness, and orientation should be consistent across all slices for accurate volume reconstruction.
'''

import os
import pydicom
import numpy as np
import nibabel as nib
from PIL import Image

def save_nifti(volume, filename):
    volume = volume.astype(np.float32)
    # Convert the numpy array to a NIfTI image
    nifti_img = nib.Nifti1Image(volume, affine=np.eye(4))
    # Save the NIfTI image
    nib.save(nifti_img, filename)

def get_png_vol(png_folder):
    image_arrays = []
    for png_file in sorted(os.listdir(png_folder)):
        print(png_file)
        if png_file.lower().endswith('.png'):
            image_arrays.append(np.array(Image.open(os.path.join(png_folder, png_file))))

    # Stack the image arrays to create a 3D array
    stacked_images = np.stack(image_arrays, axis=0)
    return stacked_images

# Directory containing DICOM files
directory = '/CHAOS_Train_Sets/CT'
save_folder = '/CHAOS'

i=1 # Only for Naming purposes
# Iterate through all items in the base directory
for vol in os.listdir(directory):
    vol_path = os.path.join(directory, vol)

    # Check if the item is a directory
    if os.path.isdir(vol_path):
        png_folder = os.path.join(vol_path, 'Ground')
        print(f"Working with: {png_folder}")
        seg_volume = get_png_vol(png_folder)
        save_nifti(seg_volume, os.path.join(save_folder, 'labelsTr', f'chaos_{i:02}.nii.gz'))
        i=i+1
