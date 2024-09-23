import os

from mmcv import Config
import numpy as np
import mmcv
from mmseg.apis import inference_segmentor, init_segmentor
import os
from torch import nn
from os.path import join as opj


def all_eval_except_dropout(m):
    if not isinstance(m, nn.Dropout) and not isinstance(m, mmcv.cnn.bricks.drop.DropPath) and not isinstance(m, nn.Dropout2d):
        m.eval()
    else:
        if isinstance(m, nn.Dropout2d):
            m.p = 1.0
            m.inplace = True
            m.train()
        print('keep', m, 'active')

def main():
    checkpoints = {
        'split0': '/home/ws/oc9627/mmsegmentation/work_dirs/2d_ms_org_seg_run4_downscale025/split-0/best_mDice_iter_1000.pth',
        'split1': '/home/ws/oc9627/mmsegmentation/work_dirs/2d_ms_org_seg_run4_downscale025/split-1/best_mDice_iter_820.pth',
        'split2': '/home/ws/oc9627/mmsegmentation/work_dirs/2d_ms_org_seg_run4_downscale025/split-2/best_mDice_iter_900.pth',
        'split3': '/home/ws/oc9627/mmsegmentation/work_dirs/2d_ms_org_seg_run4_downscale025/split-3/best_mDice_iter_960.pth',
        'split4': '/home/ws/oc9627/mmsegmentation/work_dirs/2d_ms_org_seg_run4_downscale025/split-4/best_mDice_iter_960.pth'
        }
    for split in range(5):
        img_dir = f'/home/ws/oc9627/mmsegmentation/data/2d_ms_org_seg_run4/images/split{split}_test'
        ckp_dir = os.path.dirname(checkpoints[f'split{split}'])
        outdir_inference = opj(ckp_dir, 'inference_test')
        os.makedirs(outdir_inference, exist_ok=True)

        # load model
        ckp = checkpoints[f'split{split}']
        cfg = Config.fromfile(
            '/home/ws/oc9627/mmsegmentation/work_dirs/2d_ms_org_seg_run4_downscale025/split-0.py')
        cfg.load_from = ckp
        cfg.model.decode_head.norm_cfg = dict(type='BN', requires_grad=True)

        model = init_segmentor(
            cfg, checkpoint=ckp)
        model.apply(all_eval_except_dropout)

        for img_loc in sorted(os.listdir(img_dir)):
            img = os.path.join(img_dir, img_loc)
            img_id = os.path.basename(img).replace('.jpg', '')

            result, _, _ = inference_segmentor(model, img)
            print(img)
            pred = result[0]
            np.save(opj(outdir_inference, f'{img_id}.npy'), pred)
main()