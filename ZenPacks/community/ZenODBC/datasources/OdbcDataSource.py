################################################################################
#
# This program is part of the ZenODBC Zenpack for Zenoss.
# Copyright (C) 2009, 2010, 2011 Egor Puzanov.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""OdbcDataSource

Defines attributes for how a datasource will be graphed
and builds the nessesary DEF and CDEF statements for it.

$Id: OdbcDataSource.py,v 2.0 2011/05/03 22:21:05 egor Exp $"""

__version__ = "$Revision: 2.0 $"[11:-2]

from ZenPacks.community.SQLDataSource.datasources import SQLDataSource

class OdbcDataSource(SQLDataSource.SQLDataSource):

    ZENPACKID = 'ZenPacks.community.ZenODBC'

    sourcetypes = ('ODBC',)
    sourcetype = 'ODBC'

    def getConnectionString(self, context):
        return "'pyisqldb','%s'"%self.getCommand(context, self.cs)
