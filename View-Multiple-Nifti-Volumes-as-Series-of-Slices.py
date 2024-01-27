'''
This code helps us view a 3d NIFTI volume as a series of slices using <> keys
-> Starts from the middle slice and displays the [current slice number/ total number of slices]
-> Assumes the shape to be of the format [x,x,#slices] where [x,x] is the shape of each slice
'''
import tkinter as tk
from tkinter import Button
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import nibabel as nib

# Load the NIfTI file
ground_nii_file = '/usr/sci/scratch/rachaell/raw_datasets/Femur/Sli2Vol_predictions/n09_R_femur.nii.gz'  # Replace with your file path
pred_nii_file = '/usr/sci/scratch/rachaell/raw_datasets/Femur/Sli2Vol_predictions/n09_R_femur_pred.nii.gz'  # Replace with your file path
ground_img = nib.load(ground_nii_file)
ground_data = ground_img.get_fdata()
pred_img = nib.load(pred_nii_file)
pred_data = pred_img.get_fdata()
print(ground_data.shape, pred_data.shape)

# Initial slice number
slice_num = ground_data.shape[2] // 2
total_slices = ground_data.shape[2]

# Create the main window
root = tk.Tk()
root.title("NIfTI Slice Viewer")

'''# Create a matplotlib figure and axis
fig, ax = plt.subplots()
img_plot = ax.imshow(data[ :, :, slice_num], cmap='gray')
ax.set_title(f"Slice {slice_num}/{total_slices}")'''

fig, (ax1, ax2) = plt.subplots(1, 2)
img_plot1 = ax1.imshow(ground_data[:, :, slice_num], cmap='gray')
img_plot2 = ax2.imshow(pred_data[:, :, slice_num], cmap='gray')
ax1.set_title(f"GroundTruth - Slice {slice_num}/{total_slices}")
ax2.set_title(f"Prediction - Slice {slice_num}/{total_slices}")


# Function to update the slice
def update_slice(num):
    global slice_num
    slice_num = num
    img_plot1.set_data(ground_data[ :, :, slice_num])
    img_plot2.set_data(pred_data[ :, :, slice_num])
    ax1.set_title(f"GroundTruth - Slice {slice_num}/{total_slices}")
    ax2.set_title(f"Prediction - Slice {slice_num}/{total_slices}")
    canvas.draw()

# Add matplotlib figure to tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=0, columnspan=2)

# Add navigation buttons
prev_button = Button(root, text="Previous Slice", command=lambda: update_slice(max(slice_num - 1, 0)))
prev_button.grid(row=1, column=0)

next_button = Button(root, text="Next Slice", command=lambda: update_slice(min(slice_num + 1, data.shape[2] - 1)))
next_button.grid(row=1, column=1)

# Start the GUI event loop
root.mainloop()
