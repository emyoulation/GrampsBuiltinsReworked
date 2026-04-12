# GrampsBuiltinsReworked
Builtin Plugins recast as addons for experimentation. This allows faster turnaround for evolving plug-ins in the Core Gramps repository. Updates can be released more frequently than the limited enhancement release schedule of Gramps. These are intended to be temporary. To be deleted when merged back into the core plug-ins.

1) **Kinship Report** : adding Gramps PersonID in response to [Adding data in kinship-report](https://gramps.discourse.group/t/adding-data-in-kinship-report/5287) thread on Discourse. <br />added 24 Apr 2024 with [PR 1709](https://github.com/gramps-project/gramps/pull/1709) Add Gramps ID option to Kinship Report. Merged to Gramps 6.0 on 2 Jan 2025.<br />
Still outstanding: the way to add parents (or spouse, where appropriate) descriptive phrases.

2) **GEDCOM dialect** : experiments to change the format of Notes generated for unrecognized tags. In response to [Converting Reunion for Mac to Gramps for Mac](https://gramps.discourse.group/t/converting-reunion-for-mac-to-gramps-for-mac/7585/) thread on Discourse that had an incorrect tag in citations. Needed the failure Note to have less extraneous formatting.

3) **eventnames.py** : The "Tools > Family Tree > Extract event description" originally populated blank Event descriptions. (Extracted from the Event type and the Main Participant names.) Claude AI generated option to remove descriptions.
In response to:
* [Gramps Finland Google Group](https://groups.google.com/g/gramps-finland/c/sFPVLpegjt4): Kuvaus-kenttien (syntymä, kuolema, avioliitto etc.) muokkaaminen (translation: Editing description fields (birth, death, marriage, etc.)
* [5401](https://gramps-project.org/bugs/view.php?id=5401): Tools>Family Tree Processing>Extract Event Description - does not extract - it ADDS
* [1658](https://gramps-project.org/bugs/view.php?id=1658): Different name formats after running "Extract event descriptions from event data".
* [8626](https://gramps-project.org/bugs/view.php?id=8626): "Extract Event Description" tool needs improvements
   
