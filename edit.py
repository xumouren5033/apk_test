import argparse
import os

def modify_buildozer_spec(app_name, package_name, domain, version, project_dir):
    spec_file_path = os.path.join(project_dir, 'buildozer.spec')
    
    with open(spec_file_path, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith('title ='):
            lines[i] = f'title = {app_name}\n'
        elif line.startswith('package.name ='):
            lines[i] = f'package.name = {package_name}\n'
        elif line.startswith('package.domain ='):
            lines[i] = f'package.domain = {domain}\n'
        elif line.startswith('version ='):
            lines[i] = f'version = {version}\n'

    with open(spec_file_path, 'w') as file:
        file.writelines(lines)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Modify buildozer.spec file')
    parser.add_argument('--app_name', required=True, help='应用名称')
    parser.add_argument('--package_name', required=True, help='包名')
    parser.add_argument('--domain', required=True, help='域名')
    parser.add_argument('--version', required=True, help='版本号')
    parser.add_argument('--project_dir', required=True, help='项目目录')

    args = parser.parse_args()

    modify_buildozer_spec(args.app_name, args.package_name, args.domain, args.version, args.project_dir)
