'''
This code is to convert a series of 2d DICOM slices into a 3D Nifti volume.
-> This is implementation for CT Pancrease dataset. Here, there are a lot of unnecessary subfolders, so modify accordingly.

-> Ensure that the DICOM files are from the same series and are correctly oriented.
-> The code assumes that all DICOM files in the directory belong to the same series and are slices of the same volume.
-> The affine transformation matrix used here (np.eye(4)) is an identity matrix. In real scenarios, you might need to use the correct affine matrix from the DICOM headers to preserve spatial orientation and scale.
-> The pixel spacing, slice thickness, and orientation should be consistent across all slices for accurate volume reconstruction.
'''


import os
import pydicom
import numpy as np
import nibabel as nib

def load_dicom_series(directory):
    # Read all DICOM files in the directory
    dicom_files = [pydicom.dcmread(os.path.join(directory, f)) for f in os.listdir(directory) if f.endswith('.dcm')]
    # Sort the DICOM files by their Image Position (Slice Location)
    dicom_files.sort(key=lambda x: float(x.ImagePositionPatient[2]))
    # Combine the pixel data into a single 3D array
    volume = np.stack([file.pixel_array for file in dicom_files], axis=-1)
    return volume

def save_nifti(volume, filename):
    # Convert the numpy array to a NIfTI image
    nifti_img = nib.Nifti1Image(volume, affine=np.eye(4))
    # Save the NIfTI image
    nib.save(nifti_img, filename)


def find_deepest_subfolder(directory):
    deepest_subfolder = None
    max_depth = -1

    for root, dirs, files in os.walk(directory):
        current_depth = root.count(os.sep)
        if current_depth > max_depth and dirs:
            max_depth = current_depth
            deepest_subfolder = os.path.join(root, dirs[-1])

    return deepest_subfolder

# Directory containing DICOM files
dicom_directory = '/usr/sci/scratch/rachaell/raw_datasets/CT-Pancreas/manifest-1599750808610/Pancreas-CT'
i=0
# Iterate through all items in the base directory
for folder_name in os.listdir(dicom_directory):
    folder_path = os.path.join(dicom_directory, folder_name)

    # Check if the item is a directory
    if os.path.isdir(folder_path):
        last_sub_folder_path = find_deepest_subfolder(folder_path)

        print(f"Working with: {last_sub_folder_path}")
       
        # Load DICOM series and save as NIfTI
        volume = load_dicom_series(last_sub_folder_path)
        save_nifti(volume, f'/usr/sci/scratch/rachaell/raw_datasets/CT-Pancreas/nifti-slices/pancreas_{i:04}.nii.gz')
        i=i+1
