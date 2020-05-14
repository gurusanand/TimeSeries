import re
import os
import glob
import pandas as pd


def split_pages(data):
  return list(filter(None, map(
      str.strip, map(str, data.split('\x0c')))))


all_data = []
base_dir = r"J:\PQM Share\RDS"
save_dir = r""
save_fname = os.path.join(save_dir, 'results.xlsx')
fpaths = glob.glob(os.path.join(base_dir, '*.txt'))
page_search_sent = 'ELECTRONIC AND FAX INSTRUCTIONS AUTHORISATION AND INDEMNITY LETTER'
company_pattern = re.compile(r'^Company:\s+(.*)$', re.IGNORECASE)
inst_line_pattern = re.compile(r"^\(([A-H]{1})\).+\((.*)\)", re.IGNORECASE)
inst_pattern = re.compile(r'\((.*?)\)')
results = {
    'company_name': [],
    'instructions': []
}

for fpath in fpaths:
  with open(fpath, 'r', encoding='utf8') as infile:
    data = infile.read()
  all_data += split_pages(data)

for data in all_data:
  if page_search_sent in data:
    company_name, instructions = [], []
    for line in data.splitlines():
      inst_line_match = re.search(inst_line_pattern, line)
      company_match = re.findall(company_pattern, line)
      if inst_line_match:
        instructions.append(re.findall(inst_pattern, line)[1])
        print(f'Instruction: {re.findall(inst_pattern, line)[1]}')
      elif company_match:
        company_name.append(company_match[0])
        print(f'Company Name: {company_match[0]}')
    results['company_name'].append(company_name[0])
    results['instructions'].append(', '.join(instructions))

df = pd.DataFrame(results)
df.to_excel(save_fname)
