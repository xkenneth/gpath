try:
    import os
    print "Using Python."
    join = os.path.join
    isdir = os.path.isdir
    isfile = os.path.isfile
except ImportError:
    pass

try: 
    from System.IO import Path, Directory, File
    print "Using .net"
    join = Path.Combine
    isdir = Directory.Exists
    isfile = File.Exists
    
except ImportError:
    pass
