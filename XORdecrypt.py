import binascii

hex_string = "A67BBD94B2B24CBE73E88FE1EE00EA27F0D1A5EC16E622FA84F0E244E824FE87A0E211BD71FA82F1ED14E820FED7A5E116BB2DFAD6A0DE2A9B61BA8FFCB300AB7CADC6F7B552B36DE88EFBA754B066B1C6FDB200BC66B196E6BB47AD75B88EEBF800AB63A7C6E2B552AB7DAD95B2A34FAA78ACC6E0B14CA634BD96FDBA00BE34A383EBF454B775BCC6E6BC45A634BF89E7B844FF71B085FAB54EB871E884F7A057BA71A6C6E6BC45B267AD8AE4B153FF76B1C6FFB141B167E889F4F441FF67AD85E7A645F334AA93E6F44EB07AE585E0AD50AB7BAF94F3A448B677E4C6FFB154B77BACC8B2924FAD34AD9EF3B950B371E4C6F3F446BE77ADCBE6BB0DB975AB83B2B945BA60A188F5F44FAD34A988B2B158BC7CA988F5B10CFF62A187B2B500AB66BD95E6B144FF77A793E0BD45AD38E885FDA14CBB34AA83B2A153BA70E6C6C6BC49AC34A383EBF800A87CA185FAF442B060A0C6E2B552AB7DAD95B2BF45AF60E887F0A74FB361BC83FEAD00AC71AB94F7A00CFF77A793FEB000AB7CAD88B2B645FF61BB83F6F454B034AD9EF1BC41B173ADC6F7BA43AD6DB892F7B000B271BB95F3B345AC3AE8A7B2BA55B276AD94B2BB46FF67A181FCBD46B677A988E6F450AD75AB92FBB741B334AC8FF4B249BC61A492FBB153FF75BA8FE1B100A87DBC8EB2A048B667E887E2A452B075AB8EB2A04FFF70A195E6A649BD61BC8FFCB300B471B195BCDE2A967AE8D7AAE314F334A9C6F0BB4FB434AA9FB28349B378A187FFF473AB75A68AF7AD009571BE89FCA700BB71BB85E0BD42BA70E892FAB100AD71A487E6BD4FB167A08FE2F44FB934A788F7F957BE6DE880E7BA43AB7DA788E1F454B034AB94EBA454B073BA87E2BC59F334A988F6F457BA7ABCC6FDBA00AB7BE882FBA743AA67BBC6E1A445BC7DAE8FF1B54CB36DE892FAB100B975AB92FDA649A575BC8FFDBA00AF66A784FEB14DFF61BB83F6F454B034AB94F7B554BA34A9C6E6A641AF70A789E0F446AA7AAB92FBBB4EF1348188B29E55B36DE8D7ABED16F334A587E6BC45B275BC8FF1BD41B1349B89FEBB4DB07AE8B1BCF467B078A78BF0F453BE7DACDCB2F66ABA62A788E1F441B160A185FBA441AB71ACC6F3F44BBA6DE880F7B554AA66ADC6FDB200AB7CADC6C08761FF55A481FDA649AB7CA5C6F4BB52FF64BD84FEBD43FF7FAD9FB2B752A664BC89F5A641AF7CB1CAB2B54CAB7CA793F5BC00B771E885F7A654BE7DA68AEBF444B670E888FDA000B67ABE83FCA000AB7CADC6F1BB4EBC71B892B2BB46FF64BD84FEBD43FF7FAD9FB2B752A664BC89F5A641AF7CB1C8B0DE2A967AE8D7ABE310FF5EA98BF7A700973AE8A3FEB849AC34A9C6D0A649AB7DBB8EB2B752A664BC89F5A641AF7CAD94B2B554FF60A083B2934FA971BA88FFB14EAB348B89FFB955B17DAB87E6BD4FB167E8AEF7B544AE61A994E6B152AC34E0A1D19C71F634AB89FCB745B662AD82B2BB46FF60A083B2A44FAC67A184FBB849AB6DE889F4F402B17BA6CBE1B143AD71BCC6F7BA43AD6DB892FBBB4EFD38E8CEFCBB57FF77A98AFEB144FF64BD84FEBD43F27FAD9FB2B752A664BC89F5A641AF7CB1CFBEF442AA60E885FDA14CBB34BB83F7F44EB034BF87EBF454B034A18BE2B845B271A692B2BD54F1348188B2E519E827E88EFBA700BC7BA48AF7B547AA71E8A5FEBD46B97BBA82B2974FBC7FBBC6FBBA56BA7ABC83F6F457B775BCC6FAB553FF76AD85FDB945FF7FA689E5BA00BE67E892FAB1008D4789C6F7BA43AD6DB892FBBB4EFF75A481FDA649AB7CA5CAB2B349A97DA681B2B500AF66A985E6BD43BE78E88BF7A048B070E889F4F449B264A483FFB14EAB75BC8FFDBA0CFF75A682B2BD4EFF25F1D1A6F441B17BBC8EF7A600985780B7B2B941AB7CAD8BF3A049BC7DA988B2B54EBB34AB94EBA454B073BA87E2BC45AD38E8ABF3B843B078A5C6D8FA00887DA48AFBB54DAC7BA6C6F6B156BA78A796F7B000A87CA992B2BD53FF7AA791B2BF4EB063A6C6F3A7009B7DAE80FBB10D9771A48AFFB54EFF7FAD9FB2B158BC7CA988F5B10EFF5AA788F7F44FB934BC8EF7A745FF75B896F7B552FF60A7C6FAB556BA34AA83F7BA00AF61BCC6E6BB00AF66A985E6BD43BE78E893E1B10CFF75A682B2A048BA7DBAC6F7B552B36DE88FFCA245B160A189FCF444B670E888FDA000BD71AB89FFB100AF61AA8AFBB700B47AA791FEB144B871E893FCA049B334BC8EF7F452BA67AD87E0B748FF63A995B2B045BC78A995E1BD46B671ACC6F0AD00AB7CADC6D0A649AB7DBB8EB2B34FA971BA88FFB14EAB34A188B2E519E623E6EC989D4EFF25F1D1A4F441B134A995EBB94DBA60BA8FF1F94BBA6DE885E0AD50AB7BBB9FE1A045B234BF87E1F450AA76A48FE1BC45BB34AA9FB28348B660AE8FF7B844FF50A180F4BD45FF75A682B29941AD60A188B29C45B378A587FCF457B77BE4C6FBBA46B361AD88F1B144FF76B1C6C0B54CAF7CE8ABF7A64BB371EF95B2A34FAD7FE889FCF450AA76A48FF1F94BBA6DE882FBA754AD7DAA93E6BD4FB138E882FBA743B37BBB83F6F441FF79AD92FABB44FF7BAEC6E2A142B37DABCBF9B159FF75AF94F7B14DBA7ABCC8B28048B667E88BF7A048B070E889F4F44BBA6DE883EAB748BE7AAF83BEF457B77DAB8EB2A153BA67E883EAA44FB171A692FBB554B67BA6C6FBBA00BE34AE8FFCBD54BA34AE8FF7B844F334AB87FFB100AB7BE884F7F44BB17BBF88B2B553FF50A180F4BD45F25CAD8AFEB941B134A383EBF445A777A087FCB345F1349C8EFBA700A875BBC6E6BC45FF72A194E1A000AF61AA8AFBA748BA70E896E0B543AB7DAB87FEF44DBA60A089F6F446B066E883E1A041BD78A195FABD4EB834A9C6E1BC41AD71ACC6E1B143AD71BCCBF9B159FF7BBE83E0F441B134A993E6BC45B160A185F3A045BB34E084E7A000B17BBCC6E2A649A975BC83BBF443B079A593FCBD43BE60A189FCA700BC7CA988FCB14CFF63A192FABB55AB34BD95FBBA47FF75E896E0BD4FAD34BB8EF3A645BB34BB83F1A645AB3AE8ABF7A64BB371EF95B2F650AA76A48FF1F94BBA6DE587F5A645BA79AD88E6F454BA77A088FBA555BA36E884F7B741B271E88DFCBB57B134A995B29945AD7FA483B5A7008F61B29CFEB153F334A988F6F457BE67E88FFCA245B160AD82B2BD4EFF25F1D1A6F441B170E896E7B64CB667A083F6F449B134F9DFA5EC0ED51E8188B2E519E823E887B2B345B171BA87FEBD5ABE60A189FCF44FB9348B89F1BF53F867E895F1BC45B271E891F3A700B67AAC83E2B14EBB71A692FEAD00B67ABE83FCA045BB34AA9FB2864FB1349A8FE4B153AB38E8A7F6BD008C7CA98BFBA600BE7AACC6DEB14FB175BA82B29544B371A587FCF800BE78A4C6E6BC45B134A992B299698B3AE8B2FAB100B375BC92F7A600BE61BC8EFDA653FF64BD84FEBD53B771ACC6E6BC45B666E891FDA64BFF7DA6C6A3ED17E738E887FCB000AB7CADC6F3B847B066A192FAB900BC75A583B2A04FFF76ADC6F9BA4FA87AE887E1F4728C55E4C6F4A64FB234BC8EF7BD52FF7DA68FE6BD41B367E6C6C08761FF61BB83E1F445A764A788F7BA54B675BC8FFDBA00B27BAC93FEBB00BE34B894FDB055BC60E889F4F454A87BE890F7A659FF78A994F5B100AF66A18BF7A70CFF60A7C6F7BA43AD6DB892B2B54EBB34AC83F1A659AF60E4C6E2B152B97BBA8BFBBA47FF76A792FAF450AA76A48FF1F44BBA6DE883FCB752A664BC8FFDBA00BE7AACC6E2A142B37DABC6F9B159FF70A181FBA041B334BB8FF5BA41AB61BA83BCF469AB67E895F7B755AD7DBC9FB2BD53FF77A788FCB143AB71ACC6E6BB00AB7CADC6F7AC54AD71A583B2B049B972A185E7B854A634A780B2B241BC60A794FBBA47FF78A994F5B100B67ABC83F5B152AC38E887B2A452B076A483FFF446B066E891FABD43B734BC8EF7A645FF7DBBC6FCBB00B47AA791FCF445B972A185FBB14EAB34AF83FCB152BE78E892F7B748B17DB993F7FA00967AE8D7ABE319F334858FF1BC41BA78E8A9BCF472BE76A188B2A455BD78A195FAB144FF75E894F7B841AB71ACC6F1A659AF60A795EBA754BA79E892FAB554FF7DBBC6E2A64FBD75AA8AEBF453BA77BD94F7F441AC34A489FCB300BE67E892FAB100B975AB92FDA649A575BC8FFDBA00B072E892FAB100AF61AA8AFBB700B471B1C6E0B14DBE7DA695B2B049B972A185E7B854FF39E88FE6F452BA79A98FFCA700BE7AE887E1A755B264BC8FFDBA00AB7CA992B286739E34A98AE1BB00BA7AA289EBA700AB7CA195B2A745BC61BA8FE6AD0ED51E9B8FFCB745FF60A083B2E519E824BBCAB2B500B375BA81F7F44EAA79AA83E0F441B170E890F3A649BA60B1C6FDB200BA7AAB94EBA454B67BA6CAB2B049B87DBC87FEF453B673A687E6A152BA38E88DF7AD00BE73BA83F7B945B160E4C6F3BA44FF7BBC8EF7A600AB71AB8EFCBD51AA71BBC6FAB556BA34AA83F7BA00BB71BE83FEBB50BA70E88FFCF454B771E880FBB14CBB34A780B2A455BD78A185BFBF45A634AB94EBA454B073BA87E2BC59F1349C8EF7F465B353A98BF3B800BC66B196E6BB53A667BC83FFF800B67ABE83FCA045BB34AA9FB28041B771BAC6D7B867BE79A98AB2A645B37DAD95B2BB4EFF60A083B2A749B27DA487E0F441B170E894F7B841AB71ACC6FABD47B734A483E4B14CFF7BAEC6F6BD46B97DAB93FEA059FF7BAEC6E6BC45FF70A195F1A645AB71E88AFDB341AD7DBC8EFFF450AD7BAA8AF7B90CFF75BBC6F6BB45AC34BC8EF7F443B37BBB83FEAD00AD71A487E6B144FF509BA7BEF457B77DAB8EB2A341AC34AC83E4B14CB064AD82B2B554FF60A083B28173FF5AA992FBBB4EBE78E8B5F7B755AD7DBC9FB29547BA7AAB9FB2FC6E8C55E1C6F3BA44FF64BD84FEBD53B771ACC6F0AD00915D9BB2B2B553FF75E896E0BB50B067AD82B2A754BE7AAC87E0B00ED51E9C8EF7F449B160BA89F6A143AB7DA788B2BB46FF71A48AFBA454B677E885E7A656BA34AB94EBA454B073BA87E2BC59FF76B1C6DCB141B3348389F0B849AB6EE887FCB000897DAB92FDA600927DA48AF7A60CFF7DA682F7A445B170AD88E6B859FF75A682B2A749B261A492F3BA45B061BB8AEBF449B134BC8EF7F44DB670E5D7ABEC10AC38E88EF3A700A67DAD8AF6B144FF7AAD91B2A455BD78A185BFBF45A634A98AF5BB52B660A08BE1F442BE67AD82B2BB4EFF60A083B2B049AC77BA83E6B100B37BAF87E0BD54B779E896E0BB42B371A5C8B2954CAB7CA793F5BC00B275BC8EF7B941AB7DAB87FEB859FF79A794F7F443B079B88AF7AC0CFF71A48AFBA454B677E885E7A656BA67E896E0BB56B670ADC6E1B941B378AD94B2BF45A634BB8FE8B153FF75A682B2B241AC60AD94B2BB50BA66A992FBBB4EAC34AE89E0F441AF64BA89EABD4DBE60AD8AEBF445AE61A190F3B845B160E883E1A049B275BC83F6F453BA77BD94FBA059F1"

def byte_to_binary(n):
    return ''.join(str((n & (1 << i)) and 1) for i in reversed(range(8)))

def hex_to_binary(h):
    return ''.join(byte_to_binary(ord(b)) for b in binascii.unhexlify(h))

print hex_to_binary(hex_string)
