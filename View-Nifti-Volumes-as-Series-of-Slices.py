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
nii_file = '/usr/sci/scratch/rachaell/raw_datasets/SLiver07/nifti-slices/sliver_0016.nii.gz'  # Replace with your file path
img = nib.load(nii_file)
data = img.get_fdata()
print(data.shape)

# Initial slice number
slice_num = data.shape[2] // 2
total_slices = data.shape[2]

# Create the main window
root = tk.Tk()
root.title("NIfTI Slice Viewer")

# Create a matplotlib figure and axis
fig, ax = plt.subplots()
img_plot = ax.imshow(data[:, :, slice_num], cmap='gray')
ax.set_title(f"Slice {slice_num}/{total_slices}")


# Function to update the slice
def update_slice(num):
    global slice_num
    slice_num = num
    img_plot.set_data(data[:, :, slice_num])
    ax.set_title(f"Slice {slice_num}/{total_slices}")
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
