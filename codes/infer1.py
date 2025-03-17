import argparse
import functools

from macls.predict import MAClsPredictor
from macls.utils.utils import add_arguments, print_arguments

parser = argparse.ArgumentParser(description=__doc__)
add_arg = functools.partial(add_arguments, argparser=parser)
add_arg('configs',          str,    'configs/cam++2.yml',   '配置文件')
add_arg('use_gpu',          bool,   True,                  '是否使用GPU预测')
add_arg('audio_path',       str,    'dataset/数据处理结果/内光纤/分类后文件/内光纤尾端敲击/4.wav', '音频路径')
add_arg('model_path',       str,    'personalmodels/CAMPPlus_Fbank/best_model/', '导出的预测模型文件路径')
args = parser.parse_args()
print_arguments(args=args)

# 获取识别器
predictor = MAClsPredictor(configs=args.configs,
                           model_path=args.model_path,
                           use_gpu=args.use_gpu)

label, score = predictor.predict(audio_data=args.audio_path)

print(f'音频：{args.audio_path} 的预测结果标签为：{label}，得分：{score}')
