'''
Code to view 2D DICOM files volume-wise

Details
-> The script uses pydicom to read DICOM files and matplotlib to display the images.
-> DICOM images are displayed in grayscale using the bone colormap, which is often used for medical images. You can change the colormap if needed.
-> Also displayed image sizes. 
-> This script assumes that the DICOM files are in a single directory and reads every file with a .dcm extension. If your files are structured differently, you may need to adjust the file loading logic.
-> Since I have a large number of images, I have added keyboard controls to navigate through them.
'''

import pydicom
import matplotlib.pyplot as plt
import os

class DicomViewer:
    def __init__(self, dicom_directory):
        self.dicom_directory = dicom_directory
        self.file_names = [f for f in os.listdir(dicom_directory) if f.endswith('.dcm')]
        self.index = 0

    def load_dicom(self, index):
        """ Load a DICOM file by index. """
        file_path = os.path.join(self.dicom_directory, self.file_names[index])
        return pydicom.dcmread(file_path)

    def show_dicom_image(self, dicom):
        """ Show a DICOM image. """
        plt.imshow(dicom.pixel_array, cmap=plt.cm.bone)
        image_size = dicom.pixel_array.shape
        plt.title(f"Image {self.index + 1} of {len(self.file_names)} - Size: {image_size[0]}x{image_size[1]}")
        plt.show()

    def on_key_event(self, event):
        """ Handle key press event. """
        if event.key == 'right':
            self.index = (self.index + 1) % len(self.file_names)
            self.update_figure()
        elif event.key == 'left':
            self.index = (self.index - 1) % len(self.file_names)
            self.update_figure()

    def update_figure(self):
        """ Update the displayed figure. """
        plt.clf()
        dicom = self.load_dicom(self.index)
        self.show_dicom_image(dicom)
        plt.draw()

    def run(self):
        """ Run the DICOM viewer. """
        fig, _ = plt.subplots()
        fig.canvas.mpl_connect('key_press_event', self.on_key_event)
        self.update_figure()
        plt.show()

def main():
    dicom_directory = 'path/to/your/dicom/files'
    viewer = DicomViewer(dicom_directory)
    viewer.run()

if __name__ == "__main__":
    main()
