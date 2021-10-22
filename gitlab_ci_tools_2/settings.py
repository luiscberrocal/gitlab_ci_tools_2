import configparser
import os
from pathlib import Path


def create_configuration(config_file):
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'app_is_required': False}
    config['gitlab.com'] = {'ci_token': '',
                            'ci_url_template': "https://gitlab.com/api/v4/projects/{ci_project_id}/variables"}
    with open(config_file, 'w') as cfg_file:
        config.write(cfg_file)
    return config


def get_or_create_configuration(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config


def get_user_configuration_file():
    home = Path.home()
    configuration_folder = home / '.gitlab_ci_tools_2'
    if not os.path.exists(configuration_folder):
        os.mkdir(configuration_folder)
        print(f'Created {configuration_folder}')
    config_file = configuration_folder / 'config.cfg'

    return config_file, os.path.exists(config_file)


if __name__ == '__main__':
    # cfg = get_configuration(fn)
    fn, created = get_user_configuration_file()
    print(f'Created: {created}')
    print(fn)
    if not created:
        create_configuration(fn)
