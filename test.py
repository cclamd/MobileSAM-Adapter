# import os
#
#
# def find_unique_basename_files(folder_path):
#     """
#     返回文件夹中文件名（减去后缀）只出现一次的文件的列表。
#     """
#     files = os.listdir(folder_path)
#
#     # 创建一个字典来统计每个基本文件名的出现次数
#     basename_count = {}
#     for f in files:
#         basename = os.path.splitext(f)[0]
#         basename_count[basename] = basename_count.get(basename, 0) + 1
#
#     # 找出只出现一次的文件名
#     unique_files = [f for f in files if basename_count[os.path.splitext(f)[0]] == 1]
#
#     return unique_files
#
# folder_path = r"C:\Users\Administrator\Downloads\png_folder_new"
# print(find_unique_basename_files(folder_path))
#
# #
# # import os
# #
# # # 文件夹路径
# # source_folder = r"D:\cut_pic_new"  # 源文件夹，包含要遍历的图片
# # target_folder = r"C:\Users\Administrator\Downloads\png_folder_new"  # 目标文件夹，要删除的图片所在的文件夹
# #
# # # 获取源文件夹中的所有文件名（不包含扩展名）
# # source_files = [os.path.splitext(f)[0] for f in os.listdir(source_folder)]
# #
# # # 获取目标文件夹中的所有文件名（不包含扩展名）
# # target_files = [os.path.splitext(f)[0] for f in os.listdir(target_folder)]
# #
# # # 找到不相同的文件名
# # different_files = list(set(source_files) - set(target_files))
# #
# # # 遍历不相同的文件名，删除源文件夹中的对应文件
# # for different_file in different_files:
# #     source_file_path = os.path.join(source_folder, different_file)
# #
# #     # 构建文件路径（加上扩展名）
# #     source_image_path = f"{source_file_path}.jpg"  # 假设是jpg扩展名
# #
# #     # 如果文件存在，删除
# #     if os.path.exists(source_image_path):
# #         os.remove(source_image_path)
# #         print(f"Deleted: {source_image_path}")
# #     else:
# #         print(f"File not found: {source_image_path}")
#
#
#
# import os
# import shutil
#
# def find_and_copy_different_files(source_folder1, source_folder2, destination_folder):
#     # 获取两个文件夹中的文件列表
#     files1 = set(os.listdir(source_folder1))
#     files2 = set(os.listdir(source_folder2))
#
#     # 在两个文件夹中查找不同的文件
#     different_files = files1.symmetric_difference(files2)
#
#     # 确保目标文件夹存在
#     if not os.path.exists(destination_folder):
#         os.makedirs(destination_folder)
#
#     # 在循环中添加调试输出
#     for file in different_files:
#         source_path1 = os.path.join(source_folder1, file)
#         source_path2 = os.path.join(source_folder2, file)
#         destination_path = os.path.join(destination_folder, file)
#
#         print(f"Checking file: {file}")
#         print(f"Source path 1: {source_path1}")
#         print(f"Source path 2: {source_path2}")
#         print(f"Destination path: {destination_path}")
#
#         # 仅在一个源文件夹中找到文件时执行复制
#         if os.path.exists(source_path1) and not os.path.exists(destination_path):
#             print("Copying from source 1")
#             shutil.copy(source_path1, destination_path)
#         elif os.path.exists(source_path2) and not os.path.exists(destination_path):
#             print("Copying from source 2")
#             shutil.copy(source_path2, destination_path)
#
#
# # 两个源文件夹和目标文件夹的路径
# source_folder1 = r'D:\cut_pic_new'
# source_folder2 = r'D:\cut_pic'
# destination_folder = r'cut_pic_left'
#
#
#
# # 调用函数来执行操作
# find_and_copy_different_files(source_folder1, source_folder2, destination_folder)
#
#
#
#
# from PIL import Image
# import os
#
# # 读取图像
# image_path = r"D:\new_cutpic\0.jpg"
# image = Image.open(image_path)
#
# # 进行图像处理，例如裁剪、缩放等
# # ...
#
# new_filename = image_path.replace(".jpg", "")
#
# # 保存图像，指定保存格式
# image.save(new_filename+'.png', format="PNG")  # 保存为PNG格式，你可以根据需要选择不同的格式，如JPEG等

# from PIL import Image
# import os
#
# valid_formats = ["PNG", "JPEG", "GIF"]  # PIL 支持的有效格式列表
#
# folder_path = r"D:\new_cutpic"  # 替换为你的文件夹路径
#
# for filename in os.listdir(folder_path):
#     if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
#         image_path = os.path.join(folder_path, filename)
#         try:
#             img = Image.open(image_path)
#             format_to_use = img.format.upper()
#
#             if format_to_use in valid_formats:
#                 # print(f"{filename}: Valid format ({format_to_use})")
#                 continue
#             else:
#                 print(f"{filename}: Unsupported format ({format_to_use})")
#
#         except Exception as e:
#             print(f"Error processing {filename}: {e}")
# import os
# import shutil
#
# def find_unique_basename_files_and_move(folder_path, destination_folder):
#     """
#     返回文件夹中文件名（减去后缀）只出现一次的文件的列表，并将这些文件剪切到目标文件夹。
#     """
#     files = os.listdir(folder_path)
#
#     # 创建一个字典来统计每个基本文件名的出现次数
#     basename_count = {}
#     for f in files:
#         basename = os.path.splitext(f)[0]
#         basename_count[basename] = basename_count.get(basename, 0) + 1
#
#     # 找出只出现一次的文件名
#     unique_files = [f for f in files if basename_count[os.path.splitext(f)[0]] == 1]
#
#     # 将只出现一次的文件剪切到目标文件夹
#     for f in unique_files:
#         source_path = os.path.join(folder_path, f)
#         destination_path = os.path.join(destination_folder, f)
#         shutil.move(source_path, destination_path)
#
#     return unique_files
#
# folder_path = r"C:\Users\Administrator\Downloads\png_new_cutpic"
# destination_folder = r"C:\Users\Administrator\Downloads\unique_files"
# unique_files = find_unique_basename_files_and_move(folder_path, destination_folder)
# print(unique_files)


import os
import shutil

def copy_matching_files(source_folder, target_folder):
    """
    在目标文件夹中查找与源文件夹中的文件名字相同的文件（去除扩展名），并将它们拷贝到源文件夹中。
    """
    source_files = set([os.path.splitext(f)[0] for f in os.listdir(source_folder)])
    target_files = set([os.path.splitext(f)[0] for f in os.listdir(target_folder)])

    matching_files = source_files.intersection(target_files)

    for filename in matching_files:
        source_file_path = os.path.join(target_folder, f"{filename}.jpg")  # 源文件路径
        target_file_path = os.path.join(source_folder, f"{filename}.jpg")  # 目标文件路径
        shutil.copy(source_file_path, target_file_path)
        print(f"Copied {filename}.jpg to {source_folder}")

source_folder = r"C:\Users\Administrator\Downloads\png_new_cutpic"  # 替换为源文件夹路径
target_folder = r"D:\new_cutpic"  # 替换为目标文件夹路径
copy_matching_files(source_folder, target_folder)
