import cv2
import os
import re

class ExperimentImages(object):
    def __init__(self, experiment_dir):
        self._time_dir_re = re.compile('[tT](\d+)')
        self._image_re = re.compile('([a-zA-Z]\d+)[tT](\d+).(jpg|JPG)')
        self._experiment_dir = experiment_dir
        self._pic_dir = os.path.join(experiment_dir, "pic")
        self._times = [x.name for x in os.scandir(self._pic_dir) if x.is_dir() and self._time_dir_re.match(x.name)]
        self._times.sort(key=lambda t: int(t[1:]))
    
    def list_subjects(self):
        t_dirs = [os.path.join(self._pic_dir, t) for t in self._times]
        subjects = set()
        for t in t_dirs:
            subjects.update([self._image_re.match(x.name).group(1) for x in os.scandir(t) if x.is_file() and self._image_re.match(x.name)])
        subjects = list(subjects)
        subjects.sort()
        return subjects

    def list_times(self):
        return self._times

    def get_subject_images(self, subject_id):
        subjects = self.list_subjects()
        if not subject_id in subjects:
            raise ValueError('Subject {} not found in experiment directory.'.format(subject_id))
        times = self.list_times()
        images = []
        for t in times:
            img_path = os.path.join(self._pic_dir, t, '{}{}.jpg'.format(subject_id, t))
            img = cv2.imread(img_path)
            images.append(img)
        return images