_base_ = ['../bevfusion_lidar-cam_voxel0075_second_secfpn_8xb4-cyclic-20e_nus-3d.py']

train_dataloader = dict(
    batch_size=2)
auto_scale_lr = dict(enable=True, base_batch_size=32)
vis_backends = [dict(type='LocalVisBackend'), dict(type='TensorboardVisBackend')]
visualizer = dict(
    type='Det3DLocalVisualizer', vis_backends=vis_backends, name='visualizer')
train_cfg = dict(by_epoch=True, max_epochs=12, val_interval=2)