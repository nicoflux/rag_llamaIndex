# RAG LlamaIndex

This repository contains a project that implements a basic Retrieval-Augmented Generation (RAG) system using the LlamaIndex library. The project includes a Python starter script (`starter.py`) that loads documents, processes them, and interacts with the LlamaIndex system to build a vector store for document search and retrieval.

## Repository Structure

- `starter.py`: The main Python script that sets up and runs the project. It includes the following steps:
  - Loading documents from a specified directory.
  - Building a vector store using LlamaIndex.
  - Handling embeddings and processing.

- `data/`: A directory that contains sample PDF documents (`Owners_Manual x.pdf`, `Owners_Manual y.pdf`). These are used as sample data for the RAG system.

## Setup Instructions

1. **Environment Setup**:
   Ensure you have Python 3.x installed, and install the required libraries for the project. The key dependency is `llama_index`. You can install it via:

   ```bash
   pip install llama_index
   ```

2. **Usage**:
   Run the `starter.py` script to load the documents from the `data/` folder and process them with LlamaIndex. The vector store will be built, enabling efficient retrieval of information from the documents.

   ```bash
   python starter.py
   ```

## Sample Data

The `data/` directory contains two sample PDF documents that are used to demonstrate how the system processes and indexes files. You can add your own documents in this directory if you wish to extend the functionality.

## Customization

You can modify the `starter.py` script to:
- Use different types of documents.
- Implement additional processing steps or adjust the embedding parameters to fine-tune the behavior of the LlamaIndex.
