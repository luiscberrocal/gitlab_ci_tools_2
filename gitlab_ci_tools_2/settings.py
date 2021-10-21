import configparser


def get_configuration(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

if __name__ == '__main__':
    fn ='/home/luiscberrocal/PycharmProjects/gitlab_ci_tools_2/gitlab_ci_tools_2/config.cfg'
    cfg = get_configuration(fn)
