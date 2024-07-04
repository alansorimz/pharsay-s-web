
def create_q1(sentences):
    q1 = []
    for sentence in sentences:
        # print(sentence)
        for s in sentence:
            for _s in sentence:
                string = ""
                if s[0].find("sub") != -1:
                    string += s[2] + "&"

                    if _s[1].find('hasVB') != -1:
                        string += _s[2]
                    elif _s[1].find('hasNN') != -1 and _s[0].find('sub') == -1:
                        string += _s[2]
                    elif _s[1].find('hasNNP') != -1:
                        string += _s[2]
                    else:
                        string = ""
                        continue

                if string != "": q1.append(string)

    return q1