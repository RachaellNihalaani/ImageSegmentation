'''
This code is to convert a series of 2d DICOM slices into a 3D Nifti volume.
-> This is implementation for CHAOS Train Sets & CT Pancreas dataset. If there are a lot of unnecessary subfolders (like in CT Pancreas), modify accordingly.

-> Ensure that the DICOM files are from the same series and are correctly oriented.
-> The code assumes that all DICOM files in the directory belong to the same series and are slices of the same volume.
-> The affine transformation matrix used here (np.eye(4)) is an identity matrix. In real scenarios, you might need to use the correct affine matrix from the DICOM headers to preserve spatial orientation and scale.
-> The pixel spacing, slice thickness, and orientation should be consistent across all slices for accurate volume reconstruction.
'''

import os
import pydicom
import numpy as np
import nibabel as nib
from PIL import Image
def load_dicom_series(directory):
    # Read all DICOM files in the directory
    dicom_files = [pydicom.dcmread(os.path.join(directory, f)) for f in os.listdir(directory) if f.endswith('.dcm')]
    # Sort the DICOM files by their Image Position (Slice Location) - OPTIONAL STEP
    # print(dicom_files) # Use this to look at the DICOM Header to extract relevant information if needed
    # dicom_files.sort(key=lambda x: float(x.ImagePositionPatient[2]))
    # Combine the pixel data into a single 3D array
    volume = np.stack([file.pixel_array for file in dicom_files], axis=0)
    return volume
    
def find_deepest_subfolder(directory):
    deepest_subfolder = None
    max_depth = -1
    for root, dirs, files in os.walk(directory):
        current_depth = root.count(os.sep)
        if current_depth > max_depth and dirs:
            max_depth = current_depth
            deepest_subfolder = os.path.join(root, dirs[-1])
    return deepest_subfolder
    
def save_nifti(volume, filename):
    volume = volume.astype(np.float32)
    # Convert the numpy array to a NIfTI image
    nifti_img = nib.Nifti1Image(volume, affine=np.eye(4))
    # Save the NIfTI image
    nib.save(nifti_img, filename)

# Directory containing DICOM files
directory = '/CHAOS/CHAOS_Train_Sets/CT'
save_folder = '/CHAOS'

i=1
# Iterate through all items in the base directory
for vol in os.listdir(directory):
    vol_path = os.path.join(directory, vol)

    # Check if the item is a directory
    if os.path.isdir(vol_path):
        dicom_folder = os.path.join(vol_path, 'DICOM_anon')
        # dicom_folder = find_deepest_subfolder(vol_path) # Use if there are nested sub-folders
        print(f"Working with: {dicom_folder}")
        img_volume = load_dicom_series(dicom_folder)
        save_nifti(img_volume, os.path.join(save_folder, 'imagesTr', f'chaos_{i:02}.nii.gz'))


        i=i+1
