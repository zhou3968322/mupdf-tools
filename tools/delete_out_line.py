# -*- coding:utf-8 -*-
# email:bingchengzhou@foxmail.com
# create: 2021/3/11
import fitz
import argparse


def main(pdf_file_path, out_pdf_path):
    doc = fitz.Document(pdf_file_path)
    for outline_xref in doc.get_outline_xrefs():
        doc._deleteObject(outline_xref)
    doc.save(out_pdf_path)
    doc.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_pdf_path", "-i", default=str, help="input pdf path")
    parser.add_argument("--output_pdf_path", "-o", default=str, help="output pdf path")
    args = parser.parse_args()
    main(args.input_pdf_path, args.output_pdf_path)