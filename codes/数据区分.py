import os
import shutil

def move_wav_files(src_folder, dest_folder):
    # 检查目标文件夹是否存在，如果不存在就创建
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # 获取源文件夹中的所有文件
    files = os.listdir(src_folder)

    # 遍历文件
    for file in files:
        # 获取文件的完整路径
        file_path = os.path.join(src_folder, file)
        
        # 检查文件是否为文件，而不是文件夹
        if os.path.isfile(file_path):
            # 如果文件是 .wav 文件
            if file.lower().endswith('.wav'):
                # 构造目标路径
                dest_path = os.path.join(dest_folder, file)
                # 移动文件
                shutil.move(file_path, dest_path)
                print(f"Moved {file} to {dest_folder}")
            else:
                print(f"Skipped {file}, not a WAV file")
        else:
            print(f"Skipped {file}, it's a directory")

if __name__ == '__main__':
    # 输入源文件夹和目标文件夹
    src_folder = 'E:/光纤大创训练/10月csdn借鉴/AudioClassification-Pytorch/dataset/数据处理结果/内光纤/周日敲击'  # 请替换为实际的源文件夹路径
    dest_folder = 'E:/光纤大创训练/10月csdn借鉴/AudioClassification-Pytorch/dataset/数据处理结果/内光纤/周日敲击wav'  # 请替换为实际的目标文件夹路径

    move_wav_files(src_folder, dest_folder)