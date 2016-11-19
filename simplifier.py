from sets import Set

def simplify_candidates(candidate):
    sim_candidate = candidate
    for i in range(0, 2):
        if candidate[i][0:4] == 'The ' or candidate[i][0:4] == 'the ':
            sim_candidate[i] = candidate[i][4:]
        elif candidate[i][0:2] == 'A ' or candidate[i][0:2] == 'a ':
            sim_candidate[i] = candidate[i][2:]
        elif candidate[i][0:3] == 'An ' or candidate[i][0:3] == 'an ':
            sim_candidate[i] = candidate[i][3:]
    return sim_candidate

# candidates is a list of size 2, pronoun is the word, sent is a list of dict
def break_by_conn(candidates, tokens):
    can_count = 0
    conn_found = False
    sent1 = []
    sent2 = []

    for i in range(0, len(tokens)):
        if tokens[i]['pos'] == '.': continue
        if conn_found:
            sent2.append(tokens[i])
        elif tokens[i]['pos'] in Set(["IN", "CC"]) and can_count == 2:
            conn_found = True
            conn = tokens[i]
        else:
            if tokens[i]['word'] == candidates[0] or tokens[i]['word'] == candidates[1]:
                can_count += 1
            sent1.append(tokens[i])
    # sent1 and sent2 are list of dict from token. conn is the dict of conn from tokens
    return sent1, sent2, conn




# tokens and dependency are also a list of dict
# def basic_structure(tokens, dependency):
#     # necessary_pos = Set(["NN","NNS", "NNP","NNPS", "VB", "VBD", """"VBP", "IN", "PRP"])
#     for index in range(0,len(tokens)):
#         if tokens[index]['pos'] in Set(["IN", "CC"]):
#             break


