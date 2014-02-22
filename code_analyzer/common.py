import MySQLdb
import os, sys
import yaml

f = open(os.path.join(os.path.dirname(sys.argv[0]),'../config.yaml'))
config = yaml.safe_load(f)
f.close()

try:
    dbConn = MySQLdb.connect( host   = config['database']['host'],
                              user   = config['database']['user'],
                              passwd = config['database']['password'],
                              db     = config['database']['name'] )

except MySQLdb.Error, e:
    print "Error %d: %s" % ( e.args[ 0 ], e.args[ 1 ])
    sys.exit( 1 )

# path to the top of the backup directory, date and time
# directories start right under this.
# BACKUP_TOP = "/home/analyst6/homedirs"
BACKUP_TOP = config['teambackup']['gitdir']

# Static time interval for backups, if it matters, in seconds
BACKUP_INTERVAL = config['teambackup']['interval']
