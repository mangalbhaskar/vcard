
## VCARD Parser

* CSV (.csv) to VCARD (.vcf)
* VCARD (.vcf) to CSV (.csv)
* CSV file header should be exactly in the given format:
  ```bash
  last_name,first_name,org,title,phone,email,website,street,city,p_code,country
  ```

## How to

* **How to convert CSV to VCARD file format?**
  ```bash
  python csv2vcard.py --path /path/to/<name>.csv
  ## examples
  python csv2vcard.py --path csv2vcard-sample.csv
  ```
  * This would generate individual contact details `.vcf` files and, also all the contact details in single `.vcf` file in the export directory
* **How to import contact(s) from `.vcf` file(s) to mobile phone**
  * Download the file on the mobile through email, whatspp (preferred)
  * Open the file and import it
  * **CATIOUS - BE CAREFULL!!**
    * On importing the contacts, the duplicate contact details would be deleted


## Requirement

* Requires: `Python >=3.6`


## References

* https://www.w3.org/TR/vcard-rdf/#Mapping
* https://l0b0.wordpress.com/2009/12/25/vcard-parser-and-validator/


## Credits

* Adapted from: https://pypi.org/project/csvTovcf/#description
* Author: Shivam Mani Tripathi
* License: MIT License
