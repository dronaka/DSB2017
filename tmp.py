import torch
from config_submit import config as config_submit

checkpoint = torch.load(config_submit['classifier_param'])