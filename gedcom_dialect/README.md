GEDCOM dialect

GEDCOM dialect : experiments to change the format of Notes generated for unrecognized tags. In response to "[Converting Reunion for Mac to Gramps for Mac](https://gramps.discourse.group/t/converting-reunion-for-mac-to-gramps-for-mac/7585/)" thread on Discourse that had an incorrect tag in citations. Needed the failure Note to have less extraneous formatting.

With a note that is SO different from the tag data, it is too difficult to build test post-processing scripts that easily convey to the experimental version of the import plugin.  So the first step to expanding the plugin is preserving parsable original data. 

[Outstanding problems reported for the Gramps 5.5.1 import](https://www.gedcomassessment.com/en/assessment-gramps-5.htm):

* IDNO (ID Number)
* Change Date
* Date Sort
* FROM dates
* TO dates
* INT dates; with or without "(Phrase)" .. deduced or inferred from other information with the evidence/reasoning as the "phrase"
* Event Primaary
* Event Shared: SHAR Role, ASSO Rela
* BIRT/DEAT/CENS with TYPE
* Master Place
* Name with Comma Suffix
* Place ADDR label and fields
* Repository
* Restriction
* Source

## See also
* [Gramps and GEDCOM](https://www.gramps-project.org/wiki/index.php/Gramps_and_GEDCOM)

