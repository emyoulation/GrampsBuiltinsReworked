# encoding:utf-8
#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2009 Benny Malengier
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
from gramps.gen.plug._pluginreg import *
from gramps.gen.const import GRAMPS_LOCALE as glocale
from gramps.version import major_version, VERSION_TUPLE

_ = glocale.translation.gettext

# this is the default in gen/plug/_pluginreg.py: plg.require_active = True
#         if VERSION_TUPLE >= (5, 2, 0):
#             helpt_url = "Gramps_5.2_Wiki_Manual_-_Reports_-_part_6#Kinship_Report"

# ------------------------------------------------------------------------
#
# Kinship Report
#
# ------------------------------------------------------------------------
register(REPORT,
         id = "kinship_report2",
         name = _("Kinship Report2"),
         description = _("Produces a textual report of kinship for a given person"),
         version = "1.1",
         gramps_target_version = major_version,
         status = STABLE,
         fname = "kinshipreport2.py",
         authors = ["Brian G. Matherly"],
         authors_email = ["brian@gramps-project.org"],
         category = CATEGORY_TEXT,
         reportclass = "KinshipReport",
         optionclass = "KinshipOptions",
         report_modes = [REPORT_MODE_GUI, REPORT_MODE_BKI, REPORT_MODE_CLI],
         )
