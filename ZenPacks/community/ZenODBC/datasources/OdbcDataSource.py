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

$Id: OdbcDataSource.py,v 1.5 2011/01/19 00:02:24 egor Exp $"""

__version__ = "$Revision: 1.5 $"[11:-2]

from ZenPacks.community.SQLDataSource.datasources import SQLDataSource

class OdbcDataSource(SQLDataSource.SQLDataSource):

    ZENPACKID = 'ZenPacks.community.ZenODBC'

    sourcetypes = ('ODBC',)
    sourcetype = 'ODBC'


    # Screen action bindings (and tab definitions)
    factory_type_information = ( 
    { 
        'immediate_view' : 'editODBCDataSource',
        'actions'        :
        ( 
            { 'id'            : 'edit'
            , 'name'          : 'Data Source'
            , 'action'        : 'editODBCDataSource'
            , 'permissions'   : ( 'View', )
            },
        )
    },
    )


    def getConnectionString(self, context):
        return "'findodbc','%s'"%self.getCommand(context, self.cs)
