################################################################################
#
# This program is part of the ZenODBC Zenpack for Zenoss.
# Copyright (C) 2009, 2010 Egor Puzanov.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""OdbcPlugin

wrapper for PythonPlugin

$Id: OdbcPlugin.py,v 1.5 2010/08/18 19:16:55 egor Exp $"""

__version__ = "$Revision: 1.5 $"[11:-2]

from Products.DataCollector.plugins.CollectorPlugin import CollectorPlugin
from twisted.python.failure import Failure
from ZenPacks.community.SQLDataSource.SQLClient import SQLClient

class OdbcPlugin(CollectorPlugin):
    """
    A OdbcPlugin defines a native Python collection routine and a parsing
    method to turn the returned data structure into a datamap. A valid
    OdbcPlugin must implement the process method.
    """
    transport = "python"

    tables = {}

    def queries(self, device = None):
        return self.tables


    def collect(self, device, log):
        queries = self.queries(device)
        for tname, query in queries.iteritems():
            if len(query) == 3:
                cs, sql, columns = query
                if type(columns) is not dict:
                    columns = dict(zip(columns, columns))
            else:
                sql, kb, cs, columns = query 
            queries[tname] = (sql, {}, "findodbc, '" + cs + "'", columns)
        return SQLClient(device).query(queries)


    def preprocess(self, results, log):
        newres = {}
        for table, value in results.iteritems():
            if value != []:
                if isinstance(value[0], Failure):
                    log.error(value[0].getErrorMessage())
                    continue
            newres[table] = value
        return newres
