# GrampsBuiltinsReworked
Builtin Plugins recast as addons for experimentation. This allows faster turnaround for evolving plug-ins in the Core Gramps repository. Updates can be released more frequently than the limited enhancement release schedule of Gramps. These are intended to be temporary. To be deleted when merged back into the core plug-ins.

1) **Kinship Report** : adding Gramps PersonID in response to [Adding data in kinship-report](https://gramps.discourse.group/t/adding-data-in-kinship-report/5287) thread on Discourse. <br />added 24 Apr 2024 with [PR 1709](https://github.com/gramps-project/gramps/pull/1709) Add Gramps ID option to Kinship Report. Merged to Gramps 6.0 on 2 Jan 2025.<br />
Still outstanding: the way to add parents (or spouse, where appropriate) descriptive phrases.

2) **GEDCOM dialect** : experiments to change the format of Notes generated for unrecognized tags. In response to [Converting Reunion for Mac to Gramps for Mac](https://gramps.discourse.group/t/converting-reunion-for-mac-to-gramps-for-mac/7585/) thread on Discourse that had an incorrect tag in citations. Needed the failure Note to have less extraneous formatting.
