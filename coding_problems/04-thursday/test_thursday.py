# pylint: skip-file

import pytest

from thursday import best_friend


def test_best_friend_with_known_inputs_1():
    assert best_friend('he headed to the store', 'h', 'e') == True


def test_best_friend_with_known_inputs_2():
    assert best_friend('i found an ounce with my hound', 'o', 'u') == True


def test_best_friend_with_known_inputs_3():
    assert best_friend('those were their thorns they said', 't', 'h') == True


def test_best_friend_with_known_inputs_4():
    assert best_friend('we found your dynamite', 'd', 'y') == False


def test_best_friend_with_known_inputs_5():
    assert best_friend('look they took the cookies', 'o', 'o') == False


def test_best_friend_with_known_inputs_6():
    assert best_friend('a test', 't', 'e') == False


def test_best_friend_with_known_inputs_7():
    assert best_friend('abcdee', 'e', 'e') == False


def test_best_friend_with_known_inputs_8():
    assert best_friend('abcde', 'e', 'e') == False


@pytest.mark.parametrize("txt,a,b,result",
                         [("fqbseqbkqboqb", "q", "b", True),
                          ("ns", "a", "g", True),
                             ("fdupitrit sitxritz nitc", "i", "t", True),
                             ("zo", "f", "b", True),
                             ("trl", "r", "l", True),
                             ("xkzu kjwzukozu", "z", "u", True),
                             ("dtk rtk qmstkq atkgg xfc ctkhxttkt", "t", "k", False),
                             ("j jqe", "q", "e", True),
                             ("xi th mhserw gr", "u", "z", True),
                             ("b", "n", "z", True),
                             ("fjf eej u cywq us l", "c", "j", False),
                             ("oollkullallq awllrplllfll hlltlw", "l", "l", False),
                             ("jrrtiv rdxcu hddtn mc", "i", "x", False),
                             ("kmi", "c", "x", True),
                             ("y owaski hrq ypwel iubj kmmhqv", "b", "z", False),
                             ("mrzhm rzhbzha", "z", "h", True),
                             ("j yjuvjuyjuy hjubjuuju pju", "j", "u", False),
                             ("mupa qfpxnr v", "i", "m", True),
                             ("wjyijye yn wk", "j", "y", True),
                             ("bzfnlt", "c", "l", True),
                             ("ycxz vaya mzzpdi gm s pq", "b", "g", True),
                             ("hpwmzuz jzuyciex ezuqduge bzupjwj", "z", "u", False),
                             ("iy jj rfxs gj frcnup gvn", "o", "t", True),
                             ("hxqexqvxqmapxq awxq oxqrcdqxq zxqvexq k cxqz",
                              "x", "q", True),
                             ("tauxaucvauq fqrdau dlibauoauv xaau ulh keaubpaugau",
                              "a", "u", False),
                             ("y cc py gz wo rj", "s", "t", True),
                             ("gjjd el ljdtjdojdgjd", "j", "d", False),
                             ("fbq tbq ofbqjhobqfbq ibqmcbqo", "b", "q", True),
                             ("nxasi aqfe mon esjtc yom rj", "a", "q", False),
                             ("ydjarjauqjaoja xvjaiks zjaija", "j", "a", True),
                             ("psvmiksvm isv vvsvgsvx mssvdtrg vsvcosvzvsvwsv",
                              "s", "v", False),
                             ("szqqw tfmm qzpm", "y", "x", True),
                             ("gpsqnds edsfdsndsydsr rdsedsrdsudscmds ixjgds wdsddsipdsq",
                              "d", "s", False),
                             ("mgehj a rdehwehw lkqehsweh", "e", "h", True),
                             ("qcjvul bqlxa pkcg pzqder", "y", "b", True),
                             ("ycsucsg", "c", "s", True),
                             ("ps jlnw sln elnglnz plnnlnltlndln", "l", "n", False),
                             ("uqqgtxgtq mgtj pgtdgtfegtb kqgtptgt t", "g", "t", True),
                             ("i qwyyb", "a", "z", True),
                             ("mwubcwu vwu iwu j swul", "w", "u", True),
                             ("hl", "t", "a", True),
                             ("nfmd z jqog hquz i", "l", "h", True),
                             ("fkfxvkf kxqkf lhfwa dkflkfslh f", "k", "f", False),
                             ("emmgzzmmyv gmmogl ibmmenmml ummqtmmamm rmmmbmm qmmkvmmzmmwmm",
                              "m", "m", False),
                             ("hfyl xfydfy b tfybfyqfy hfyu efylfy", "f", "y", True),
                             ("ra fex myt axmmq mwkp", "a", "r", False),
                             ("erjya ayhstr kiha enr", "o", "j", True),
                             ("ctra mmrgb dhul eccsfs ottfh", "h", "g", False),
                             ("wfwkpewkdwkowk", "w", "k", False),
                             ("hktd jrkae vhhymv", "q", "h", True),
                             ("w fm dpul", "x", "v", True),
                             ("orzotj jcptki j xyb fh", "b", "z", False),
                             ("plx sx", "l", "x", True),
                             ("ylek el", "y", "u", False),
                             ("tuhzw mjzw mjfm w", "z", "w", True),
                             ("ygd fgdnagd qarmgdmgds ngdxdogdi gpxgdr xggdkygdb",
                              "g", "d", False),
                             ("kszzxsz iszvszk", "s", "z", True),
                             ("xux isbbcbb ibbzbblbb qbbubbvybbybb tgbbjbb zbbftbbr",
                              "b", "b", False),
                             ("ijlgmlgglg blggo", "l", "g", True),
                             ("kuet", "e", "d", False),
                             ("iou xsx nsxasxt wsxq nsxe", "s", "x", True),
                             ("llzmlzurlz yndlzblz clzolzl xrlzrlzslzd llzl bblz",
                              "l", "z", False),
                             ("vhmzphmzhmxhml", "h", "m", True),
                             ("j k db", "t", "o", True),
                             ("jlgc blz", "m", "j", True),
                             ("bmg g", "s", "s", True),
                             ("xfzsxr binvgm spciwx msf kzcdi pkwgcy", "d", "t", False),
                             ("u", "m", "f", True),
                             ("rgc cmgnwg bep lr ulam", "u", "t", False),
                             ("t nsafczesa k nusaf", "s", "a", True),
                             ("zaeeae ipkaedae aaexaejaeyxhae saejaexaedae qxaemaegae dkgaej",
                              "a", "e", False),
                             ("gxwpqxwdxwixwjxw uxwhyghxw bxwikxw qxwaxw",
                              "x", "w", True),
                             ("xfksb hen imkl", "r", "p", True),
                             ("ladhddh udv gdh fdhv unydhqhdh gdhkdhpdhuhadh",
                              "d", "h", False),
                             ("mrlgb bhxsem muqvj vhys yg", "s", "i", False),
                             ("ysv lwv zydrasf in", "y", "d", False),
                             ("vcsccsa qkicskcs hskgcsycs us", "c", "s", False),
                             ("a cv egd", "k", "v", True),
                             ("wyg txdtk kcxusn uxxor lfcku", "l", "d", False),
                             ("dgi xygihjgin", "g", "i", True),
                             ("kdvgy omgs m dyqbnn", "h", "z", True),
                             ("hhs xhswmhsphsho fghs wyqbhskhst bhsqmhswhs f",
                              "h", "s", False),
                             ("gvnv c bcx foag ylhafq i", "d", "e", True),
                             ("cx g fda p", "k", "d", True),
                             ("ujhf", "m", "j", True),
                             ("r ev a b", "b", "d", False),
                             ("wz gst iiq", "e", "q", True),
                             ("mffdtff", "f", "f", False),
                             ("kqtqjb d pc v zwxgx", "f", "i", True),
                             ("aipp ewubu afrgf fjxl", "k", "r", True),
                             ("vd gfjjo m iuiszx", "c", "o", True),
                             ("ghttbd", "t", "b", False),
                             ("laddup ybwm aao vwhxu fwwjv smgil", "a", "q", False),
                             ("odpnkdpek pdp", "d", "p", True),
                             ("xnonbno az om pnocnosbuf ynnow onoenoanotnof",
                              "n", "o", False),
                             ("m pn o zx", "g", "j", True),
                             ("pubwubwebwambw qbwybwqbwjbwhw lmbwmbws zbwicbw sbw",
                              "b", "w", True),
                             ("wxv gvxvnyxvzxv qvxv bxvtxvoxva lj", "x", "v", True),
                             ("rxb fvl", "q", "c", True),
                             ("sfsot xsot ar motrot", "o", "t", True)])
def test_random_test_cases(txt, a, b, result):
    assert best_friend(txt, a, b) == result
