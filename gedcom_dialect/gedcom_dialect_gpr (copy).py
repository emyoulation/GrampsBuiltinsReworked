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

_ = glocale.translation.gettext

MODULE_VERSION = "5.2"

# ------------------------------------------------------------------------
#
# GEDCOM
#
# ------------------------------------------------------------------------

plg = newplugin()
plg.id = "im_gedd"
plg.name = _("GEDCOMdialect")
plg.description = _(
    "GEDCOM dialect is used to transfer data between genealogy programs. "
    "Most genealogy software will accept a GEDCOM file as input."
)
plg.version = "0.1"
plg.gramps_target_version = MODULE_VERSION
plg.status = STABLE
plg.fname = "GEDCOMdialect.py"
plg.ptype = IMPORT
plg.import_function = "importData"
plg.extension = "ged"
