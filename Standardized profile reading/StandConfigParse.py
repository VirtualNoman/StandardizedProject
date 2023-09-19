import configparser


class ConfigRead:
    """Classes that read and manage configuration files. Configure data structure:

    [section]
    option=value
    option=value

    Attributes:
        file_path (str): The path to the configuration file.
        conf (configparser.ConfigParser): ConfigParserObject to read and manage configuration file contents.
    Note:
        Remember to use the save_config method to save to a file after modifying the instance
    """

    def __init__(self, configfile_path: str):
        """
        Initialize the ConfigRead class.

        Args:
            configfile_path (str): The path to the configuration file.
        """
        self.file_path = configfile_path
        self.conf = configparser.ConfigParser()
        self.conf.read(self.file_path, encoding='utf-8')

    def read_sections(self) -> list[str]:
        """
        Gets all sections in the configuration file.

        Returns:
            list[str]: A list of all sections in the configuration file.
        """
        return self.conf.sections()

    def section_exist(self, section_name) -> bool:
        """
        Checks whether the specified section exists.

        Args:
            section_name: The name of the section to check.

        Returns:
            bool: True if the section exists, False otherwise.
        """
        return self.conf.has_section(section_name)

    def read_options(self, section) -> list[str]:
        """
        Get all options (keys) in the specified section.

        Args:
            section: The name of the section to get options from.

        Returns:
            list[str]: The list of all options in the specified section.
        """
        return self.conf.options(section)

    def option_exist(self, section, option) -> bool:
        """
        Check if the specified option exists in the specified section.

        Args:
            section: The name of the section where the option belongs.
            option: The name of the option to check.

        Returns:
            bool: True if the option exists, False otherwise.
        """
        return self.conf.has_option(section, option)

    def get_items(self, section) -> list[tuple]:
        """
        Get all key-value pairs in the specified section.

        Args:
            section: The name of the section to get items from.

        Returns:
            list[tuple]: The list of all key-value pairs in the specified section.
        """
        return self.conf.items(section)

    def read_value(self, section, option) -> str:
        """
        Get the value of the specified option in the specified section.

        Args:
            section: The name of the section where the option belongs.
            option: The name of the option to get the value of.

        Returns:
            str: The value of the option.
        """
        return self.conf.get(section, option)

    def remove_section(self, section):
        """
        Remove the specified section.

        Args:
            section: The name of the section to remove.
        """
        self.conf.remove_section(section)

    def remove_item(self, section, option):
        """
        Remove the specified key-value pair in the specified section.

        Args:
            section: The name of the section where the key-value pair belongs.
            option: The name of the option to remove.
        """
        self.conf.remove_option(section, option)

    def add_section(self, section_name):
        """
        Add a new section.

        Args:
            section_name: The name of the section to add.
        """
        self.conf.add_section(section_name)

    def add_item(self, section, option, value):
        """
        Add a new key-value pair.

        Args:
            section: The name of the section where the key-value pair belongs.
            option: The name of the option to add.
            value: The value of the option.
        """
        self.conf.set(section, option, value)

    def save_config(self):
        """
        Save the configuration changes to the file and make them effective.
        """
        with open(self.file_path, "w+") as f:
            self.conf.write(f)
        f.close()