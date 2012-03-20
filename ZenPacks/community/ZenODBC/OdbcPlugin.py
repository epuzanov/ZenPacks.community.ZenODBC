################################################################################
#
# This program is part of the ZenODBC Zenpack for Zenoss.
# Copyright (C) 2009-2012 Egor Puzanov.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""OdbcPlugin

wrapper for PythonPlugin

$Id: OdbcPlugin.py,v 2.1 2012/03/20 20:22:48 egor Exp $"""

__version__ = "$Revision: 2.1 $"[11:-2]

from ZenPacks.community.SQLDataSource.SQLPlugin import SQLPlugin

class OdbcPlugin(SQLPlugin):

    def prepareQueries(self, device):
        queries = self.queries(device)
        for tname, query in queries.iteritems():
            if len(query) == 3:
                cs, sql, columns = query
                kbs = {}
                if type(columns) is dict:
                    columns = dict(zip(columns.values(), columns.keys()))
                else:
                    columns = dict(zip(columns, columns))
            else:
                sql, kbs, cs, columns = query 
            queries[tname] = (sql, kbs, "'pyisqldb','" + cs + "'", columns)
        return queries
