# Arachnida Project: Spider & Scorpion

Welcome to the **Arachnida** project, an introduction to web data scraping and metadata manipulation. This project is divided into two main parts: **Spider** and **Scorpion**, allowing you to explore the fundamentals of web scraping and metadata analysis.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Spider: Image Extraction](#spider-image-extraction)
3. [Scorpion: Metadata Analysis](#scorpion-metadata-analysis)

---

## Introduction

This project enables you to process data from the web:
- **Spider**: Create a program to automatically extract images from a website.
- **Scorpion**: Develop a program to analyze and manipulate metadata of image files.

Metadata provides descriptive information about data, often used for images or documents. It can reveal details about the file's creator, creation date, and more.

---

## Spider: Image Extraction

The **Spider** program extracts all images from a given website URL, with optional recursive behavior. It supports the following features:

### Usage:
```bash
./spider [-rlp] URL
```

### Options:
- **`-r`**: Recursively downloads images from the provided URL.
- **`-r -l [N]`**: Specifies the maximum depth level for recursion (default: 5).
- **`-p [PATH]`**: Specifies the directory to save downloaded images (default: `./data/`).

### Supported File Extensions:
- `.jpg/.jpeg`
- `.png`
- `.gif`
- `.bmp`

---

## Scorpion: Metadata Analysis

The **Scorpion** program analyzes image files for EXIF and other metadata.

### Usage:
```bash
./scorpion FILE1 [FILE2 ...]
```

### Features:
- Compatible with the same file extensions as **Spider**.
- Displays basic attributes (e.g., creation date) and EXIF metadata.
- Flexible output format, customizable by the developer.

---

This README provides an overview of the **Spider** and **Scorpion** programs. For more details, consult the project documentation. Good luck!
