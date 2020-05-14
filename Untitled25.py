
# coding: utf-8

# In[2]:


import re

data = """
TELEPHONE, ELECTRONIC AND FAX INSTRUCTIONS AUTHORISATION AND INDEMNITY LETTER*
To; MIZUHO BANK, LTD.
12 Marina View
#08-01 Asia Square Tower 2
Singapore 018961
Dear Sirs,
Company: Oriental Barko Panama S.A
Address: 10 Anson Road #17-11 International Plaza Singapore 079903
Number: 6227 3557(Tel); 6227 2747 (Fax)
1.	MIZUHO BANK, LTD. (the "Bank") is hereby instructed to accept and act upon
any instructions, notices, communication, orders, messages, information or other material (collectively "Instructions") given or purported to be given by or on behalf of the abovenamed Company (the "Company"), to the Bank, in connection with accounts held with the Bank by the Company, services provided or agreed to be provided by the Bank to the Company and/or facilities which may from time to time be made available by the Bank to the Company, which Instructions are:
(a)	communicated orally by telephone ("Telephone Instructions"):
(b)	transmitted by facsimile ("Fax Instructions1'):
(c)	communicated or transmitted to the Bank via electronic mail or if applicable, any other electronic means ("Electronic Instructions"): or
(d)	Electronic Instructions followed by original and signed hard copies of Electronic Instructions ("Secured Electronic Instructions"),
where:
(i)	such Telephone Instructions or Electronic Instructions are given or purported to have been given by (in the Bank's or an Officer's reasonable belief), and such Fax Instructions or Secured Electronic Instructions are signed or purported to have been signed by, the person(s) who are, at the time of communication or receipt thereof, as the case may be, persons who have been notified by the Company to the Bank in any notice, mandate, resolution, power of attorney or other document or instrument given by the Company to the Bank, as being authorised by the Company to give Instructions to the Bank, or as authorised signatory(ies) of the Company (each, an "Authorised Person'’), whether or not the Instructions are actually authorised by the Company; and
(ii)	such Electronic Instructions and Secured Electronic Instructions have been received by the Bank and are referable to the Electronic Security Codes, if any, issued to arty Authorised Person or to any use of such Electronic Security Codes by any person, whether authorised or not by the Company or the Authorised Person.
For the purposes of this Letter:
[‘Where possible, this Indemnity and Notice shall be on the letterhead of the Company]
"""

page_search_sent = 'TELEPHONE, ELECTRONIC'
company_pattern = re.compile(r'^Company:\s+(.*)$', re.IGNORECASE)
inst_line_pattern = re.compile(r"^\(([A-H]{1})\).+\((.*)\)", re.IGNORECASE)
inst_pattern = re.compile(r'\((.*?)\)')

if page_search_sent in data:
  for line in data.splitlines():
    inst_line_match = re.search(inst_line_pattern, line)
    company_match = re.findall(company_pattern, line)
    if inst_line_match:
      print(f'Instruction: {re.findall(inst_pattern, line)[1]}')
    elif company_match:
      print(f'Company Name: {company_match[0]}')


# In[3]:


def split_pages(data):
    return list(filter(None, map(
        str.strip, map(str, data.split('\x0c')))))


# In[14]:


dir=r"J:\PQM Share\RDS"
import glob
fpaths=glob.glob(dir+"\*.txt")


# In[15]:


print (fpaths)


# In[16]:


for fpath in fpaths:
    with open(fpath, 'r', encoding='utf8') as infile:
        data = infile.read()
    

