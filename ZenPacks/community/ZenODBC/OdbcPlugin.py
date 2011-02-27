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

$Id: OdbcPlugin.py,v 1.7 2011/02/27 21:07:21 egor Exp $"""

__version__ = "$Revision: 1.7 $"[11:-2]

from Products.DataCollector.plugins.CollectorPlugin import CollectorPlugin
from twisted.python.failure import Failure
from ZenPacks.community.SQLDataSource.SQLClient import SQLClient

class OdbcPlugin(SQLClient):

    def collect(self, device, log):
        queries = self.queries(device)
        for tname, query in queries.iteritems():
            if len(query) == 3:
                cs, sql, columns = query
                if type(columns) is not dict:
                    columns = dict(zip(columns, columns))
            else:
                sql, kb, cs, columns = query 
            queries[tname] = (sql, {}, "'findodbc','" + cs + "'", columns)
        return SQLClient.collect(device, log, queries)
