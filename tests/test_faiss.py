"""
=========================================
Test: Build FAISS Index
=========================================
"""

from src.ingestion.build_index import BuildIndex


def main():

    builder = BuildIndex()

    index = builder.build()

    print("\n========== RESULTS ==========\n")

    print(f"Total Stored Vectors : {index.ntotal}")


if __name__ == "__main__":
    main()