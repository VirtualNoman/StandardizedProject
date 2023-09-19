import configparser


class ConfigRead:
    """读取和管理配置文件的类。配置数据结构:

    [section]
    option=value
    option=value

    Attributes:
        file_path (str): 配置文件的路径。
        conf (configparser.ConfigParser): ConfigParser对象，用于读取和管理配置文件内容。
    Note:
        Remember to use the save_config method to save to a file after modifying the instance
    """

    def __init__(self, configfile_path: str):
        """
        初始化 ConfigRead 类。

        Args:
            configfile_path (str): 配置文件的路径。
        """
        self.file_path = configfile_path
        self.conf = configparser.ConfigParser()
        self.conf.read(self.file_path, encoding='utf-8')

    def read_sections(self) -> list[str]:
        """
        获取配置文件中的所有 sections。

        Returns:
            list[str]: 配置文件中的所有 sections 的列表。
        """
        return self.conf.sections()

    def section_exist(self, section_name) -> bool:
        """
        检查指定的 section 是否存在。

        Args:
            section_name: 要检查的 section 的名称。

        Returns:
            bool: 如果 section 存在则返回 True，否则返回 False。
        """
        return self.conf.has_section(section_name)

    def read_options(self, section) -> list[str]:
        """
        获取指定 section 下的所有 options，即 keys。

        Args:
            section: 要获取 options 的 section 名称。

        Returns:
            list[str]: 指定 section 下的所有 options 的列表。
        """
        return self.conf.options(section)

    def option_exist(self, section, option) -> bool:
        """
        检查指定 section 下的 option 是否存在。

        Args:
            section: option 所属的 section 名称。
            option: 要检查的 option 名称。

        Returns:
            bool: 如果 option 存在则返回 True，否则返回 False。
        """
        return self.conf.has_option(section, option)

    def get_items(self, section) -> list[tuple]:
        """
        获取指定 section 下的所有键值对。

        Args:
            section: 要获取 items 的 section 名称。

        Returns:
            list[tuple]: 指定 section 下的所有键值对的列表。
        """
        return self.conf.items(section)

    def read_value(self, section, option) -> str:
        """
        获取指定 section 下 option 键对应的值。

        Args:
            section: option 所属的 section 名称。
            option: 要获取 value 的 option 名称。

        Returns:
            str: option 键对应的值。
        """
        return self.conf.get(section, option)

    def remove_section(self, section):
        """
        删除指定的 section。

        Args:
            section: 要删除的 section 名称。
        """
        self.conf.remove_section(section)

    def remove_item(self, section, option):
        """
        删除指定 section 下的键值对。

        Args:
            section: 要删除键值对的 section 名称。
            option: 要删除的 option 名称。
        """
        self.conf.remove_option(section, option)

    def add_section(self, section_name):
        """
        添加新的 section。

        Args:
            section_name: 要添加的 section 名称。
        """
        self.conf.add_section(section_name)

    def add_item(self, section, option, value):
        """
        添加新的键值对。

        Args:
            section: 要添加键值对的 section 名称。
            option: 要添加的 option 名称。
            value: option 对应的值。
        """
        self.conf.set(section, option, value)

    def save_config(self):
        """
        保存配置文件更改到文件中，并使其生效。
        """
        with open(self.file_path, "w+") as f:
            self.conf.write(f)
        f.close()