# dataset settings
dataset_type = 'MS2D'
data_root = 'data/fasdf'
img_norm_cfg = dict(
    mean=[0], std=[1], to_rgb=False)
train_pipeline = [
    dict(type='LoadImageFromFile', imdecode_backend='pillow', color_type = 'color'),
    dict(type='LoadAnnotations', reduce_zero_label=False),
    dict(type='Resize', img_scale=(256, 256), keep_ratio=True),
    dict(type='RandomFlip', prob=0.5),
    dict(type = 'GaussNoise'),
    dict(type='Normalize', **img_norm_cfg),
    # dict(type='Pad', size=crop_size, pad_val=0, seg_pad_val=255),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_semantic_seg']),
]
# val_pipeline = [
#     dict(type='LoadImageFromFile', imdecode_backend='pillow', color_type = 'grayscale'),
#     # dict(type='LoadAnnotations', reduce_zero_label=True),
#     dict(type='Resize', img_scale=(512, 512), keep_ratio=True),
#     dict(type='Normalize', **img_norm_cfg),
#     dict(type='RandomFlip', prob=0.5),
#     # dict(type='Pad', size=crop_size, pad_val=0, seg_pad_val=255),
#     dict(type='DefaultFormatBundle'),
#     dict(type='Collect', keys=['img']) # , meta_keys=["filename"]
# ]

test_pipeline = [
    dict(type='LoadImageFromFile', imdecode_backend='pillow', color_type = 'color'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(512, 512),
        # img_ratios=[0.5, 0.75, 1.0, 1.25, 1.5, 1.75],
        flip=False,
        transforms=[
            dict(type='Resize', img_scale=(512, 512), keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir='images/training',
        ann_dir='masks/training',
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir='images/validation',
        ann_dir='masks/validation',
        pipeline=test_pipeline),
    test=dict(# added for inference
        type=dataset_type,
        data_root=data_root,
        img_dir='images/validation',
        ann_dir='masks/validation',
        pipeline=test_pipeline))
