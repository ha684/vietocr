from vietocr.model.trainer import Trainer
from vietocr.tool.config import Cfg

config = Cfg.load_config_from_name('vgg_seq2seq')

dataset_params = {
    'name': 'ha',
    'data_root': '/kaggle/input/data-line/data_line/',
    'train_annotation': 'train_line_annotation.txt',
    'valid_annotation': 'test_line_annotation.txt'
}

params = {
    'print_every': 100,
    'valid_every': 15 * 200,
    'iters': 100000,
    'checkpoint': './checkpoint/seq2seqocr_checkpoint.pth',
    'export': './weights/seq2seq.pth',
    'metrics': 10000
}

config['trainer'].update(params)
config['dataset'].update(dataset_params)
config['device'] = 'cuda'
config['dataloader']['num_workers'] = 0

trainer = Trainer(config, pretrained=True)
trainer.train()


