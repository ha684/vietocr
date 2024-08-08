from vietocr.model.trainer import Trainer
from vietocr.tool.config import Cfg

config = Cfg.load_config_from_name('vgg_seq2seq')

dataset_params = {
    'name': 'ha',
    'data_root': r'D:\Data\New folder\en_00',
    'train_annotation': 'label_train.txt',
    'valid_annotation': 'label_test.txt'
}

params = {
    'print_every': 1,
    'valid_every': 15 * 200,
    'iters': 100000,
    'checkpoint': './checkpoint/seq2seqocr_checkpoint.pth',
    'export': './weights/seq2seq.pth',
    'metrics': 10000,
    'patience': 10
}

config['trainer'].update(params)
config['dataset'].update(dataset_params)
config['device'] = 'cuda'
config['dataloader']['num_workers'] = 0

trainer = Trainer(config, pretrained=True)
trainer.train()
config.save('config.yml')


