config = {
    'datapath': './DSB2017/data',
    'preprocess_result_path': './DSB2017/prep_result/',
    'outputfile': 'prediction.csv',
    'detector_model': 'net_detector',
    'detector_param': './DSB2017/model/detector.ckpt',
    'classifier_model': 'net_classifier',
    'classifier_param': './DSB2017/model/classifier.ckpt',
    'n_gpu': 1,
    'n_worker_preprocessing': None,
    'use_exsiting_preprocessing': False,
    'skip_preprocessing': False,
    'skip_detect': False
}
