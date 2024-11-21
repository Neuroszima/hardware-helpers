# to fix: prepare a simple reader-writer for binary format and convert this file into binary
bin_data = b'#800002000xxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' \
           b'xxxxxxxxxxxxxxxxxxxxxxxxxyxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxyxxxxxxxxxxxxx' \
           b'xxxxxxxxxxwxxxxxxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxwxxxwwxxxwwwwxwxxwxwwwwwwwwwwwww' \
           b'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwxwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww' \
           b'wwwwwwwwxwwwwwxwwwwwwwwwwwwwwwwwwwwwwxwwwwwwwwwwxxwwwwwwwwwwxxwwwwxwwwwwxxwwwww' \
           b'wwxxxxwwwwwwwxwxwxxxxxxxxxxxxxxxxxxxxxxxxxxxxyxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' \
           b'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' \
           b'xxxxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxwxxxwxxxxwwwxwxwwwwxwwwwwww' \
           b'wwwwwwwwwwwwxwwwwwwwwwwwxwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww' \
           b'wwwwwwwwwwwwwwwwwwwwwwwwwwwwxwwwwwwwwwwwwwxxwwwwwwwxwwwwwxwwwxwwwxwwxwwwwwxwxww' \
           b'wwwxwxwwxwxxxxwwwxxxxxxxwxxwxxxxxxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' \
           b'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' \
           b'xxxxxxxxxxxxxxxxwxxxxxxxxxxxxxxxxxxyz||}}|||||{{{{{{{{{{{{{{\x81\x84\x87\x86\x85' \
           b'\x85\x84\x84\x84\x84\x83\x82\x81\x81\x80\x80\x7f\x7f\x7f~}|{|{zzyyyxxxxxwwwvvuv' \
           b'uuuuuuuuttttstsssssssrrrrrqqqqppppppooooooooonmmllllllmmmmmmnnmnnnnnnnnonoooooo' \
           b'nnonnnnmnmnnnmnonnoopppppppqqqrrrrrsrssssssssttttttttttttttuutuuuuuuuuuuvvuvvvu' \
           b'vvvvwwwyyxyxyyyzzzzzzz{{|||}}~~}~~}}~~~~~~~~~~}}}}}}~~~~~~~~~~~~~\x7f~\x7f\x7f' \
           b'\x7f\x7f~\x7f\x7f\x7f\x7f\x7f\x7f\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80' \
           b'\x82\x81\x82\x82\x82\x82\x82\x81\x81\x81\x81\x81\x81\x81\x80\x80\x80\x80\x80\x80' \
           b'\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x7f\x80\x80\x7f\x80\x80\x80\x80\x80' \
           b'\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x7f\x7f\x7f~~~~}}}}}}}||||||{|{{{{' \
           b'{{zz{zzzzzzzzzzzzzzyyyzzyyyyyyyzyyzyyyyxxwwwwwwvuvvuuuutttsssrrrrrrrrrrrrrrrrrr' \
           b'rrrrrrrrrqrqqqqqrqpqqqpppppppppooooooooooonmmmmmmlmmmmmmnonnooooooooooooooooooo' \
           b'oooooooooooooooppqpqrrrrrrrrrrsssststttttttttttttttutttuuuuuuuuvuvvuvvvvuvvvvvv' \
           b'vxwxxyxyxyyyzzzzz{z{{||}}}}}~}}}}~~}~~~~~}~}}}}}}}~~~~}~~~~~~~~~~\x7f~~~~\x7f~' \
           b'\x7f\x7f\x7f\x7f\x7f\x80\x80\x80\x80\x80\x80\x80\x80\x81\x81\x82\x81\x82\x82\x82' \
           b'\x81\x81\x81\x81\x81\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x7f\x7f\x80\x80' \
           b'\x7f\x7f\x80\x80\x7f\x7f\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80' \
           b'\x80\x80\x80\x7f\x7f~~~~~}}}}}}|||||{{{{{{{zzzzzzzzzzzzzzzyzyzzzzyyyyyyyyyyyyyyy' \
           b'xyyxxxwvwwvvvvuuuttuttssssrqrrrqqrrrrqqqqqqrrrrrrrrrrrqqqrqrqrqpqqqpqppppppppooo' \
           b'oopoooonmmmmmmmmmmmnoooooooooooooooooooooooooooooooooooooppppqqrqrrrrrrssssstst' \
           b'tttttttttttttuuuutuuuuuuuvvvuuuvvvvwvvvvwvv\n'