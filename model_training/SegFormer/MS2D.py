# Copyright (c) OpenMMLab. All rights reserved.
# originally located in mmseg/datasets
import os.path as osp

import mmcv
import numpy as np
from PIL import Image
import os
from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class MS2D(CustomDataset):
    """IF dataset.

    In segmentation map annotation for ADE20K, 0 stands for background, which
    is not included in 150 categories. ``reduce_zero_label`` is fixed to True.
    The ``img_suffix`` is fixed to '.jpg' and ``seg_map_suffix`` is fixed to
    '.png'.
    """
    CLASSES = ('background', 'organoid')

    PALETTE = [[0], [1]]

    def __init__(self, **kwargs):
        super(MS2D, self).__init__(
            img_suffix='.jpg',
            seg_map_suffix='_label.tif',
            reduce_zero_label=False,
            **kwargs)

    def results2img(self, results, imgfile_prefix, to_label_id, file_info, indices=None):
        """Write the segmentation results to images.

        Args:
            results (list[ndarray]): Testing results of the
                dataset.
            imgfile_prefix (str): The filename prefix of the png files.
                If the prefix is "somepath/xxx",
                the png files will be named "somepath/xxx.png".
            to_label_id (bool): whether convert output to label_id for
                submission.
            indices (list[int], optional): Indices of input results, if not
                set, all the indices of the dataset will be used.
                Default: None.

        Returns:
            list[str: str]: result txt files which contains corresponding
            semantic segmentation images.
        """
        if indices is None:
            indices = list(range(len(self)))

        mmcv.mkdir_or_exist(imgfile_prefix)
        result_files = []
        for result, idx in zip(results, indices):

            filename = self.img_infos[idx]['filename']
            basename = osp.splitext(osp.basename(filename))[0]
            dice = file_info[idx]

            png_filename = osp.join(imgfile_prefix, f'{basename}_dice-{dice:.2f}.png')

            # The  index range of official requirement is from 0 to 150.
            # But the index range of output is from 0 to 149.
            # That is because we set reduce_zero_label=True.
            result = result + 1

            output = Image.fromarray((result*128).astype(np.uint8), "L")
            output.save(png_filename)
            result_files.append(png_filename)

        return result_files

    def clear_outdir(self, outdir):
        for f in os.listdir(outdir):
            assert f.endswith(self.seg_map_suffix) or f.endswith(".txt") or f.endswith('.png') or f.endswith('Thumbs.db')
            if f != 'Thumbs.db':
                os.remove(os.path.join(outdir, f))

    def format_results(self,
                       results,
                       imgfile_prefix,
                       file_info,
                       to_label_id=True,
                       indices=None):
        """Format the results into dir (standard format for ade20k evaluation).

        Args:
            results (list): Testing results of the dataset.
            imgfile_prefix (str | None): The prefix of images files. It
                includes the file path and the prefix of filename, e.g.,
                "a/b/prefix".
            to_label_id (bool): whether convert output to label_id for
                submission. Default: False
            indices (list[int], optional): Indices of input results, if not
                set, all the indices of the dataset will be used.
                Default: None.

        Returns:
            tuple: (result_files, tmp_dir), result_files is a list containing
               the image paths, tmp_dir is the temporal directory created
                for saving json/png files when img_prefix is not specified.
        """
        self.clear_outdir(imgfile_prefix)
        if indices is None:
            indices = list(range(len(self)))

        assert isinstance(results, list), 'results must be a list.'
        assert isinstance(indices, list), 'indices must be a list.'

        result_files = self.results2img(results, imgfile_prefix, to_label_id, file_info,
                                        indices)
        return result_files
