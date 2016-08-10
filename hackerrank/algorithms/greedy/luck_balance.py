def max_luck(nt, max_l_important):
    non_im = sum([x[0] for x in nt if x[1] == 0])
    important = sorted([x[0] for x in nt if x[1] == 1], reverse=True) 
    sum_loses = sum(important[max_l_important:])
    sum_wins = sum(important[:max_l_important])
    return (non_im + sum_wins) - sum_loses
          


nested_list = [(5,1), (2,1), (1,1), (8,1), (10,0), (5,0)]
print max_luck(nested_list, 3)