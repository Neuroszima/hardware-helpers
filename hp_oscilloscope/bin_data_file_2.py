# to fix: prepare a simple reader-writer for binary format and convert this file into binary
bin_data = (b'#800004000\x85\x92\x8e\x86\x81\x80\x80\x81\x8c\x83\x83\x8a\x96\x96\x95\x96\x8f\x95\x94\x8f\x82'
            b'\x89\x88\x82\x8b\x84\x83\x88\x96\x90\x90\x96\x95\x96\x96\x92\x88\x8e\x8d\x89\x86\x85\x85\x88'
            b'\x90\x8b\x89\x8e\x95\x95\x94\x93\x8d\x8f\x94\x8a\x83\x85\x85\x84\x87\x85\x85\x8b\x91\x8e\x90'
            b'\x91\x8a\x91\x92\x8c\x84\x87\x87\x84\x85\x83\x84\x85\x8e\x8a\x8b\x90\x90\x91\x91\x90\x8a\x8d'
            b'\x8d\x88\x84\x85\x86\x85\x8c\x89\x88\x8a\x8f\x8e\x8fYYYYYYYYYWYXX\x94\x96\x99\x94\x97\x93\x95'
            b'\x96\x94\x94\x94\x94\x95\x95\x95\x96\x97\x96\x96\x97\x98\x97\x97\x98\x99\x99\x99\x99\x99\x99'
            b'\x99\x9b\x99\x99\x99\x99\x99\x99\x9a\x99\x97\x98\x99\x98\x97\x98\x98\x97\x96\x96\x97\x94\x95'
            b'\x95\x95\x95\x8c\x94\x94\x8e\x80\x88\x88\x7f~||\x7f\x8d\x81\x84\x8b\x91\x91\x91\x92\x86\x8f'
            b'\x8c\x88\x80\x82\x81\x81\x87\x7f\x7f\x87\x8f\x8d\x90\x93\x90\x94\x90\x8f\x85\x88\x84\x85\x86'
            b'\x85\x81\x85\x90\x88\x8a\x91\x92\x93\x93\x8f\x87\x8e\x8a\x86\x81\x82\x80\x81\x87\x85\x85\x8b'
            b'\x90\x8e\x8e\x90\x8a\x8e\x8e\x8b\x83\x86\x85\x82\x85\x82\x83\x86\x8f\x8a\x8a\x8e\x8d\x90\x90'
            b'\x8e\x87\x89\x8a\x85\x85\x84\x84\x84\x8d\x88\x8b\x8dk\x8f\x91YZYZZZZ[Y\\YY\x99\x95\x96\x96\x95'
            b'\x94\x95\x95\x95\x95\x95\x96\x95\x96\x96\x97\x98\x98\x97\x97\x97\x9d\x99\x99\x99\x99\x99\x99'
            b'\x99\x9b\x9b\x9b\x9b\x99\x9b\x9b\x9b\x9b\x9b\x9b\x9a\x98\x99\x99\x99\x98\x99\x99\x99\x98\x97'
            b'\x99\x96\x97\x96\x97\x97\x91\x94\x93\x91\x7f\x88\x8a\x7f\x80{|\x80\x94\x86\x89\x8d\x95\x90\x93'
            b'\x95\x8a\x8e\x8e\x89\x81\x85\x83\x81\x8a\x81\x86\x88\x95\x93\x92\x95\x90\x96\x95\x8c\x85\x88\x8b'
            b'\x86\x89\x85\x85\x88\x94\x8d\x90\x94\x93\x95\x95\x93\x85\x8e\x8d\x8a\x84\x84\x84\x84\x8e\x86\x87'
            b'\x8e\x91\x8f\x90\x91\x8a\x8e\x8f\x88\x83\x84\x86\x83\x8a\x84\x85\x8d\x90\x8d\x8d\x91\x8e\x90\x90'
            b'\x8e\x85\x88\x8a\x86\x86\x84\x84\x85\x8c\x88\x8a\x8eYWYYYYXYXXYW\x93Y\x7f\x94\x93\x93\x93\x93'
            b'\x93\x93\x93\x93\x93\x93\x93\x93\x95\x94\x94\x94\x96\x95\x95\x96\x97\x96\x97\x97\x97\x97\x97'
            b'\x97\x98\x98\x97\x97\x98\x97\x97\x97\x96\x96\x97\x96\x94\x95\x97\x95\x94\x94\x94\x94\x92\x93'
            b'\x93\x92\x8f\x91\x92\x8f\x84\x8c\x8a\x82z{zz\x83|\x80\x84\x90\x8c\x8a\x90\x8b\x8f\x90\x88|'
            b'\x86\x84~\x7f}}\x82\x8e\x89\x84\x8e\x8d\x8f\x91\x90\x83\x89\x8a\x80\x7f\x80\x81\x80\x88\x83'
            b'\x81\x88\x8d\x8a\x8e\x8f\x88\x8b\x89\x89|\x80\x84{\x80\x81\x7f\x85\x8d\x89\x86\x8c\x89\x8b'
            b'\x8c\x87\x80\x87\x88\x80\x80~~\x80\x8a\x83\x84\x88\x8b\x8c\x8c\x8a\x85\x88\x88\x85\x81\x80'
            b'\x82\x81\x84\x82\x84\x87V\x8b\x8bWVVVVUUVU\x95UU\x96\x91\x92\x92\x91\x91\x91\x91\x91\x92'
            b'\x91\x91\x92\x94\x93\x93\x94\x95\x94\x94\x95\x95\x95\x95\x95\x96\x96\x96\x96\x96\x97\x97'
            b'\x97\x96\x97\x96\x96\x95\x96\x96\x95\x94\x95\x94\x94\x93\x93\x92\x92\x91\x92\x92\x91\x90'
            b'\x90\x90\x90\x8b\x8e\x8e\x85y\x81~y~xx\x7f\x8a\x86\x85\x8d\x8b\x8e\x8e\x8e\x82\x85'
            b'\x86~{{{}\x87\x80\x80\x86\x90\x8f\x8f\x91\x8a\x8e\x8e\x88~\x82\x81\x80\x86\x80\x81'
            b'\x84\x90\x8a\x8a\x90\x8d\x8f\x91\x8e\x81\x8a\x88\x82\x82\x80\x80\x83\x8b\x87\x87\x8d\x8e\x8f'
            b'\x8f\x8f\x89\x8b\x8b\x86\x81\x81\x81\x81\x85\x85\x85\x88\x90\x8e\x8e\x91\x8e\x90\x8e\x8e\x86'
            b'\x87\x8a\x86\x8b\x86\x85\x8a\x8b\x8e\x8et[Z[\\[\\\\[[[[\x81\x97\x97\x9c\x99\x97\x98\x97\x96'
            b'\x97\x97\x97\x97\x98\x98\x98\x98\x99\x99\x99\x99\x9b\x99\x9b\x9b\x9d\x9c\x9c\x9c\x9c\x9d\x9d'
            b'\x9c\x9d\x9e\x9d\x9d\x9d\x9d\x9e\x9d\x9c\x9d\x9c\x9c\x9c\x9c\x9c\x9c\x9a\x9b\x9c\x9c\x99\x99'
            b'\x99\x99\x97\x98\x99\x94\x86\x8e\x8e\x8b\x84\x81\x81\x83\x91\x88\x87\x91\x98\x95\x97\x98\x8d'
            b'\x94\x95\x8b\x85\x8a\x88\x86\x8d\x86\x87\x8d\x9a\x97\x93\x99\x95\x99\x98\x93\x8a\x8e\x91\x8b'
            b'\x8a\x89\x89\x8a\x97\x90\x90\x95\x98\x99\x98\x98\x8e\x95\x92\x8d\x87\x87\x88\x88\x8e\x8c\x87'
            b'\x8e\x95\x95\x95\x95\x90\x93\x94\x91\x87\x8c\x8a\x87\x8b\x8a\x88\x8a\x94\x92\x91\x95\x93\x95'
            b'\x95\x93\x8a\x90\x8e\x8a\x8a\x89\x89\x8a\x92\x8c\x8c\x91]]]^^]^][^][\x99\x9a\x97\x99\x98\x97'
            b'\x98\x98\x98\x97\x9b\x99\x98\x99\x98\x99\x9d\x9b\x9b\x9b\x9c\x9b\x9c\x9c\x9c\x9c\x9c\x9d\x9d'
            b'\x9d\x9e\x9d\x9d\x9d\x9e\x9d\x9c\x9c\x9c\x9c\x9c\x9c\x9c\x9b\x9b\x9b\x9b\x99\x98\x99\x99\x99'
            b'\x98\x98\x97\x98\x97\x97\x97\x94\x86\x8d\x8d\x89\x80\x85\x80\x7f\x8a\x82\x85\x8b\x95\x92\x92'
            b'\x96\x8c\x92\x91\x8e\x83\x85\x88\x81\x87\x81\x81\x88\x93\x8b\x8e\x95\x94\x97\x96\x95\x8a\x90'
            b'\x8c\x88\x84\x83\x84\x85\x90\x89\x8c\x8f\x94\x93\x93\x93\x8a\x92\x91\x8d\x83\x85\x84\x83\x8d'
            b'\x84\x85\x86\x91\x8e\x8f\x92\x8e\x91\x92\x8c\x85\x88\x8b\x84\x87\x85\x85\x85\x8e\x8d\x89\x8f'
            b'\x91\x92\x91\x91\x88\x8d\x8d\x88\x86\x86\x86\x86Y\x87\x89sZ[[ZYZZZaZYY\x94\x97\x97\x94\x94\x94'
            b'\x93\x93\x94\x93\x94\x95\x94\x95\x94\x95\x96\x95\x95\x96\x97\x96\x96\x97\x98\x97\x99\x98\x99'
            b'\x98\x99\x99\x98\x99\x98\x99\x98\x98\x99\x98\x97\x98\x97\x97\x97\x97\x97\x96\x98\x93\x94\x94'
            b'\x90\x94\x94\x94\x87\x93\x95\x8e\x81\x8b\x89\x83\x7f||}\x8e\x83\x85\x8b\x93\x93\x90\x93\x8d'
            b'\x8f\x8e\x87\x81\x84\x86\x81\x8d\x81\x83\x89\x97\x91\x8e\x95\x93\x96\x96\x93\x86\x8d\x8e\x88'
            b'\x89\x86\x86\x88\x94\x8c\x90\x93\x97\x96\x96\x93\x8d\x93\x90\x8c\x86\x86\x86\x86\x8e\x89\x8a'
            b'\x8c\x99\x91\x93\x92\x91\x93\x94\x8e\x87\x8d\x8a\x87\x8a\x87\x88\x8a\x94\x8f\x92\x95\x94\x95'
            b'\x95\x94\x8c\x92\x91\x8d\x8b\x8b\x8a\x8b_~\x8e_^_``^`_^\x9cdm\x9f\x9a\x9b\x9b\x99\x99\x99\x9a'
            b'\x98\x9b\x99\x99\x9b\x9c\x9b\x9b\x9c\x9d\x9c\x9c\x9d\x9e\x9e\x9e\x9f\x9f\x9e\x9f\x9f\x9f\xa1'
            b'\x9f\x9f\xa0\xa0\xa0\xa1\x9e\xa4\x9e\x9e\x9f\x9f\x9c\x9e\x9c\x9c\x9d\x9c\x9b\x9c\x9c\x9c\x9a'
            b'\x9b\x9a\x98\x90\x98\x98\x8f\x83\x8a\x88\x82\x89\x81\x83\x89\x98\x91\x8e\x95\x97\x98\x99\x94'
            b'\x88\x8b\x8d\x86\x85\x84\x84\x84\x93\x8a\x8e\x91\x97\x98\x94\x97\x8e\x94\x95\x8f\x87\x8a\x89'
            b'\x86\x8f\x87\x88\x8f\x96\x92\x97\x96\x90\x96\x96\x92\x87\x8b\x8b\x87\x86\x86\x86\x89\x91\x8d'
            b'\x8d\x90\x93\x94\x93\x93\x88\x8e\x8e\x87\x85\x85\x85\x86\x8d\x88\x88\x8d\x93\x91\x91\x92\x89'
            b'\x91\x91\x8e\x86\x89\x88\x86[\x86\x86\\ZZ[[ZYYYkYYy\x94\x96\x98\x95\x93\x93\x94\x93\x94\x94'
            b'\x94\x94\x95\x94\x95\x95\x95\x95\x95\x98\x97\x95\x96\x97\x98\x97\x98\x97\x97\x98\x98\x97\x97'
            b'\x97\x97\x97\x96\x96\x97\x97\x95\x95\x96\x95\x94\x94\x94\x95\x92\x93\x93\x92\x91\x92\x92\x91'
            b'\x8f\x90\x91\x8e|\x88\x84|yyy|\x8a\x80\x80\x8a\x92\x8e\x8e\x8f\x87\x8d\x8d\x7f{~\x81}\x85\x80~'
            b'\x83\x8f\x8e\x88\x91\x8d\x91\x90\x8e\x82\x86\x87\x80\x80\x80\x80\x80\x8d\x88\x88\x8b\x90\x90\x8f'
            b'\x8d\x84\x88\x88\x83\x7f\x80\x80\x80\x86\x83\x80\x87\x8d\x8a\x8d\x8d\x89\x8b\x89\x87\x7f\x82\x81'
            b'\x80\x82\x80\x7f\x81\x8c\x85\x89\x8c\x8a\x8c\x8c\x8a\x80\x85\x87\x7f\x82\x80\x80\x80TTVUUTUUTTUT'
            b'\x90\x98\x91\x91\x90\x8f\x8f\x90\x90\x8f\x90\x90\x91\x91\x91\x91\x92\x91\x93\x93\x93\x93\x93\x94'
            b'\x95\x95\x95\x96\x97\x97\x96\x97\x97\x96\x97\x97\x96\x97\x97\x97\x96\x97\x96\x96\x95\x96\x96\x96'
            b'\x94\x95\x95\x95\x94\x94\x94\x94\x90\x93\x94\x91\x82\x8d\x8b\x84~}~~\x88\x81\x81\x88\x93\x8f\x90'
            b'\x94\x8b\x91\x93\x8a\x81\x85\x86\x81\x88\x83\x83\x85\x96\x8b\x8d\x94\x95\x96\x97\x93\x8a\x93\x8e'
            b'\x8c\x88\x86\x87\x87\x93\x8d\x8e\x90\x95\x96\x96\x97\x8d\x93\x93\x90\x88\x8a\x8a\x87\x8c\x8d\x86'
            b'\x8d\x95\x91\x91\x97\x93\x96\x95\x92\x8a\x8d\x8c\x8b\x8a\x88\x88\x88\x91\x8e\x8e\x93\x95\x96\x96'
            b'\x95\x8e\x93\x93\x8e\x8a\x8a\x8a\x88```````^^]`]\x9c\x9b\xa1\x9b\x99\x9b\x99\x99\x9a\x99\x9b\x9a'
            b'\x9c\x9b\x9a\x9b\x9c\x9b\x9c\x9c\x9e\x9d\x9d\x9e\x9f\x9d\x9e\x9e\xa0\xa0\x9f\xa0\xa0\x9f\x9f\x9f'
            b'\xa0\xa0\xa1\x9e\x9d\x9c\x9e\x9d\x9c\x9d\x9d\x9c\x9b\x9c\x9c\x9b\x99\x99\x9a\x99\x97\x99\x99\x95'
            b'\x88\x93\x91\x87\x80\x80\x82\x80\x89\x85\x86\x89\x96\x92\x95\x96\x91\x95\x97\x8e\x81\x87\x88\x83'
            b'\x8a\x82\x82\x88\x94\x8e\x8f\x95\x95\x96\x97\x95\x87\x92\x8e\x89\x84\x86\x85\x85\x91\x88\x8a\x8f'
            b'\x94\x93\x94\x95\x8e\x90\x90\x8d\x84\x87\x88\x85\x88\x83\x84\x87\x91\x8c\x8e\x90\x8c\x92\x8e\x8f'
            b'\x85\x88\x86\x84\x84\x82\x82\x84\x8d\x88\x88\x8c\x8f\x8f\x8f\x8e\x8a\x8d\x8b\x86\x83\x83\x84\x81'
            b'W[WWUVXYVTWT\x92\x96\x95\x94\x90\x92\x93\x92\x91\x91\x91\x92\x93\x92\x92\x92\x93\x94\x94\x94\x95'
            b'\x95\x95\x95\x97\x95\x96\x96\x97\x96\x98\x97\x97\x97\x97\x97\x97\x97\x97\x97\x96\x97\x97\x97\x96'
            b'\x96\x96\x95\x94\x94\x94\x94\x93\x93\x93\x93\x91\x92\x93\x91\x80\x87\x8a\x85{}~{\x85\x80\x80\x8a'
            b'\x91\x90\x8e\x91\x8b\x8e\x8f\x8c|\x84\x86\x7f\x83~\x7f\x82\x8f\x8b\x8a\x91\x92\x93\x93\x91\x84\x8b'
            b'\x88\x86\x81\x81\x82\x82\x8a\x84\x88\x8e\x91\x91\x91\x92\x88\x8c\x8e\x87\x81\x83\x82\x81\x84\x81'
            b'\x83\x88\x8e\x8a\x8d\x8e\x8a\x8e\x8e\x8a\x81\x86\x86\x84\x80\x80\x82\x83\x8c\x88\x85\x8d\x8e\x8f'
            b'\x8e\x8e\x86\x8a\x8b\x88\x84\x85\x84ZXXYXYYYYYYXX\x95\x96\x97\x95\x95\x95\x94\x94\x96\x94\x94\x96'
            b'\x96\x96\x95\x97\x98\x97\x98\x98\x98\x99\x99\x99\x9c\x9b\x9b\x9b\x9d\x9b\x9b\x99\x9b\x9c\x9c\x9c'
            b'\xa0\x9b\x9c\x9c\x9c\x9b\x9b\x9b\x9e\x9b\x99\x9c\x9a\x99\x9a\x99\x99\x99\x99\x99\x98\x98\x99\x97'
            b'\x85\x8e\x8c\x85\x81\x82\x82\x81\x90\x86\x86\x8e\x98\x98\x96\x99\x90\x96\x98\x92\x86\x88\x88\x86'
            b'\x8d\x86\x87\x91\x99\x96\x91\x98\x97\x9b\x9b\x97\x8a\x8f\x91\x8d\x8c\x8a\x8a\x8e\x96\x91\x91\x97'
            b'\x9a\x9a\x9b\x99\x93\x99\x97\x90\x8a\x8d\x8d\x8a\x91\x8b\x8b\x91\x99\x92\x95\x98\x93\x98\x97\x94'
            b'\x8b\x8f\x8e\x8a\x8e\x8a\x8b\x8b\x96\x91\x91\x96\x97\x97\x97\x95\x8d\x91\x93\x8f\x8a\x8b\x8b\x8c'
            b'``c`_``__bcx\x99\x9a\x9c\x99\x99\x99\x99\x99\x9b\x99\x99\x9b\x99\x99\x99\x9b\x9c\x98\x9a\x9b\x9c'
            b'\x99\x9d\x9c\x9b\x9c\x9c\x9d\x9c\x9c\x9d\x9c\x9d\x9d\x9d\x9d\x9c\x9c\x9d\xa1\x9b\x9c\x9c\x9b\x9a'
            b'\x9b\x9b\x9a\x99\x99\x99\x99\x97\x98\x98\x98\x93\x97\x97\x92\x85\x8c\x8e\x83\x80\x80\x80\x80\x8a'
            b'\x84\x86\x8d\x95\x93\x93\x96\x8e\x93\x94\x8c\x81\x83\x85\x82\x87\x82\x82\x89\x94\x8e\x8d\x94\x90'
            b'\x96\x96\x8f\x85\x8a\x88\x85\x84\x84\x83\x86\x90\x8d\x8c\x92\x92\x93\x93\x91\x89\x8e\x89\x87\x82'
            b'\x83\x84\x81\x89\x85\x82\x87\x8f\x8e\x8f\x90\x8a\x8e\x8f\x88\x82\x85\x86\x81\x85\x81\x82\x85\x8d'
            b'\x88\x8a\x8e\x8e\x8f\x8f\x8d\x86\x8a\x8b\x87X\x83\x84^YXXXXXYXkYX\x94\x93\x94\x95\x93\x93\x93\x93'
            b'\x93\x93\x93\x91\x94\x94\x94\x94\x95\x97\x95\x95\x95\x97\x96\x97\x97\x98\x98\x97\x98\x99\x99\x99'
            b'\x99\x99\x99\x99\x99\x98\x99\x99\x98\x98\x99\x98\x98\x97\x98\x98\x97\x96\x96\x97\x96\x95\x97\x96'
            b'\x95\x91\x94\x93\x8f\x7f\x82\x87|~}}\x7f\x91\x89\x8a\x8b\x94\x95\x95\x94\x85\x8d\x8a\x86\x80\x81'
            b'\x82\x80\x88\x82\x82\x8c\x94\x92\x93\x95\x8e\x94\x95\x90\x83\x8a\x87\x84\x87\x81\x84\x84\x8f\x8d'
            b'\x8e\x91\x91\x93\x94\x91\x88\x8a\x8d\x88\x84\x83\x83\x82\x8a\x86\x88\x8c\x92\x90\x91\x91\x8d\x8d'
            b'\x90\x8c\x84\x86\x85\x86\x87\x85\x84\x8c\x91\x8c\x8d\x92\x8f\x93\x92\x8e\x88\x8c\x8b\x88]\x87'
            b'\x87]\\\\\\\\\\\\\\[]\\\\\x9d\x98\x99\x99\x98\x98\x98\x98\x99\x99\x99\x99\x98\x9a\x99\x99\x9a'
            b'\x9b\x9b\x9b\x9c\x9d\x9c\x9c\x9c\x9d\x9d\x9e\x9e\x9e\x9e\x9e\x9e\x9e\x9d\x9f\x9e\x9e\x9e\x9e\x9f'
            b'\x9d\x9e\x9e\x9c\x9c\x9d\x9c\x9c\x9b\x9c\x9c\x9c\x9a\x9b\x9b\x9a\x95\x99\x99\x92\x86\x8f\x8f\x85'
            b'\x88\x83\x82\x87\x94\x8d\x8e\x91\x99\x98\x99\x99\x90\x95\x92\x8e\x86\x88\x87\x87\x8f\x8a\x8d\x8d'
            b'\x99\x97\x94\x9b\x95\x99\x99\x91\x89\x8c\x90\x8a\x8b\x89\x89\x8e\x97\x93\x95\x97\x93\x99\x99\x98'
            b'\x88\x8e\x95\x8a\x89\x8a\x88\x89\x93\x8d\x8d\x8b\x97\x95\x97\x94\x8d\x94\x92\x8e\x87\x8a\x8a\x8a'
            b'\x8e\x88\x88\x8d\x95\x91\x91\x95\x91\x95\x95\x91\x8a\x8d\x8e\x8a\x89\x88\x88\\]]^]]]]]g\\\\\x8a\x99'
            b'\x99\x99\x99\x97\x97\x97\x97\x98\x97\x97\x97\x99\x98\x98\x99\x99\x99\x99\x99\x9a\x9a\x99\x9a\x9c\x9a'
            b'\x9c\x9b\x9c\x9b\x9c\x9c\x9b\x9b\x9b\x9c\x9a\x9b\x9b\x99\x99\x9b\x9c\x99\x98\x99\x99\x99\x98\x98\x98'
            b'\x98\x96\x97\x96\x96\x91\x96\x95\x91\x84\x8c\x8e\x83~~~~\x8d\x87\x87\x8e\x94\x92\x92\x92\x8a\x91\x8f'
            b'\x8a\x7f\x81\x80\x80\x85\x80\x80\x88\x93\x90\x91\x93\x90\x93\x94\x92\x82\x8a\x8a\x85\x84\x84\x81\x83'
            b'\x8e\x88\x89\x8e\x92\x92\x92\x91\x88\x8e\x8f\x87\x81\x85\x80\x81\x87\x84\x83\x88\x90\x8c\x8e\x8f\x88'
            b'\x8d\x8d\x88\x83\x85\x84\x82\x85\x82\x82\x84\x8e\x8a\x88\x8e\x8e\x8f\x8e\x91\x85\x8b\x8b\x86\x85\x84'
            b'\x85\x84ZYn[YYZYYYYY\x97\x98\x84\x97\x94\x94\x95\x94\x97\x95\x95\x95\x96\x95\x95\x95\x97\x96\x96\x97'
            b'\x99\x99\x97\x99\x99\x99\x99\x9a\x9b\x99\x99\x9b\x9b\x9a\x9a\x9b\x9a\x9a\x9b\x9b\x99\x9a\x9a\x99\x99'
            b'\x99\x99\x98\x98\x98\x99\x98\x97\x97\x97\x99\x96\x96\x96\x95\x86\x91\x93\x89~\x83\x81~\x85\x81\x7f'
            b'\x88\x94\x90\x8d\x93\x8f\x95\x95\x93\x86\x87\x8c\x84\x82\x81\x81\x85\x94\x87\x8a\x8e\x96\x95\x96\x94'
            b'\x8a\x8e\x8e\x89\x84\x86\x87\x84\x8c\x85\x89\x8a\x95\x92\x92\x95\x8b\x92\x94\x8d\x84\x8a\x8a\x84\x8a'
            b'\x85\x84\x87\x91\x8e\x8d\x91\x91\x93\x93\x91\x89\x8c\x8c\x87\x84\x85\x85\x85\x8b\x87\x87\x8c\x93\x91'
            b'\x90\x93\x8b\x91\x90\x8c\x87\x8a\x88\x87\x80\x88\x8aa]]]]]]]]f]]e\x99\x9a\x9a\x99\x99\x99\x99\x99\x99'
            b'\x99\x99\x99\x9b\x9a\x9b\x9b\x9d\x9c\x9c\x9d\xa0\x9e\x9d\x9f\x9f\x9e\x9f\xa0\xa1\xa6\xa1\xa0\xa1\xa1'
            b'\xa1\x9e\xa0\xa1\xa3\x9e\xa0\x9d\xa0\x9f\x9f\x9d\x9e\x9d\x9b\x9d\x9d\x9b\x9b\x9b\x9c\x9c\x99\x9b\x9b'
            b'\x95\x88\x93\x8d\x86\x86\x83\x84\x85\x92\x8d\x8a\x8f\x99\x97\x99\x99\x8d\x97\x95\x8e\x87\x87\x87\x86'
            b'\x90\x89\x8e\x8e\x9b\x97\x99\x9b\x93\x9a\x99\x94\x8b\x90\x91\x8b\x8e\x8a\x89\x8e\x98\x90\x91\x97\x98'
            b'\x99\x99\x98\x90\x93\x91\x8d\x89\x88\x89\x88\x92\x89\x8c\x8f\x95\x96\x98\x96\x8f\x93\x95\x8f\x88\x8c'
            b'\x8a\x88\x8b\x87\x88\x8c\x95\x91\x91\x93\x91\x95\x94\x94\x8b\x8e\x8e\x8a\x8a\x89\x89\x8b^\x8e\x8e'
            b'_^]]]]]]]\x9e^^\x9d\x98\x98\x9a\x98\x98\x98\x98\x97\x98\x98\x98\x99\x99\x99\x98\x9b\x9b\x9a\x99\x9b'
            b'\x9b\x9c\x9b\x9b\x9c\x9c\x9c\x9d\xa1\x9c\x9c\x9a\x9c\x9c\x9c\x9c\x9b\x9b\x9b\x9b\x9b\x9c\x9a\x9b\x99'
            b'\x9a\x99\x99\x98\x99\x98\x98\x95\x96\x96\x97\x92\x95\x96\x8e~\x89\x89\x81\x83~}\x81\x91\x89\x87\x8e'
            b'\x91\x93\x94\x91\x85\x8d\x8a\x83\x80\x81\x81\x80\x8a\x85\x88\x8b\x95\x92\x92\x95\x8e\x95\x93\x8e\x84'
            b'\x88\x86\x84\x8b\x84\x85\x88\x92\x8e\x8f\x93\x92\x94\x94\x93\x86\x8d\x8c\x87\x85\x84\x84\x86\x8e\x8a'
            b'\x8a\x8d\x91\x91\x92\x92\x89\x8e\x8f\x88\x84\x85\x85\x84\x89\x88\x88\x8a\x91\x8f\x8e\x91\x8f\x92\x90'
            b'\x8e\x88\x8b\x8b\x88\x88\x86\x86\x88u\x8d\x8b\\[[Z[[[[[fZZ[\x96\x97\x98\x96\x95\x95\x95\x96\x96\x95'
            b'\x95\x96\x97\x97\x96\x97\x98\x98\x97\x98\x98\x99\x98\x99\x9a\x98\x99\x99\x9b\x9a\x9a\x9b\x9b\x9b\x9b'
            b'\x9b\x9a\x9a\x9b\x99\x99\x99\x99\x99\x98\x99\x99\x98\x98\x95\x97\x98\x95\x96\x97\x96\x98\x94\x95\x8e'
            b'\x80\x89\x88\x80\x80~~~\x90\x86\x87\x91\x94\x93\x93\x93\x87\x91\x8e\x85\x80\x83\x81\x82\x8b\x85\x85'
            b'\x8b\x96\x91\x94\x96\x90\x98\x96\x8e\x86\x8c\x8a\x85\x88\x84\x86\x87\x92\x90\x8e\x92\x95\x95\x96\x95'
            b'\x8b\x8f\x8d\x87\x85\x86\x87\x86\x8f\x88\x8a\x8e\x94\x94\x93\x94\x8d\x93\x93\x8e\x87\x87\x8a\x87\x8d'
            b'\x87\x86\x8c\x95\x8f\x93\x94\x91\x94\x95\x93\x8a\x8e\x8e\x8c\x8b\x8a\x8a\x8c\x93\x90\x91\x93`a_`````_```'
            b'\x9c\x9d\x9e\x9b\x9b\x9b\x9b\x9b\x9c\x9b\x9b\x99\x9c\x9c\x9c\x9c\x9e\x9e\xa1\x9e\xa0\x9e\x9f\xa0\xa1'
            b'\xa1\xa0\xa2\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa0\xa1\xa0\xa1\xa0\xa0\xa1\xa0\x9e\xa0\x9f\x9f\x9c\x9e'
            b'\x9d\x9c\x9a\x9b\x9c\x9c\x96\x9a\x9a\x99\x8c\x95\x95\x87\x85\x85\x83\x85\x8f\x88\x86\x90\x98\x97\x97'
            b'\x98\x8f\x96\x95\x8e\x84\x86\x89\x86\x8e\x86\x87\x8c\x99\x93\x91\x98\x95\x99\x99\x95\x8b\x94\x91\x8a'
            b'\x8a\x88\x88\x8a\x93\x90\x93\x94\x98\x98\x98\x98\x90\x91\x94\x90\x87\x88\x88\x88\x8e\x88\x8a\x8c\x95'
            b'\x92\x94\x95\x8e\x96\x93\x93\x87\x8c\x8b\x88\x8b\x87\x8a\x8a\x94\x91\x8f\x93\x93\x94\x94\x94\x8c\x8c'
            b'\x8f\x8b\x88\x88\x88\x89\x92\x8c\x8b\x8e\\\x91\x93\\\\\\\\][\\\\Z\x9aZZ\x9b\x95\x97\x97\x96\x94\x93'
            b'\x95\x95\x94\x95\x95\x95\x97\x97\x95\x97\x98\x98\x98\x98\x99\x99\x99\x99\x99\x99\x99\x9c\x9a\x9a\x9a'
            b'\x9b\x9b\x9a\x9a\x9a\x98\x99\x99\x9c\x98\x99\x99\x99\x97\x98\x98\x97\x95\x97\x96\x95\x94\x95\x95\x94'
            b'\x8e\x92\x93\x8a~\x86\x81~\x80}|\x80\x8e\x85\x8b\x8f\x92\x91\x92\x8f\x86\x8b\x8b\x85\x7f\x80\x81\x80'
            b'\x8b\x85\x85\x8c\x94\x93\x8f\x94\x8c\x91\x93\x8d\x87\x88\x87\x82\x86\x85\x84\x88\x93\x90\x8c\x92\x8e'
            b'\x93\x93\x91\x82\x88\x8a\x84\x83\x81\x83\x84\x8d\x89\x88\x8c\x8f\x8e\x93\x90\n')
