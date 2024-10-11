# PDF Processing Pipeline with Summarization & Keyword Extraction

This repository contains a dynamic pipeline to process multiple PDF documents, extract domain-specific summaries and keywords, and store the results in a MongoDB database. The solution prioritizes concurrency, speed, and customization, providing an efficient way to handle PDFs of varying lengths and store the extracted information.

## Features
- **PDF Ingestion & Parsing**: Automatically detects and processes PDFs from a specified folder.
- **Concurrency**: Parallel processing of PDFs to improve speed and efficiency.
- **Summarization**: Generates domain-specific summaries based on the length of the document.
- **Keyword Extraction**: Extracts domain-specific keywords from the text content.
- **MongoDB Integration**: Saves PDF metadata, summaries, and keywords in MongoDB.
- **Error Handling**: Logs errors like corrupted or unsupported files without breaking the pipeline.

## Prerequisites

Make sure you have the following installed:
- Python 3.8+
- MongoDB (Running on `localhost:27017`)
- [Git](https://git-scm.com/)
- [pip](https://pip.pypa.io/en/stable/) (Python package manager)

## Setup Instructions

### Step 1: Clone the Repository

Clone this repository to your local machine using the command:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
### Step 2: Install Dependencies
The project relies on several Python libraries. You can install all the required dependencies using pip:
```bash
pip install -r requirements.txt
```
### Required Libraries

- **pymongo**
- **PyPDF2**
- **requests**
- **transformers**
- **sentence-transformers**
- **torch**
- **concurrent.futures**

### Step 3: Setup MongoDB

Ensure that MongoDB is installed and running on your system. By default, it should be available at mongodb://127.0.0.1:27017/. If it's not running, start MongoDB using:

```bash
mongod
```

### Step 4: Download PDF Dataset

The PDF dataset for this project is provided in a separate GitHub repository. You can download it by running:

```bash
git clone https://github.com/Devian158/AI-Internship-Task.git
```

### Step 5: Run the Pipeline

To run the pipeline and process the PDFs, use the following command:

```bash
python app.py
```
### This will:

- **Ingest and parse all PDFs from the specified folder.**
- **Extract summaries and keywords for each PDF.**
- **Save the metadata, extracted summaries, and keywords in the MongoDB database.**

### Step 6: Check MongoDB

You can inspect the saved PDF data in MongoDB by connecting to your local MongoDB instance. You can use a tool like MongoDB Compass or connect via the terminal:

```bash
mongo
use PdfData
db.data.find().pretty()
```

## Project Structure

```bash
|---- utils/

|   |-- pusher.py         # MongoDB interaction logic
|   |-- extractor.py      # Logic for extracting text, keywords, and summaries
|   |-- downloader.py     # Handles downloading PDFs from links
|    |-- summerizer        # summerizing the texts
    

|-- downloads/            # Folder where downloaded PDFs are stored
|-- logs/                 # Log files for error and info tracking
|-- pdf_data.json         # JSON file storing extracted PDF data (optional backup)
|-- app.py                # To run all the function with single command
|-- requirements.txt      # Python dependencies
|-- playground.ipynb      # To test the functions and custom modules

```

## Error Handling

- All errors, such as corrupted PDFs or unsupported formats, are logged in the ```pdf_processing.log``` file in the ```logs/``` folder.
- MongoDB entries are unaffected by files with errors, ensuring the pipeline continues smoothly.


## Performance Benchmarks

The pipeline is designed for efficient processing, and here are the approximate performance metrics when handling a batch of PDF documents:

- **PDF Downloading**: The download process for all PDFs takes approximately **40-50 seconds**, depending on the number of files and the network speed.
- **PDF Extraction**: Extracting text content from the PDFs takes around **1 minute** for a batch of documents, assuming a mix of short and long PDFs.
- **Keyword Extraction**: The keyword extraction step takes about **30 seconds** for all documents.
- **Summarization**: Generating summaries for all documents takes around **2 minutes**, with longer PDFs requiring more time for summarization.

These times are based on a sample dataset of PDFs. Actual performance may vary depending on system resources, file sizes, and the number of documents processed concurrently.

You can find more detailed performance logs in the `pdf_processing.log` file located in the `logs/` folder.


### License
This project is licensed under the MIT License. See the LICENSE file for details.

## Authors
- **Shivam - Project Owner and Developer**

## Acknowledgments
Special thanks to:

- The developers of the transformers library for providing easy-to-use summarization models.
- The creators of PyPDF2 and pdfplumber for making PDF text extraction accessible in Python.
