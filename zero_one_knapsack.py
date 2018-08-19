# DP 0/1 knapsack problem
# Given a max carrying weight and items of a set value and weight
# determine the maximum value you can carry and the items to take
import pprint

def init_list(weight, items):
    l = [[None for _ in range(weight + 1)] for _ in range(len(items))]
    for a in l:
        a[0] = 0
    for a in range(len(l[0])):
        if a >= items[0]:
            l[0][a] = items[0]

    return l

def knapsack(ws, vals, dp):
    for item in range(1, len(dp)):
        for cap in range(len(dp[0])):
            if dp[item][cap] == 0: continue
            elif cap < ws[item]:
                dp[item][cap] = dp[item - 1][cap]
            else:
                curr_val = vals[ws[item]]
                dp[item][cap] = max(curr_val + dp[item - 1][cap - ws[item]],
                                    dp[item - 1][cap])
    return dp[-1][-1]

# to see which items were selected:
# if an element is greater than the element above it, that means
# the item at that row was selected. Add it to a list and go up (picked
# an item) and left by the weight of the item (remaining capacity)
def which_items(dp, ws):
    ci = len(dp) - 1
    cc = len(dp[0]) - 1
    items = []
    while dp[ci][cc] != 0 and ci >= 0 and cc >= 0:
        if dp[ci][cc] > dp[ci - 1][cc]:
            items.append(ws[ci])
            cc -= ws[ci]
        ci -= 1
    return items


if __name__ == '__main__':
    cap = 7
    vals = {1: 1, 3: 4, 4: 5, 5: 7}
    ws = (1, 3, 4, 5)
    l = init_list(cap, ws)

    max_weight = knapsack(ws, vals, l)
    items = which_items(l, ws)
    print(items)
    print(max_weight)

    for x in l:
        for y in x:
            print('{:<2}'.format(y), end=' ')
        print()

