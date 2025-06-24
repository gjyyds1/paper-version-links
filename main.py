import requests
import json
import sys
import os
from packaging import version


def get_paper_versions():
    paper_data = {}
    
    # 获取所有版本
    response = requests.get(
        "https://api.papermc.io/v2/projects/paper",
        headers={"accept": "application/json"}
    ).json()
    
    # 使用packaging.version进行版本排序
    versions_list = response["versions"]
    sorted_versions = sorted(versions_list, key=lambda x: version.parse(x), reverse=True)
    
    # 设置最新版本
    paper_data["latest"] = sorted_versions[0]
    
    # 获取每个版本的最新构建
    data = {}
    for ver in sorted_versions:
        response = requests.get(
            f"https://api.papermc.io/v2/projects/paper/versions/{ver}",
            headers={"accept": "application/json"}
        ).json()
        
        version_name = response["version"]
        latest_build = response["builds"][-1]
        latest_build_url = f"https://api.papermc.io/v2/projects/paper/versions/{version_name}/builds/{latest_build}/downloads/paper-{version_name}-{latest_build}.jar"
        data[version_name] = latest_build_url
    
    paper_data["versions"] = data
    return paper_data


if __name__ == "__main__":
    try:
        data = get_paper_versions()
        with open("paper-versions.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print("版本数据已成功保存到 paper-versions.json")
    except KeyboardInterrupt:
        print("检测到键盘中断，正在停止程序")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
    except Exception as e:
        print(f"发生错误: {str(e)}")
        sys.exit(1)
