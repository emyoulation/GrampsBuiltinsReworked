Kinship Report

Based on the [built-in Kinship report](https://www.gramps-project.org/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Kinship_Report).

19 Apr 2024, a user on Discourse asked about [Adding data in kinship report](https://gramps.discourse.group/t/adding-data-in-kinship-report/5287). 

In particular, they wanted inclusion of the GrampsID to be a a configuration option. That was easily added and [PR 1709](https://github.com/gramps-project/gramps/pull/1709) was proposed for the 5.2 maintenance branch. Re-based for 6.0 and released.

![Kinship1](https://github.com/user-attachments/assets/6465ef6a-bfed-4895-a650-e4fc2ff0e3b1)

The second part was to add the appropriate relationship description for each section:
* Spouse sections, add "; married X on &lt;date> in &lt;place>"
* Children/granchildren section, add "; son/daughter of Y and Z"

Similar to the the [Biography quickview](https://github.com/gramps-project/addons-source/blob/maintenance/gramps60/BiographyQuickview/BiographyQuickview.py)
![image](https://github.com/user-attachments/assets/cc76adae-e0d1-4a46-b52b-91710aba0c5f)
