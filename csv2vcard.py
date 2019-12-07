import os
import csv
import codecs


"""
CREDITS: https://pypi.org/project/csvTovcf/#description
Author: Shivam Mani Tripathi
License: MIT License

Adapted by: mangalbhaskar
Requires: Python >=3.6
"""

def check_export():
    """
    Checks if export folder exists in directory
    """
    if not os.path.exists("export"):
        print("Creating /export folder...")
        os.makedirs("export")


def parse_csv(csv_filename: str, csv_delimeter=','):
    """
    Simple csv parser with a ; delimiter
    """
    print("Parsing csv..")
    try:
        with codecs.open(f"{csv_filename}", "r", "utf-8-sig") as f:
            # contacts = csv.reader(f, delimiter=csv_delimeter)
            contacts = csv.reader(f)
            header = next(contacts)  # saves header
            parsed_contacts = [dict(zip(header, row)) for row in contacts]
            return parsed_contacts
    except IOError:
        print(f"I/O error for {csv_filename}")
        return []


def test_csv2vcard():
    """
    Try it out with this mock Forrest Gump contact
    """
    mock_contacts = [{
        "last_name": "Gump", "first_name": "Forrest", "title": "Shrimp Man",
        "org": "Bubba Gump Shrimp Co.",
        "phone": "+49 170 5 25 25 25", "email": "forrestgump@example.com",
        "website": "https://www.linkedin.com/in/forrestgump",
        "street": "42 Plantation St.", "city": "Baytown", "p_code": "30314",
        "country": "United States of America"
    }]
    check_export()
    vcard = create_vcard(mock_contacts[0])
    print(vcard)
    export_vcard(vcard, single_file=False)


def create_vcard(contact: dict):
    """
    The mappings used below are from https://www.w3.org/TR/vcard-rdf/#Mapping
    https://l0b0.wordpress.com/2009/12/25/vcard-parser-and-validator/
    """
    vc_begin = "BEGIN:VCARD\n"
    vc_version = "VERSION:3.0\n"
    vc_name = f"N;CHARSET=UTF-8:{contact['last_name']};{contact['first_name']};;;\n"
    vc_title = f"TITLE;CHARSET=UTF-8:{contact['title']}\n"
    vc_org = f"ORG;CHARSET=UTF-8:{contact['org']}\n"
    vc_phone = f"TEL;TYPE=WORK,VOICE:{contact['phone']}\n"
    vc_email = f"EMAIL;TYPE=WORK:{contact['email']}\n"
    vc_website = f"URL;TYPE=WORK:{contact['website']}\n"
    vc_address = f"ADR;TYPE=WORK;CHARSET=UTF-8:{contact['street']};{contact['city']};{contact['p_code']};{contact['country']}\n"
    vc_end = "END:VCARD\n"

    vc_filename = f"{contact['phone']}-{contact['last_name'].lower()}_{contact['first_name'].lower()}.vcf"
    vc_output = vc_begin + vc_version + vc_name + vc_title + vc_org + vc_phone + vc_email + vc_website + vc_address + vc_end

    vc_final = {
        "filename" : vc_filename,
        "output" : vc_output,
        "name" : contact['first_name'] + contact['last_name'],
    }

    return vc_final


def export_vcard(vc_final, file_name, single_filename):
    """
    Exporting a vCard to /export/
    """
    try:
        with open(file_name, "a") as f:
            f.write(vc_final['output'])
            f.close()
            print(f"Created vCard 3.0 for {vc_final['name']}.")
        with open(single_filename, "a") as f:
            f.write(vc_final['output']+'\n')
            f.close()
    except IOError:
        print(f"I/O error for {vc_final['filename']}")


def csv2vcard(csv_filename: str, csv_delimeter=None):
    """
    Main function
    """
    check_export()

    import datetime
    _timestamp_format_ = "{:%d%m%y_%H%M%S}"
    ts = (_timestamp_format_).format(datetime.datetime.now())
    single_filename = f"export/contacts-{ts}.vcf"

    for c in parse_csv(csv_filename, csv_delimeter):
        vc_final = create_vcard(c)
        print('vc_final:{}'.format(vc_final))
        file_name = f"export/{vc_final['filename']}"
        export_vcard(vc_final, file_name, single_filename)



def parse_args():
  import argparse
  from argparse import RawTextHelpFormatter
  
  ## Parse command line arguments
  parser = argparse.ArgumentParser(
    description='CSV to VCARD (vcf) converter:\n\n',formatter_class=RawTextHelpFormatter)

  parser.add_argument('--path'
    ,dest='path'
    ,metavar="/path/to/<name>.csv"
    ,required=True
    ,help='CSV file required`')

  args = parser.parse_args()

  return args


def main(args):
    path = args.path
    # path = "csv2vcard-sample.csv"
    csv2vcard(path)


if __name__ == '__main__':
    args = parse_args()
    main(args)
