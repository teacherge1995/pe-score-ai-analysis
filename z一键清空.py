import os
import shutil


def clean_target_folders(root_dir=None):
    """
    清空指定根目录下的四个目标文件夹 (downloads, templates, templates_download, uploads)
    如果未指定 root_dir，则默认使用当前脚本所在目录
    """
    # 定义要清空的文件夹名称列表
    target_folders = ['downloads', 'templates', 'templates_download', 'uploads']

    # 如果未指定根目录，使用当前脚本所在目录
    if root_dir is None:
        root_dir = os.path.dirname(os.path.abspath(__file__))

    # print(f"开始扫描目录: {root_dir}")

    # 遍历根目录下的所有文件夹
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)

        # 检查是否是目录，且名称在目标列表中
        if os.path.isdir(item_path) and item in target_folders:
            # print(f"正在处理文件夹: {item_path}")

            try:
                # 清空文件夹内的所有内容
                for filename in os.listdir(item_path):
                    file_path = os.path.join(item_path, filename)

                    # 如果是文件或软链接，直接删除
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                        # print(f"  删除文件: {filename}")
                    # 如果是子目录，递归删除
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                        # print(f"  删除目录: {filename}")

                # print(f"✅ 文件夹 {item} 清空成功\n")

            except Exception as e:
                print(f"❌ 清空 {item_path} 失败。原因: {str(e)}\n")

    # print("所有目标文件夹处理完毕！")


# --- 运行代码 ---
if __name__ == "__main__":
    # 方式1：默认清空当前脚本所在目录下的四个文件夹
    clean_target_folders()

    # 方式2：如果你的系统.py文件在其他目录，可指定根路径，例如：
    # clean_target_folders(root_dir=r"C:\Your\Project\Path")