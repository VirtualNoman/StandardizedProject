from StandConfigParse import ConfigRead

if __name__ == "__init__":
    profile_path = "TestProfile.ini"
    config = ConfigRead(profile_path)
    print(config.read_sections())
