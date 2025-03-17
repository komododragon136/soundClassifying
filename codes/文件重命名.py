import os

def add_prefix_to_wav_files(folder_path, prefix="7_"):
    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)

    # 遍历文件
    for file in files:
        # 获取文件的完整路径
        file_path = os.path.join(folder_path, file)

        # 检查文件是否为 .wav 文件
        if os.path.isfile(file_path) and file.lower().endswith('.wav'):
            # 构造新的文件名，给文件名前加上 "7_"
            new_name = prefix + file
            new_file_path = os.path.join(folder_path, new_name)

            # 重命名文件
            os.rename(file_path, new_file_path)
            print(f"Renamed {file} to {new_name}")
        else:
            print(f"Skipped {file}, not a WAV file or a directory")

if __name__ == '__main__':
    # 输入文件夹路径
    folder_path = 'E:/光纤大创训练/10月csdn借鉴/AudioClassification-Pytorch/dataset/数据处理结果/内光纤/分类后文件/内光纤敲击/周日敲击wav'  # 请替换为实际的文件夹路径

    add_prefix_to_wav_files(folder_path)
