def rankTeams(votes: list[str]) -> str:
    hmap = {}
    if len(votes) == 0:
        return ""
    elif len(votes) == 1:
        return votes[0]
    else:
        for vote in votes:
            for letter in vote:
                if ord(letter) not in hmap:
                    hmap[ord(letter)] = len(vote) - vote.index(letter)
                else:
                    hmap[ord(letter)] += len(vote) - vote.index(letter)

    hmap_sorted = dict(sorted(hmap.items(), key=lambda item: (item[1], -item[0]), reverse=True))

    result = "".join(chr(i) for i in hmap_sorted.keys())

    return result


if __name__ == '__main__':
    print(rankTeams(["ABC","ACB","ABC","ACB","ACB"]))
    print(rankTeams(["WXYZ","XYZW"]))
    print(rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))
    print(rankTeams(["FVSHJIEMNGYPTQOURLWCZKAX","AITFQORCEHPVJMXGKSLNZWUY","OTERVXFZUMHNIYSCQAWGPKJL","VMSERIJYLZNWCPQTOKFUHAXG","VNHOZWKQCEFYPSGLAMXJIUTR","ANPHQIJMXCWOSKTYGULFVERZ","RFYUXJEWCKQOMGATHZVILNSP","SCPYUMQJTVEXKRNLIOWGHAFZ","VIKTSJCEYQGLOMPZWAHFXURN","SVJICLXKHQZTFWNPYRGMEUAO","JRCTHYKIGSXPOZLUQAVNEWFM","NGMSWJITREHFZVQCUKXYAPOL","WUXJOQKGNSYLHEZAFIPMRCVT","PKYQIOLXFCRGHZNAMJVUTWES","FERSGNMJVZXWAYLIKCPUQHTO","HPLRIUQMTSGYJVAXWNOCZEKF","JUVWPTEGCOFYSKXNRMHQALIZ","MWPIAZCNSLEYRTHFKQXUOVGJ","EZXLUNFVCMORSIWKTYHJAQPG","HRQNLTKJFIEGMCSXAZPYOVUW","LOHXVYGWRIJMCPSQENUAKTZF","XKUTWPRGHOAQFLVYMJSNEIZC","WTCRQMVKPHOSLGAXZUEFYNJI"]))