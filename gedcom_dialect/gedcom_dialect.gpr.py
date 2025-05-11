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
from gramps.gen.plug._pluginreg import newplugin, STABLE, IMPORT
from gramps.gen.const import GRAMPS_LOCALE as glocale
from gramps.version import major_version, VERSION_TUPLE

_ = glocale.translation.gettext

# ------------------------------------------------------------------------
#
# GEDCOM dialect
#
# ------------------------------------------------------------------------
help_url = (
    "https://gramps-project.org/wiki/index.php/Addon:Isotammi_addons#FilterParams_tool"
)


if VERSION_TUPLE < (5, 2, 0):
    additional_args = {
        "status" : STABLE,}
else:
    additional_args = {
        "status" : EXPERIMENTAL,
        "audience": EXPERT,
        "help_url": help_url,
    }

register(
    IMPORT,
    id="im_gedd",
    name=_("GEDCOM_dialect"),
    description = _(
    "GEDCOM dialect is used to transfer data between genealogy programs. "
    "Most genealogy software will accept a GEDCOM file as input."
    ),
    version="1.0.1",
    gramps_target_version=major_version,
    fname="gedcom_dialect.py",
    import_function="importData",
    extension="ged",
    **additional_args,
)