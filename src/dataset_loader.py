import cv2, os, sys
from pathlib import Path
from skimage.feature import hog
from multiprocessing import Pool, set_start_method, freeze_support

try:

    if sys.platform == 'win32':
        freeze_support()
        set_start_method("spawn")
    else:
        set_start_method("fork")
except RuntimeError:
    pass


class LoadDataset:
    def __init__(self, folder_path):        
        self.folder_path = Path(folder_path).resolve()        
        if not self.folder_path.is_dir() or not self.folder_path.exists():
            raise FileNotFoundError("Directory Not Exists!")
        self.images = list(self.folder_path.iterdir())
        self.length = len(self.images)
        if self.length == 0:
            raise OSError("Directory Empty!")
        self.workers = os.cpu_count()
        print("Workers Assigned: %d" % self.workers)
        
    def _transform_image(self, image_path):
        """ Transforming Image using HOG Technique"""
        raw_image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
        if raw_image is None:
            return None
        raw_image = cv2.resize(raw_image, (64, 64))  
        transformed_image = self._apply_hog(raw_image)
        return transformed_image

    def _apply_hog(self, raw_image):
        """ Applying HOG to Raw Image """
        return hog(
            raw_image,
            orientations=9,
            pixels_per_cell=(8, 8),
            cells_per_block=(2, 2),
            block_norm="L2-Hys"
        )
    
    def load_dataset(self):
        """ Loading Images Parallely using Pool.map() """
        with Pool(processes=self.workers) as pool:
            image_data = pool.map(self._transform_image, self.images)
        return image_data
    