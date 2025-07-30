# ----------------------
# file: utils/downloader.py
# ----------------------
from datasets import load_dataset
import pandas as pd


def download_ag_news(save_csv=False, output_path="data/ag_news.csv"):
    dataset = load_dataset("ag_news", split="train")
    df = pd.DataFrame(dataset)

    if save_csv:
        df.to_csv(output_path, index=False)
        print(f"Saved AG News to {output_path}")

    return df


if __name__ == "__main__":
    download_ag_news(save_csv=True)
