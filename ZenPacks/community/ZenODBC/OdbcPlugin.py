################################################################################
#
# This program is part of the ZenODBC Zenpack for Zenoss.
# Copyright (C) 2009, 2010, 2011 Egor Puzanov.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""OdbcPlugin

wrapper for PythonPlugin

$Id: OdbcPlugin.py,v 1.8 2011/02/28 16:34:17 egor Exp $"""

__version__ = "$Revision: 1.8 $"[11:-2]

from ZenPacks.community.SQLDataSource.SQLPlugin import SQLPlugin

class OdbcPlugin(SQLPlugin):

    def prepareQueries(self, device):
        queries = self.queries(device)
        for tname, query in queries.iteritems():
            if len(query) == 3:
                cs, sql, columns = query
                kbs = {}
                if type(columns) is not dict:
                    columns = dict(zip(columns, columns))
            else:
                sql, kbs, cs, columns = query 
            queries[tname] = (sql, kbs, "'findodbc','" + cs + "'", columns)
        return queries
