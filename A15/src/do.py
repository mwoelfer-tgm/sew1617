from behaviour.engines import  *
import argparse


if __name__ == '__main__':
    dic = {"ZIP_STORED" : EngineZipStored,
           "ZIP_LMZA" : EngineZipLMZA,
           "ZIP_BZIP2" : EngineZipBZIP2,
           "ZIP_DEFLATED" : EngineZipDeflated,
           "TAR_GZIP":EngineTarGZIP,
           "TAR_STORED" : EngineTarStored}
    # initialize Argumentparser with fitting description
    parser = argparse.ArgumentParser(description='This program uses various engines for archiving data')
    # add argument"",""s
    parser.add_argument("-d", "--dest-dir", help="Output destination directory (default=Current Working Directory)",
                        default=".")
    parser.add_argument("-s","--source-dir", help="Input root directory (default=Current Working Directory)",
                        default=".")
    parser.add_argument("-a", "--archive-engine", help="use the given archive engine. "
                                                       "Possibilities: ZIP_STORED(default), ZIP_LMZA, "
                                                       "ZIP_BZIP2, ZIP_DEFLATED, TAR_GZIP, TAR_STORED",
                        default="ZIP_STORED")
    parser.add_argument("-n", "--archive-name", help="name of the archive (default=archive)",
                        default="archive.zip")
    # parse arguments
    args = parser.parse_args()
    # initialize client with parameters
    engine = dic[args.archive_engine](args.archive_name,args.dest_dir)
    engine.write()