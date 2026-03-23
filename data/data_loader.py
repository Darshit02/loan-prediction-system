import pandas as pd 
import yaml

def load_config(path="src/config/config.yaml"):
    with open(path , "r") as file:
        config = yaml.safe_load(file)
    return config


def load_dataset():
    config = load_config()
    data_path = config["data"]["raw_data_path"]
    df = pd.read_csv(data_path)
    return df

if __name__ == "__main__" :
    df = load_dataset()
    print("DataSet Loaded successfully")
    print(df.head())
    print("Shape:" , df.shape)